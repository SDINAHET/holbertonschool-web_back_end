const http = require('http');

// Create the HTTP server
const app = http.createServer((req, res) => {
  // Set the response header to plain text
  res.writeHead(200, { 'Content-Type': 'text/plain' });

  // Send the response body
  res.end('Hello Holberton School!');
});

// Make the server listen on port 1245
app.listen(1245);

// Export the server for reuse or testing
module.exports = app;
