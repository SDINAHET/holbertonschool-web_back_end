const express = require('express');

// Create an Express app
const app = express();

// Define the root endpoint
app.get('/', (req, res) => {
  res.send('Hello Holberton School!');
});

// Make the server listen on port 1245
app.listen(1245, () => {
  console.log('Server is running on port 1245');
});

// Export the app for reuse or testing
module.exports = app;
