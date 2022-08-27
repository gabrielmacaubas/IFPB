public class Aluno {
	String matricula;
	String nome;
	double nota1;
	double nota2;
	
	public Aluno(String matricula, String nome, double nota1, double nota2) {
		this.matricula = matricula;
		this.nome = nome;
		this.nota1 = nota1;
		this.nota2 = nota2;
	}
	
	public Aluno() { }

	public double calcularMedia() {
		return (nota1 + nota2) / 2;
	}
	
	public String calcularSituacao() {
		double media = calcularMedia();
		
		if (media >= 7)
			return "aprovado";
		else if (media >= 4)
			return "reprovado";
		else
			return "final";
	}
	
	public String toString() {
		return " matricula=" + matricula +
			   " nome=" + nome +
			   " nota1=" + nota1 +
			   " nota2=" + nota2;
	}
	
}







