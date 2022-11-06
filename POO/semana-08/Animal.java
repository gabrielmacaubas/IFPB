
public class Animal {

	private String nome;
	private double peso;
	
	public Animal(String nome, double peso) {
		super();
		this.nome = nome;
		this.peso = peso;
	}
	
	public String getNome() {
		return this.nome;
	}
	
	public String emitirSom() {
		return "nenhum som";
	}

	@Override
	public String toString() {
		return "Animal [nome=" + nome + 
				", peso=" + peso + 
				", emitirSom()=" + emitirSom() + "]";
	}
	
	
}
