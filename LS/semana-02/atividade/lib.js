function area_do_circulo(raio){

    const pi = 3.141592653589793
    let area = pi * (raio**2)
    return `Dado o raio ${raio}, obtemos a área ${area}`
}

export default area_do_circulo