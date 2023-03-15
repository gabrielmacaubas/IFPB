class Aluno {
    constructor(nome, idade, id) {
        this._nome = nome;
        this._idade = idade;
        this._id = id;
    }

    get nome() {
        return this._nome;
    }

    get idade() {
        return this._idade;
    }

    get id() {
        return this._id;
    }

    set nome(nomeNovo) {
        this._nome = nomeNovo;
    } 

    set idade(idadeNovo) {
        this._idade = idadeNovo;
    }
}