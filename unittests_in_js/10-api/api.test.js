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

describe('GET /available_payments', () => {
  it('returns correct status and JSON body', (done) => {
    request.get({ url: `${BASE}/available_payments`, json: true }, (err, res, body) => {
      expect(res.statusCode).to.equal(200);
      expect(body).to.deep.equal({
        payment_methods: { credit_cards: true, paypal: false },
      });
      done();
    });
  });

  it('Content-Type is application/json', (done) => {
    request.get(`${BASE}/available_payments`, (err, res) => {
      expect(res.headers['content-type']).to.match(/application\/json/);
      done();
    });
  });
});

describe('POST /login', () => {
  it('returns "Welcome Betty" for userName=Betty', (done) => {
    request.post(
      { url: `${BASE}/login`, json: { userName: 'Betty' } },
      (err, res, body) => {
        expect(res.statusCode).to.equal(200);
        expect(body).to.equal('Welcome Betty');
        done();
      }
    );
  });

  it('returns "Welcome " when userName is missing', (done) => {
    request.post(
      { url: `${BASE}/login`, json: {} },
      (err, res, body) => {
        expect(res.statusCode).to.equal(200);
        expect(body).to.equal('Welcome ');
        done();
      }
    );
  });
});


