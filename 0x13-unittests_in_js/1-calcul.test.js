const assert = require('assert');
const calculateNumber = require("./1-calcul.js");

describe('no rounding', function() {
  it('1st test for correct output should return 4', function() {
    assert.strictEqual(calculateNumber('SUM', 1, 3), 4);
    });
});
describe('round first down', function() {
  it('2nd test with rounding should return 4', function() {
    assert.strictEqual(calculateNumber('SUM', 1.2, 3), 4);
    });
});
describe('round first up', function() {
  it('3rd test with rounding should return 5', function() {
    assert.strictEqual(calculateNumber('SUM', 1.6, 3), 5);
    });
});
describe('round second down', function() {
  it('4th test with rounding should return 4', function() {
    assert.strictEqual(calculateNumber('SUM', 1, 3.4), 4);
    });
});
describe('round second up', function() {
  it('5th test with rounding should return 5', function() {
    assert.strictEqual(calculateNumber('SUM', 1, 3.7), 5);
    });
});
describe('round both down', function() {
  it('6th test with rounding should return 4', function() {
    assert.strictEqual(calculateNumber('SUM', 1.3, 3.2), 4);
    });
});
describe('round both up', function() {
  it('7th test with rounding should return 6', function() {
    assert.strictEqual(calculateNumber('SUM', 1.5, 3.7), 6);
    });
});
describe('down up', function() {
  it('8th test with rounding should return 5', function() {
    assert.strictEqual(calculateNumber('SUM', 1.3, 3.7), 5);
    });
});
describe('up down', function() {
  it('9th test with rounding should return 5', function() {
    assert.strictEqual(calculateNumber('SUM', 1.5, 3.3), 5);
    });
});

describe('no rounding', function() {
  it('1st test for correct output should return 4', function() {
    assert.strictEqual(calculateNumber('DIVIDE', 12, 3), 4);
    });
});
describe('round first down', function() {
  it('2nd test with rounding should return 4', function() {
    assert.strictEqual(calculateNumber('DIVIDE', 12.2, 3), 4);
    });
});
describe('round first up', function() {
  it('3rd test with rounding should return 5', function() {
    assert.strictEqual(calculateNumber('DIVIDE', 14.6, 3), 5);
    });
});
describe('round second down', function() {
  it('4th test with rounding should return 4', function() {
    assert.strictEqual(calculateNumber('DIVIDE', 12, 3.4), 4);
    });
});
describe('round second up', function() {
  it('5th test with rounding should return 5', function() {
    assert.strictEqual(calculateNumber('DIVIDE', 20, 3.7), 5);
    });
});
describe('round both down', function() {
  it('6th test with rounding should return 4', function() {
    assert.strictEqual(calculateNumber('DIVIDE', 12.3, 3.2), 4);
    });
});
describe('round both up', function() {
  it('7th test with rounding should return 6', function() {
    assert.strictEqual(calculateNumber('DIVIDE', 23.5, 3.7), 6);
    });
});
describe('down up', function() {
  it('8th test with rounding should return 5', function() {
    assert.strictEqual(calculateNumber('DIVIDE', 20.3, 3.7), 5);
    });
});
describe('up down', function() {
  it('9th test with rounding should return 5', function() {
    assert.strictEqual(calculateNumber('DIVIDE', 19.5, 4.3), 5);
    });
});
describe('division by 0 error', function() {
  it('10th division test by 0 should error', function() {
    assert.strictEqual(calculateNumber('DIVIDE', 4, 0), 'Error');
  });
});

describe('no rounding', function() {
  it('1st test for correct output should return 4', function() {
    assert.strictEqual(calculateNumber('SUBTRACT', 7, 3), 4);
    });
});

describe('round first down', function() {
  it('2nd test with rounding should return 4', function() {
    assert.strictEqual(calculateNumber('SUBTRACT', 7.2, 3), 4);
    });
});
describe('round first up', function() {
  it('3rd test with rounding should return 5', function() {
    assert.strictEqual(calculateNumber('SUBTRACT', 7.6, 3), 5);
    });
});
describe('round second down', function() {
  it('4th test with rounding should return 4', function() {
    assert.strictEqual(calculateNumber('SUBTRACT', 7, 3.4), 4);
    });
});
describe('round second up', function() {
  it('5th test with rounding should return 5', function() {
    assert.strictEqual(calculateNumber('SUBTRACT', 9, 3.7), 5);
    });
});
describe('round both down', function() {
  it('6th test with rounding should return 4', function() {
    assert.strictEqual(calculateNumber('SUBTRACT', 7.3, 3.2), 4);
    });
});
describe('round both up', function() {
  it('7th test with rounding should return 6', function() {
    assert.strictEqual(calculateNumber('SUBTRACT', 9.5, 3.7), 6);
    });
});
describe('down up', function() {
  it('8th test with rounding should return 5', function() {
    assert.strictEqual(calculateNumber('SUBTRACT', 9.3, 3.7), 5);
    });
});
describe('up down', function() {
  it('9th test with rounding should return 5', function() {
    assert.strictEqual(calculateNumber('SUBTRACT', 7.5, 3.3), 5);
    });
});
