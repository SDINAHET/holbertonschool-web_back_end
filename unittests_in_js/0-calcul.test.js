const assert = require('assert');
const calculateNumber = require('./0-calcul');

describe('calculateNumber', () => {
  it('should return 4 when adding 1 and 3', () => {
    assert.strictEqual(calculateNumber(1, 3), 4);
  });

  it('should round second argument', () => {
    assert.strictEqual(calculateNumber(1, 3.7), 5);
  });

  it('should round both arguments down', () => {
    assert.strictEqual(calculateNumber(1.2, 3.7), 5);
  });

  it('should round first argument up', () => {
    assert.strictEqual(calculateNumber(1.5, 3.7), 6);
  });

  it('should round both arguments correctly when .5 case', () => {
    assert.strictEqual(calculateNumber(2.5, 2.5), 6); // rounds both up
  });

  it('should handle negative numbers', () => {
    assert.strictEqual(calculateNumber(-1.2, -3.7), -5);
  });

  it('should handle mix of positive and negative', () => {
    assert.strictEqual(calculateNumber(-1.5, 2.4), 1);
  });
});
