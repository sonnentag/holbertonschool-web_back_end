const sinon = require('sinon');
const { expect } = require('chai');

const sendPaymentRequestToApi = require('./4-payment.js');
const Utils = require('./utils.js');

describe('payment test using stubs', function () {
  it('same math used', () => {
    const stubUtils = sinon.stub(Utils, 'calculateNumber');
    const spyConsole = sinon.spy(console, 'log');
    stubUtils.returns(10);

    sendPaymentRequestToApi(100, 20);

    expect(stubUtils.calledOnceWithExactly('SUM', 100, 20)).to.be.true;
    expect(spyConsole.calledOnceWithExactly('The total is: 10')).to.be.true;

    stubUtils.restore();
    spyConsole.restore();
  });
});
