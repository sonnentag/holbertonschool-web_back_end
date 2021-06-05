const Utils = {
  calculateNumber(type, a, b) {
    if (type === 'DIVIDE') {
      const divisor = Math.round(b)
      if (divisor === 0) {
        return 'Error';
      }
      return Math.round(a) / divisor;
    }
    if (type === 'SUBTRACT') {
      return Math.round(a) - Math.round(b);
    }
    return Math.round(a) + Math.round(b);
  }
};

module.exports = Utils;
