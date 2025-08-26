// 6-payment_token.js
function getPaymentTokenFromAPI(success) {
  if (success) {
    return Promise.resolve({ data: 'Successful response from the API' });
  }
  // Sinon, la fonction ne fait rien (retourne undefined)
}

module.exports = getPaymentTokenFromAPI;
