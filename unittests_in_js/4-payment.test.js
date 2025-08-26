// 4-payment.test.js
const assert = require('assert');
const sinon = require('sinon');
const Utils = require('./utils');
const sendPaymentRequestToApi = require('./4-payment');

describe('sendPaymentRequestToApi (with stub)', () => {
  it('should stub Utils.calculateNumber to return 10 and log the correct total', () => {
    const calcStub = sinon.stub(Utils, 'calculateNumber').returns(10);
    const consoleSpy = sinon.spy(console, 'log');

    sendPaymentRequestToApi(100, 20);

    // Le stub a bien été utilisé avec les bons arguments
    assert.strictEqual(calcStub.calledOnce, true);
    assert.deepStrictEqual(calcStub.firstCall.args, ['SUM', 100, 20]);

    // Le console.log affiche le message attendu
    assert.strictEqual(consoleSpy.calledOnce, true);
    assert.strictEqual(consoleSpy.firstCall.args[0], 'The total is: 10');

    // Toujours restaurer
    calcStub.restore();
    consoleSpy.restore();
  });
});
