import { Component } from '@angular/core';
import { Aluno } from './shared/aluno';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent {
  titulo = 'Matrículas';
  alunos: Aluno[];
  aluno: Aluno;
  
  constructor() {
    this.alunos = [];
    this.aluno = new Aluno();
  }

  cadastrar(): void {
    this.alunos.push(this.aluno);
    this.aluno = new Aluno();
  }


}
