const chai = require('chai');
const calculateNumber = require("./2-calcul_chai.js");

describe('no rounding', function() {
  it('1st test for correct output should return 4', function() {
    chai.expect(calculateNumber('SUM', 1, 3)).to.equal(4);
    });
});
describe('round first down', function() {
  it('2nd test with rounding should return 4', function() {
    chai.expect(calculateNumber('SUM', 1.2, 3)).to.equal(4);
    });
});
describe('round first up', function() {
  it('3rd test with rounding should return 5', function() {
    chai.expect(calculateNumber('SUM', 1.6, 3)).to.equal(5);
    });
});
describe('round second down', function() {
  it('4th test with rounding should return 4', function() {
    chai.expect(calculateNumber('SUM', 1, 3.4)).to.equal(4);
    });
});
describe('round second up', function() {
  it('5th test with rounding should return 5', function() {
    chai.expect(calculateNumber('SUM', 1, 3.7)).to.equal(5);
    });
});
describe('round both down', function() {
  it('6th test with rounding should return 4', function() {
    chai.expect(calculateNumber('SUM', 1.3, 3.2)).to.equal(4);
    });
});
describe('round both up', function() {
  it('7th test with rounding should return 6', function() {
    chai.expect(calculateNumber('SUM', 1.5, 3.7)).to.equal(6);
    });
});
describe('down up', function() {
  it('8th test with rounding should return 5', function() {
    chai.expect(calculateNumber('SUM', 1.3, 3.7)).to.equal(5);
    });
});
describe('up down', function() {
  it('9th test with rounding should return 5', function() {
    chai.expect(calculateNumber('SUM', 1.5, 3.3)).to.equal(5);
    });
});
