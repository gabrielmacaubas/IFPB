
public class Gato extends Animal {

	private double salto;

	public Gato(String nome, double peso, double salto) {
		super(nome, peso);
		this.salto = salto;
	}
	
	@Override
	public String emitirSom() {
		return "miauu";
	}
	
}
