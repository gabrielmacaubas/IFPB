class AlunoRepositorio {
    private _alunos: Aluno[];

    constructor() {
        this._alunos = [];
    }

    inserir(aluno: Aluno) {
        this._alunos.push(aluno);
        return aluno;
    }

    remover(nome: string) {
        const indxRemocao: number = this._alunos.findIndex(aluno => aluno.nome === nome);
        this._alunos.splice(indxRemocao, 1);
    }

    listar() {
        return this._alunos;
    }

    buscarPorNome(nome: string) {
        return this._alunos.filter(aluno => aluno.nome === nome);
    }
}
