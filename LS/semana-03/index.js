const numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9];
const numbersMatrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
];

//console.log(numbers[0]);
//console.log(numbersMatrix[2][2]);

numbers[9] = 10;
numbers[numbers.length] = 11;
numbers.push(12);
// numbers[8] = 90;
// console.log(numbers);

// console.log(numbersMatrix);

// numbers index (0) is 0
// ...
// numbers index (12) is 12
// for (let i = 0; i < numbers.length; i++) {
//   console.log(`numbers index (${i}) is ${numbers[i]}`);
// }

// for (const i in numbers) {
//    console.log(`numbers index (${i}) is ${numbers[i]}`);
// }

// for (const value of numbers) {
//    console.log(value);
// }

// const person = ['John Doe', 30];
// const name = person[0];
// const age = person[1];
const [name, age] = ['John Doe', 30];
console.log(age);

const person = ['John Doe', 30];
const student = [...person, 123];
// console.log(student);

const lengths = [10, 30, 15];

// f(x) = 2x
const doubleLengths = lengths.map((x) => x * 2);
console.log(lengths);
console.log(doubleLengths);

// const evenLengths = lengths.filter((x) => x % 2 === 0);
const evenLengths = lengths.filter((x) => ! (x & 1));
console.log(evenLengths);
