const request = require('supertest');
const app = require('./6-http_express');

describe('6-http_express', () => {
  it('should return "Hello Holberton School!" for the root route', async () => {
    const response = await request(app).get('/');
    expect(response.statusCode).toBe(200);
    expect(response.text).toBe('Hello Holberton School!');
  });

  it('should return a 404 error for an undefined route', async () => {
    const response = await request(app).get('/undefined_route');
    expect(response.statusCode).toBe(404);
    expect(response.text).toContain('Cannot GET /undefined_route');
  });
});
