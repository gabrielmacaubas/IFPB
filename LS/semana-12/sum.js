function sum(a, b) {
  return a + b
}

// Promise
function sumPromise(a, b) {
  const promise = new Promise((resolve, reject) => {
    if (isNaN(a) || isNaN(b)) reject('Invalid numbers')
    else setTimeout(() => resolve(a + b), 200);
  })

  return promise;
}

// Async & Await
async function sumAsync(a, b) {
  const result = await sumPromise(a, b);
  return result;
}

module.exports = { sum, sumPromise, sumAsync };
