// 10-api/api.js
const express = require('express');

const app = express();

// Middleware pour parser le JSON du body
app.use(express.json());

app.get('/', (req, res) => {
  res.send('Welcome to the payment system');
});

// :id uniquement numérique grâce au pattern ([0-9]+)
app.get('/cart/:id([0-9]+)', (req, res) => {
  const { id } = req.params;
  res.send(`Payment methods for cart ${id}`);
});

// Nouveau: GET /available_payments (JSON)
app.get('/available_payments', (req, res) => {
  res.json({
    payment_methods: {
      credit_cards: true,
      paypal: false,
    },
  });
});

// Nouveau: POST /login (texte)
app.post('/login', (req, res) => {
  const userName = (req.body && req.body.userName) ? req.body.userName : '';
  res.send(`Welcome ${userName}`);
});

const PORT = 7865;
app.listen(PORT, () => {
  console.log('API available on localhost port 7865');
});

module.exports = app;
