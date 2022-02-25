function sum(a, b = 1) {
    return a + b;
}

const sumLambda = function (a, b) { 
    return a + b 
};

const sumArrow = (a, b) => a + b;

export { sum, sumLambda, sumArrow };