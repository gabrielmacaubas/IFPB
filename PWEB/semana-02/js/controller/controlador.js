class Controlador {
    constructor() {
        this._servicoAluno = new Servico();
    }

    mostrarAluno(aluno) {
        let p = document.createElement("p");
        p.innerText = `${aluno.nome} - ${aluno.idade}`;
        const b = document.createElement("button");
        b.innerText = "X";
    
        p.setAttribute("id", aluno.id);
        b.addEventListener('click', function(event) {
            controladorAluno.removerAluno(event)
        });
        p.appendChild(b);
        document.body.append(p);
    }

    inserirAluno() {
        const idade = Number(
            document.querySelector('#fidade').value
        );
        const nome = document.querySelector('#fnome').value;
        const aluno = this._servicoAluno
        .inserirNoRepositorio(nome, idade);
        
        if (aluno) {
            this.mostrarAluno(aluno);
            alert("Aluno inserido com sucesso!");          
        }
        else {
            alert("Aluno menor de idade não permitido!");    
        }  
    }

    removerAluno(event) {
        this._servicoAluno.removerNoRepositorio(
            event.target.parentElement.id
        );
        event.target.parentElement.remove();
    }
    
}