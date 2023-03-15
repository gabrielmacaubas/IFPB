class Repositorio {
    constructor() {
        this._alunos = [];
        this._id = 0;
    }

    get alunos() {
        return this._alunos;
    }

    get id() {
        return this._id;
    }

    inserir(aluno) {
        this._alunos.push(aluno);
        this._id = this._id + 1;
    }

    remover(index) {
        this._alunos.splice(index, 1);
    }
}
