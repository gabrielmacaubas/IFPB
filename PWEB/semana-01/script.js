const alunos = [
    {
        nome: "Gustavo",
        idade: 30,
        id: 0
    },
    {
        nome: "Wagner",
        idade: 20,
        id: 1
    },
    {
        nome: "Diniz",
        idade: 17,
        id: 2
    }
];

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
    const id = alunos.length;
    const aluno = {
        nome: nome, 
        idade: idade,
        id: id
    };

    alunos.push(aluno);
    mostrarAluno(nome, idade, id);
}

function removerAluno(event, id) {
    const index = alunos.findIndex(aluno => aluno.id == id);
    alunos.splice(index, 1);
    event.target.parentElement.remove();
}

for(aluno of alunos) {
    mostrarAluno(aluno.nome, aluno.idade, aluno.id);
}

