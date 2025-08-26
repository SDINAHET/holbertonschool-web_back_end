// 6-payment_token.test.js
const assert = require('assert');
const getPaymentTokenFromAPI = require('./6-payment_token');

describe('getPaymentTokenFromAPI', () => {
  it('resolves with the expected object when success=true', (done) => {
    getPaymentTokenFromAPI(true)
      .then((res) => {
        assert.deepStrictEqual(res, { data: 'Successful response from the API' });
        done();
      })
      .catch(done); // en cas d'erreur, ne pas oublier d’appeler done(err)
  });
});
