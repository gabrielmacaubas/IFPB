class AlunoControlador {
    alunoServico: AlunoServico;

    constructor() {
        this.alunoServico = new AlunoServico();
    }

    inserir() {
        const nomeAluno: string = (<HTMLInputElement>document.querySelector("#nome")).value;
        const idadeAluno: number = Number(
            (<HTMLInputElement>document.querySelector("#idade")).value
        );
        const aluno: Aluno | undefined = this.alunoServico.inserir(nomeAluno, idadeAluno);
        if (aluno) {
            this.mostrarAlunoNoHTML(nomeAluno, idadeAluno);
            alert('Aluno inserido com sucesso!');
        } else {
            alert('Aluno menor de idade não permitido!');
        }
    }

    mostrarAlunoNoHTML(nome: string, idade: number) {
        const elementoP: Element = document.createElement("p");
        elementoP.textContent = `${nome} - ${idade}`;

        const elementoBotaoApagar: Element = document.createElement("button");
        elementoBotaoApagar.textContent = "X";

        elementoBotaoApagar.addEventListener('click', (event) => {
                this.removerAlunoDaLista(nome);
                (<HTMLButtonElement>event.target).parentElement.remove();
            }
        );
        elementoP.appendChild(elementoBotaoApagar);
        document.body.appendChild(elementoP);
    }

    removerAlunoDaLista(nome: string) {
        this.alunoServico.remover(nome);
    }

}

//
//
//
// for (let aluno of alunos) {
//     // colocar no html nome - idade
//     mostrarAlunoNoHTML(aluno.nome, aluno.idade);
// }
//
// function inserirAluno() {
// }
//
//

