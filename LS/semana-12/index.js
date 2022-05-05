const { sum, sumPromise, sumAsync } = require('./sum.js');

console.log(sum(1, 1));

// Promise - Fulfilled
console.log(sumPromise(1, 1));

sumPromise(1, 1).then((result) => console.log(result))

// Promise - Rejected
// Promise - pending
// Promise - chaining
// Async & Await
