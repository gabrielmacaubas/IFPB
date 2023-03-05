let r = new repositorio();

function mostrarAluno(nome, idade, id) {
    let p = document.createElement("p");
    p.innerText = `${nome} - ${idade}`;
    const b = document.createElement("button");
    b.innerText = "X";

    p.setAttribute("id", id);
    b.addEventListener('click', function(event){ removerAluno(event, id) });
    p.appendChild(b);
    document.body.append(p);
      
}

function inserirAluno() {
    const nome = document.querySelector('#fnome').value;
    const idade = parseInt(document.querySelector('#fidade').value);
    const id = r.alunos.length;
    const aluno = {
        nome: nome, 
        idade: idade,
        id: id
    };

    r.alunos.push(aluno);
    mostrarAluno(nome, idade, id);
}

function removerAluno(event, id) {
    const index = r.alunos.findIndex(aluno => aluno.id == id);
    r.alunos.splice(index, 1);
    event.target.parentElement.remove();
}

for(aluno of r.alunos) {
    mostrarAluno(aluno.nome, aluno.idade, aluno.id);
}
