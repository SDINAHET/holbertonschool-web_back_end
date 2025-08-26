// 5-payment.test.js
const assert = require('assert');
const sinon = require('sinon');
const sendPaymentRequestToApi = require('./5-payment');

describe('sendPaymentRequestToApi (hooks + single spy)', () => {
  let consoleSpy;

  beforeEach(() => {
    consoleSpy = sinon.spy(console, 'log');
  });

  afterEach(() => {
    consoleSpy.restore();
  });

  it('logs "The total is: 120" and is called once for (100, 20)', () => {
    sendPaymentRequestToApi(100, 20);
    assert.strictEqual(consoleSpy.calledOnce, true);
    assert.strictEqual(consoleSpy.firstCall.args[0], 'The total is: 120');
    assert.strictEqual(consoleSpy.callCount, 1);
  });

  it('logs "The total is: 20" and is called once for (10, 10)', () => {
    sendPaymentRequestToApi(10, 10);
    assert.strictEqual(consoleSpy.calledOnce, true);
    assert.strictEqual(consoleSpy.firstCall.args[0], 'The total is: 20');
    assert.strictEqual(consoleSpy.callCount, 1);
  });
});
