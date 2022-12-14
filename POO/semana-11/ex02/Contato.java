import java.util.ArrayList;

public class Contato {
	private String nome;
	private String logradouro;
	private ArrayList<Telefone> telefones = new ArrayList<>();
	
	public Contato(String nome, String logradouro) {
		this.nome = nome;
		this.logradouro = logradouro;
	}
}
