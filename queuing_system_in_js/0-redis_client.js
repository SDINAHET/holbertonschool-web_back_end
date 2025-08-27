// 0-redis_client.js
import redis from 'redis';

// Création du client Redis (127.0.0.1:6379 par défaut)
const client = redis.createClient();

// Connexion réussie
client.on('connect', () => {
  console.log('Redis client connected to the server');
});

// Connexion échouée
client.on('error', (err) => {
  console.log(`Redis client not connected to the server: ${err}`);
});
