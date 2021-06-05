const express = require('express');
const app = express();

app.get('/', (request, result) => {
  result.end('Welcome to the payment system');
});
app.get('/cart/:id[0-9]+', (request, result) => {
  result.end('Payment methods for cart '`${request.params.id}`);
});
app.listen(7865, () => {
  console.log('API available on localhost port 7865');
});
