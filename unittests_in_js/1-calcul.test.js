// 1-calcul.test.js
const assert = require('assert');
const calculateNumber = require('./1-calcul.js');

describe('calculateNumber(type, a, b)', () => {
  describe('SUM', () => {
    it('should sum rounded numbers', () => {
      assert.strictEqual(calculateNumber('SUM', 1.4, 4.5), 6); // 1 + 5
      assert.strictEqual(calculateNumber('SUM', 1.2, 3.2), 4); // 1 + 3
      assert.strictEqual(calculateNumber('SUM', -1.4, -3.6), -5); // -1 + -4
      assert.strictEqual(calculateNumber('SUM', -1.5, 2.5), 2); // -1 + 3
      assert.strictEqual(calculateNumber('SUM', 0, 0), 0);
    });
  });

  describe('SUBTRACT', () => {
    it('should subtract rounded numbers', () => {
      assert.strictEqual(calculateNumber('SUBTRACT', 1.4, 4.5), -4); // 1 - 5
      assert.strictEqual(calculateNumber('SUBTRACT', 3.6, 1.2), 3);  // 4 - 1
      assert.strictEqual(calculateNumber('SUBTRACT', -1.4, -3.6), 3); // -1 - (-4)
      assert.strictEqual(calculateNumber('SUBTRACT', -1.5, 2.5), -4); // -1 - 3
      assert.strictEqual(calculateNumber('SUBTRACT', 0, 0), 0);
    });
  });

  describe('DIVIDE', () => {
    it('should divide rounded numbers', () => {
      assert.strictEqual(calculateNumber('DIVIDE', 1.4, 4.5), 0.2); // 1 / 5
      assert.strictEqual(calculateNumber('DIVIDE', 3.6, 1.2), 4);   // 4 / 1
      assert.strictEqual(calculateNumber('DIVIDE', -3.6, 1.2), -4); // -4 / 1
      assert.strictEqual(calculateNumber('DIVIDE', -2.5, -2.5), 1); // -3 / -3
    });

    it('should return "Error" when rounded divisor is 0', () => {
      assert.strictEqual(calculateNumber('DIVIDE', 1.4, 0), 'Error');   // 1 / 0
      assert.strictEqual(calculateNumber('DIVIDE', 1.4, 0.2), 'Error'); // 1 / 0 (0.2 -> 0)
      assert.strictEqual(calculateNumber('DIVIDE', 0, 0.4), 'Error');   // 0 / 0 (0.4 -> 0)
    });
  });

  describe('Invalid type (optional)', () => {
    it('should throw on invalid type', () => {
      assert.throws(() => calculateNumber('MULTIPLY', 1, 2), /Invalid type/);
    });
  });
});
