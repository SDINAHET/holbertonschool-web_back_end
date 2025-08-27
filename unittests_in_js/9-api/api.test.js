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
  }); // <-- ferme le describe "Index page" ICI
  
  describe('Cart page', () => {
  it('Correct status code when :id is a number', (done) => {
    request.get(`${BASE}/cart/12`, (err, res) => {
      if (err) return done(err);
      expect(res.statusCode).to.equal(200);
      done();
    });
  });

  it('Correct result when :id is a number', (done) => {
    request.get(`${BASE}/cart/12`, (err, res, body) => {
      if (err) return done(err);
      expect(body).to.equal('Payment methods for cart 12');
      done();
    });
  });

  it('404 when :id is NOT a number', (done) => {
    request.get(`${BASE}/cart/hello`, (err, res) => {
      if (err) return done(err);
      expect(res.statusCode).to.equal(404);
      done();
    });
  });

  // (optionnel) un autre exemple numérique
  it('Works with other numeric ids', (done) => {
    request.get(`${BASE}/cart/0`, (err, res, body) => {
      if (err) return done(err);
      expect(res.statusCode).to.equal(200);
      expect(body).to.equal('Payment methods for cart 0');
      done();
    });
  });
});
