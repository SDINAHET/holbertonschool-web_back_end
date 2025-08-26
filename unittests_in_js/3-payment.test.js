// 3-payment.test.js
const assert = require('assert');
const sinon = require('sinon');
const Utils = require('./utils');
const sendPaymentRequestToApi = require('./3-payment');

describe('sendPaymentRequestToApi', () => {
  it('should use Utils.calculateNumber("SUM", 100, 20) and log the total', () => {
    const calcSpy = sinon.spy(Utils, 'calculateNumber');
    const consoleSpy = sinon.spy(console, 'log');

    sendPaymentRequestToApi(100, 20);

    // Le spy a bien été appelé une seule fois avec les bons arguments
    assert.strictEqual(calcSpy.calledOnce, true);
    assert.deepStrictEqual(calcSpy.firstCall.args, ['SUM', 100, 20]);

    // Le message affiché correspond au résultat (100 + 20 = 120)
    assert.strictEqual(consoleSpy.calledWith('The total is: 120'), true);

    // Toujours restaurer les spies
    calcSpy.restore();
    consoleSpy.restore();
  });
});
