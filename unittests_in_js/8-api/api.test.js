const request = require('request');
const { expect } = require('chai');

const BASE = 'http://localhost:7865';

describe('Index page', () => {
  it('Correct status code?', (done) => {
    request.get(`${BASE}/`, (err, res) => {
      if (err) return done(err);
      expect(res.statusCode).to.equal(200);
      done();
    });
  });

  it('Correct result?', (done) => {
    request.get(`${BASE}/`, (err, res, body) => {
      if (err) return done(err);
      expect(body).to.equal('Welcome to the payment system');
      done();
    });
  });

  it('Content-Type header looks right?', (done) => {
    request.get(`${BASE}/`, (err, res) => {
      if (err) return done(err);
      expect(res.headers['content-type']).to.match(/text\/html/);
      done();
    });
  });
});
