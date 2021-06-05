const request = require('request');
const { expect } = require('chai');

describe('Integration Testing', () => {

  describe('GET /', () => {
    it('basic payment system correct status', (done) => {
      const options = { url: 'http://localhost:7865', method: 'GET', };
      request(options, function (error, response, body) {
        expect(response.statusCode).to.equal(200);
        expect(body).to.equal('Welcome to the payment system');
        done();
      });
    });
  });

  describe('GET /cart/123', () => {
    it('regex payment system correct success status', (done) => {
      const options = { url: 'http://localhost:7865/cart/123', method: 'GET', };
      request(options, function (error, response, body) {
        expect(response.statusCode).to.equal(200);
        expect(body).to.equal('Payment methods for cart 123');
        done();
      });
    });
  });

  describe('GET /cart/a23', () => {
    it('regex payment system correct failure status', (done) => {
      const options = { url: 'http://localhost:7865/cart/a23', method: 'GET', };
      request(options, function (error, response, body) {
        expect(response.statusCode).to.equal(404);
        done();
      });
    });
  });

});
