const { sum, sumPromise, sumAsync } = require('./sum.js');

// console.log(sum(1, 1));

// Promise - Fulfilled
// console.log(sumPromise(2, 2));

// sumPromise(3, 3).then((result) => console.log(result));

// Promise - Rejected
// sumPromise(3, 'x')
//   .then((result) => console.log(result))
//   .catch((error) => console.log(error));

// Promise - pending
// console.log(sum(4, 4));
// sumPromise(5, 5).then((result) => console.log(result));
// console.log(sum(6, 6));

// Promise - chaining
sumPromise(3, 3)
  .then((result) => sumPromise(result, 1))
  .then((result) => console.log(result));

// Async & Await
sumAsync(4, 4);