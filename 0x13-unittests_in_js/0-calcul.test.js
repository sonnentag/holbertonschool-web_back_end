const assert = require('assert');
const calculateNumber = require("./0-calcul.js");

describe('no rounding', function() {
  it('1st test for correct output should return 4', function() {
    assert.strictEqual(calculateNumber(1, 3), 4);
    });
});
describe('round first down', function() {
  it('2nd test with rouding should return 4', function() {
    assert.strictEqual(calculateNumber(1.2, 3), 4);
    });
});
describe('round first up', function() {
  it('3rd test with rouding should return 5', function() {
    assert.strictEqual(calculateNumber(1.6, 3), 5);
    });
});
describe('round second down', function() {
  it('4th test with rouding should return 4', function() {
    assert.strictEqual(calculateNumber(1, 3.4), 4);
    });
});
describe('round second up', function() {
  it('5th test with rouding should return 5', function() {
    assert.strictEqual(calculateNumber(1, 3.7), 5);
    });
});
describe('round both down', function() {
  it('6th test with rouding should return 4', function() {
    assert.strictEqual(calculateNumber(1.3, 3.2), 4);
    });
});
describe('round both up', function() {
  it('7th test with rouding should return 6', function() {
    assert.strictEqual(calculateNumber(1.5, 3.7), 6);
    });
});
describe('down up', function() {
  it('8th test with rouding should return 5', function() {
    assert.strictEqual(calculateNumber(1.3, 3.7), 5);
    });
});
describe('up down', function() {
  it('9th test with rouding should return 5', function() {
    assert.strictEqual(calculateNumber(1.5, 3.3), 5);
    });
});
