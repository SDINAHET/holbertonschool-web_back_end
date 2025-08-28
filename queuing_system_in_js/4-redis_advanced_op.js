import redis from 'redis';

const client = redis.createClient();

client.on('connect', () => {
  console.log('Redis client connected to the server');
});

client.on('error', (err) => {
  console.log(`Redis client not connected to the server: ${err}`);
});

// Key for the hash
const key = 'HolbertonSchools';

// Hash values to store
const schools = {
  Portland: 50,
  Seattle: 80,
  'New York': 20,
  Bogota: 20,
  Cali: 40,
  Paris: 2,
};

// Store each field/value in the hash
for (const [field, value] of Object.entries(schools)) {
  client.hset(key, field, value, redis.print);
}

// Retrieve and display the hash
client.hgetall(key, (err, reply) => {
  if (err) {
    console.log(err);
  } else {
    console.log(reply);
  }
});
