const http = require('http');
const app = require('./4-http');

describe('HTTP Server Test', () => {
  let server;

  beforeAll((done) => {
    server = app.listen(1245, done);
  });

  afterAll((done) => {
    server.close(done);
  });

  it('should return "Hello Holberton School!" for any endpoint', async () => {
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

  it('should return "Hello Holberton School!" for any other endpoint', async () => {
    const options = {
      hostname: 'localhost',
      port: 1245,
      path: '/random',
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
});
