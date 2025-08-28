// 100-seat.js
// Run with: npm run dev 100-seat.js

const express = require('express');
const redis = require('redis');
const kue = require('kue');
const { promisify } = require('util');

const app = express();
const port = 1245;

// ----- Redis client & helpers -----
const client = redis.createClient();
const getAsync = promisify(client.get).bind(client);
const setAsync = promisify(client.set).bind(client);

async function reserveSeat(number) {
  // Store as string to match example output
  await setAsync('available_seats', String(number));
}

async function getCurrentAvailableSeats() {
  const val = await getAsync('available_seats');
  // Return string representation (the API responds with strings)
  return val === null ? null : val;
}

// Initialize available seats to 50 on startup
client.on('connect', async () => {
  try {
    await reserveSeat(50);
  } catch (err) {
    console.error('Failed to initialize seats:', err.message);
  }
});

// ----- Reservation flag -----
let reservationEnabled = true;

// ----- Kue queue -----
const queue = kue.createQueue();

// ----- Routes -----

// GET /available_seats -> {"numberOfAvailableSeats":"50"}
app.get('/available_seats', async (_req, res) => {
  try {
    const seats = await getCurrentAvailableSeats();
    res.json({ numberOfAvailableSeats: seats ?? '0' });
  } catch (err) {
    // Always JSON
    res.status(500).json({ error: 'Cannot retrieve number of available seats' });
  }
});

// GET /reserve_seat
// - If blocked -> {"status":"Reservation are blocked"}
// - Else create job -> {"status":"Reservation in process"} or {"status":"Reservation failed"}
app.get('/reserve_seat', (_req, res) => {
  if (!reservationEnabled) {
    return res.json({ status: 'Reservation are blocked' });
  }

  const job = queue.create('reserve_seat', {}).removeOnComplete(true);

  job.save((err) => {
    if (!err) {
      res.json({ status: 'Reservation in process' });
    } else {
      res.json({ status: 'Reservation failed' });
    }
  });

  job.on('complete', () => {
    console.log(`Seat reservation job ${job.id} completed`);
  });
  job.on('failed', (errMsg) => {
    console.log(`Seat reservation job ${job.id} failed: ${errMsg}`);
  });
});

// GET /process
// - Returns {"status":"Queue processing"} immediately
// - Then processes jobs: decrement seats, disable when 0, enforce bounds
let processingStarted = false;

app.get('/process', (_req, res) => {
  res.json({ status: 'Queue processing' });

  // Set up the processor only once
  if (processingStarted) return;
  processingStarted = true;

  queue.process('reserve_seat', async (job, done) => {
    try {
      const currentStr = await getCurrentAvailableSeats();
      const current = parseInt(currentStr, 10);

      const newCount = current - 1;

      if (Number.isNaN(current)) {
        return done(new Error('Seat count not initialized'));
      }

      if (newCount < 0) {
        return done(new Error('Not enough seats available'));
      }

      await reserveSeat(newCount);

      if (newCount === 0) {
        reservationEnabled = false;
      }

      return done();
    } catch (err) {
      return done(err);
    }
  });
});

// ----- Start server -----
app.listen(port, () => {
  console.log(`Server listening on port ${port}`);
});
