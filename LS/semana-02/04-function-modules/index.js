import { sum, sumLambda, sumArrow } from './lib/calc.js'
import { circleArea } from 'calcular_area'

console.log(sum(1, 2));
console.log(sum(1));
console.log(sum(1, 2, 3));

console.log(sumLambda(1, 2));

console.log(sumArrow(1, 2));

console.log(circleArea(10));
