// 7-job_processor.js
import kue from 'kue';

const queue = kue.createQueue();

// Blacklisted numbers
const blacklistedNumbers = ['4153518780', '4153518781'];

function sendNotification(phoneNumber, message, job, done) {
  // Track initial progress
  job.progress(0, 100);

  // Check blacklist
  if (blacklistedNumbers.includes(phoneNumber)) {
    return done(new Error(`Phone number ${phoneNumber} is blacklisted`));
  }

  // Halfway
  job.progress(50, 100);

  // Log sending
  console.log(`Sending notification to ${phoneNumber}, with message: ${message}`);

  // Done successfully
  done();
}

// Process jobs in queue "push_notification_code_2" with concurrency = 2
queue.process('push_notification_code_2', 2, (job, done) => {
  const { phoneNumber, message } = job.data;
  sendNotification(phoneNumber, message, job, done);
});
