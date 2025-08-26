// 2-calcul_chai.test.js
const { expect } = require('chai');
const calculateNumber = require('./2-calcul_chai.js');

describe('calculateNumber(type, a, b)', () => {
  describe('SUM', () => {
    it('should sum rounded numbers', () => {
      expect(calculateNumber('SUM', 1.4, 4.5)).to.equal(6);   // 1 + 5
      expect(calculateNumber('SUM', 1.2, 3.2)).to.equal(4);   // 1 + 3
      expect(calculateNumber('SUM', -1.4, -3.6)).to.equal(-5); // -1 + -4
      expect(calculateNumber('SUM', -1.5, 2.5)).to.equal(2);  // -1 + 3
      expect(calculateNumber('SUM', 0, 0)).to.equal(0);
    });
  });

  describe('SUBTRACT', () => {
    it('should subtract rounded numbers', () => {
      expect(calculateNumber('SUBTRACT', 1.4, 4.5)).to.equal(-4); // 1 - 5
      expect(calculateNumber('SUBTRACT', 3.6, 1.2)).to.equal(3);  // 4 - 1
      expect(calculateNumber('SUBTRACT', -1.4, -3.6)).to.equal(3); // -1 - (-4)
      expect(calculateNumber('SUBTRACT', -1.5, 2.5)).to.equal(-4); // -1 - 3
      expect(calculateNumber('SUBTRACT', 0, 0)).to.equal(0);
    });
  });

  describe('DIVIDE', () => {
    it('should divide rounded numbers', () => {
      expect(calculateNumber('DIVIDE', 1.4, 4.5)).to.equal(0.2); // 1 / 5
      expect(calculateNumber('DIVIDE', 3.6, 1.2)).to.equal(4);   // 4 / 1
      expect(calculateNumber('DIVIDE', -3.6, 1.2)).to.equal(-4); // -4 / 1
      expect(calculateNumber('DIVIDE', -2.5, -2.5)).to.equal(1); // -3 / -3
    });

    it('should return "Error" when rounded divisor is 0', () => {
      expect(calculateNumber('DIVIDE', 1.4, 0)).to.equal('Error');   // 1 / 0
      expect(calculateNumber('DIVIDE', 1.4, 0.2)).to.equal('Error'); // 1 / 0 (0.2 -> 0)
      expect(calculateNumber('DIVIDE', 0, 0.4)).to.equal('Error');   // 0 / 0 (0.4 -> 0)
    });
  });

  describe('Invalid type (optional)', () => {
    it('should throw on invalid type', () => {
      expect(() => calculateNumber('MULTIPLY', 1, 2)).to.throw('Invalid type');
    });
  });
});
