import java.util.List;

public class AlunoFlex {
    String matricula;
	String nome;
    double[] notas_double;
	
	public AlunoFlex(String matricula, String nome, String... notas) {
		this.matricula = matricula;
		this.nome = nome;
		this.notas_double = new double[notas.length];
		double nota;
		
		for (int i = 0; i < notas.length; i++) {
			nota = Double.parseDouble(notas[i]);
			this.notas_double[i] = nota;
		}
		
	}
	
	public AlunoFlex() { }

	public double calcularMedia() {
        double soma = 0;

        for(int i = 0; i < this.notas_double.length; i++) {
            soma = soma + this.notas_double[i];
        }

		return soma / this.notas_double.length;
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
        String s = " matricula=" + matricula + " nome=" + nome;
        
        for(int i = 0; i < this.notas_double.length; i++) {
            s = s + String.format(" nota %d = %.2f", i + 1, this.notas_double[i]);
        }

        return s;
	}
	
}