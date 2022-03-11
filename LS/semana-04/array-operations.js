export function sum(numbers) {
    let result = 0;

    // for(let flag=0; flag < numbers.length; flag++) {
    //   result += numbers[flag]
    // }

    // array [1, 2, 3] 
    // values 1, 2, 3 for...of
    // indexes 0, 1, 2 for...of
    // for (const value of numbers) {
    //   result += numbers[flag];
    // }

    // return result;
    
    // [3, 2, 1]
    // f(x, y) = x + y
    // | loop | y | x | f(x, y) |
    // |  1   | 3 | 0 |    1    |
    // |  2   | 2 | 3 |    5    |
    // |  3   | 1 | 5 |    6    |
    // return numbers.reduce((x, y) => x + y, 0);

    // f(x, y) = x + y
    // | loop | y | x | f(x, y) |
    // |  1   | 2 | 3 |    5    |
    // |  2   | 1 | 5 |    6    |
    // return numbers.reduce((x, y) => x + y);
    return numbers.reduce((acc, number) => acc + number, 0);
}

export function sumOdds(numbers) {
    // const result = 0;

    // for (const value of numbers) {
    //     if (value & 1)  { // value % 2 === 1
    //         result += value;
    //     }
    // }

    // return result;

    // return numbers
    //   .filter((x) => x & 1)
    //  .reduce((x, y) => x + y);

    // return numbers
    //   .reduce((x, y) => y & 1 ? x + y: 0, 0);
}

// Array.prototype.myReduce = function (callback, initialValue) {
//     let x = initialValue;
    
//    for (const y of this) {
//         x = callback(x, y);
//     }

//     return x;
// }

// const array = [3, 2, 1];
// const result = array.myReduce((x, y) => x +y, 0)
// console.log(result);

// [1, 2, 3].map((x) => x * 2)
// [1, 2, 3].filter((x) => x % 2 === 0)
// [1, 2, 3].reduce((x, y) => x * y, 1);
