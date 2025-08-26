// 2-calcul_chai.js
function calculateNumber(type, a, b) {
  const A = Math.round(a);
  const B = Math.round(b);

  switch (type) {
    case 'SUM':
      return A + B;
    case 'SUBTRACT':
      return A - B;
    case 'DIVIDE':
      if (B === 0) return 'Error';
      return A / B;
    default:
      throw new Error('Invalid type');
  }
}

module.exports = calculateNumber;
