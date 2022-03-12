function sum(numbers) {
    return numbers.reduce((addition, value) => addition + value, 0);
}

function sumOdds(numbers) {
    return sum(numbers.filter((value) => value % 2 !== 0));
}

function product(numbers) {
    return numbers.reduce((addition, value) => addition * value, 1);
}

export { sum, sumOdds, product }