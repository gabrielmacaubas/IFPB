
public class Animal {
	public String nome;
	public double peso;
	
	public Animal(String nome, double peso) {
		super();
		this.nome = nome;
		this.peso = peso;
	}
	
	public String emitirSom() {
		return "nenhum som";
	}
	
	public String toString() {
		return " nome=" + nome +
			   ", peso=" + peso +
			   ". som=" + emitirSom();
	}
}
