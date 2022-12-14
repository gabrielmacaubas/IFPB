import java.util.ArrayList;

public class Telefone {
	private String ddd;
	private String numero;
	private ArrayList<Contato> contatos = new ArrayList<>();
	
	public Telefone(String ddd, String numero) {
		this.ddd = ddd;
		this.numero = numero;
	}
}
