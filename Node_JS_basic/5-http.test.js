const http = require('http');
const { exec } = require('child_process');
const app = require('./5-http');

describe('HTTP Server Test', () => {
  let server;

  beforeAll((done) => {
    server = app.listen(1245, done);
  });

  afterAll((done) => {
    server.close(done);
  });

  it('should return "Hello Holberton School!" for / endpoint', async () => {
    const options = {
      hostname: 'localhost',
      port: 1245,
      path: '/',
      method: 'GET',
    };

    const response = await new Promise((resolve, reject) => {
      const req = http.request(options, (res) => {
        let data = '';
        res.on('data', (chunk) => {
          data += chunk;
        });
        res.on('end', () => resolve(data));
      });

      req.on('error', (err) => reject(err));
      req.end();
    });

    expect(response).toBe('Hello Holberton School!');
  });

  it('should return students list for /students endpoint', async () => {
    const options = {
      hostname: 'localhost',
      port: 1245,
      path: '/students',
      method: 'GET',
    };

    const response = await new Promise((resolve, reject) => {
      const req = http.request(options, (res) => {
        let data = '';
        res.on('data', (chunk) => {
          data += chunk;
        });
        res.on('end', () => resolve(data));
      });

      req.on('error', (err) => reject(err));
      req.end();
    });

    expect(response.startsWith('This is the list of our students')).toBe(true);
  });
});
