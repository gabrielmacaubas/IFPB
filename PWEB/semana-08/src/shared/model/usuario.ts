export class Usuario {
    nome: string | null;
    cpf: string | null;
    idade: number | null;

    constructor(fnome: string | null, fcpf: string | null, fidade: number | null) {
        this.nome = fnome;
        this.cpf = fcpf;
        this.idade = fidade;
    }
}
  