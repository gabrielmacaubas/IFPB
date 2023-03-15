class DisciplinaServico {
    constructor() {
        this._repositorio = new DisciplinaRepositorio();
    }

    inserir(codigo, nome) {
        if(this.buscarPorCodigo(codigo).length > 0); {
           const disciplina = new Disciplina(codigo, nome);
           return this._repositorio.inserir(disciplina);
        }
        return undefined;
    }

    remover(codigo) {
        this.repositorio.remover(codigo);
    }

    listar() {
        return this.repositorio.listar();
    }

    buscarPorCodigo(codigo) {
        return this.repositorio.buscarPorCodigo(codigo);
    }
}