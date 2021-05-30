const assert = require('assert');
const calculateNumber = require("./0-calcul.js");

describe('calculateNumber', function() {
  it('1st test for correct output should return 4', function() {
    assert.strictEqual(calculateNumber(1, 3), 4);
    });
  it('3rd test with rouding should return 5', function() {
    assert.strictEqual(calculateNumber(1.2, 3), 4);
    });
  it('2nd test with rouding should return 5', function() {
    assert.strictEqual(calculateNumber(1, 3.7), 5);
    });
  it('4th test with rouding should return 6', function() {
    assert.strictEqual(calculateNumber(1.5, 3.7), 6);
    });
});
