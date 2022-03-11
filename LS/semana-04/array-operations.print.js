import { sum, sumOdds } from './array-operations.js';

// SUM
// sum  (1, 2, 3) 6
console.log(sum[1, 2, 3]);
// sum  (2, 2, 2) 6
console.log(sum([2, 2, 2]));
// sum (1, 2, 3, 4, 5, 6) 21
console.log(sum([1, 2, 3, 4, 5, 6]));

// SUM ODDS
// sumOdds (1, 2, 3) 4
console.log(sumOdds([1, 2, 3]));
// sumOdds (2, 2, 2) 0
console.log(sumOdds[2, 2, 2]);
// sumOdds (1, 2, 3, 4, 5, 6) 9
console.log(sumOdds([1, 2, 3, 4, 5, 6]));
