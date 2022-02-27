function area_do_circulo(raio){

    const pi = 3.141592653589793;
    let area = pi * (raio**2);
    return `Dado o raio ${raio}, obtemos a área ${area}`;
}

function calculadora(val1, val2, ope){

    let resultado = 0;
    switch (ope) {

        case "+":
            resultado = val1 + val2;
            break;

        case "-":
            resultado = val1 - val2;
            break;

        case "*":
            resultado = val1 * val2;
            break;

        case "/":
            resultado = val1 / val2;
            break;

        default:
            resultado = "Operação Inválida";
        
    }  
    if (resultado == "Operação Inválida"){

        return resultado;

    } else{

        return `${val1} ${ope} ${val2} = ${resultado}`;

    }
}

export { area_do_circulo, calculadora }