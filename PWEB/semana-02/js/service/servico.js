class Servico {
    constructor() {
        this._repositorioAluno = new Repositorio()
    }
    
    inserirNoRepositorio(nome, idade) {
        if (idade < 18) {
            return false;
        }

        const id = this._repositorioAluno.id;
        const aluno = new Aluno(nome, idade, id);
        this._repositorioAluno.inserir(aluno);

        return aluno;
    }

    removerNoRepositorio(id) {
        const index = this._repositorioAluno.alunos
        .findIndex(
            aluno => aluno.id == id
        );

        this._repositorioAluno.remover(index);
    }
}