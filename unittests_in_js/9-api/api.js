// 9-api/api.js
const express = require('express');

const app = express();

app.get('/', (req, res) => {
  res.send('Welcome to the payment system');
});

// :id uniquement numérique grâce au pattern ([0-9]+)
app.get('/cart/:id([0-9]+)', (req, res) => {
  const { id } = req.params;
  res.send(`Payment methods for cart ${id}`);
});

const PORT = 7865;
app.listen(PORT, () => {
  console.log('API available on localhost port 7865');
});

module.exports = app;
