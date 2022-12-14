import java.util.ArrayList;

public class Fabricante {
	private String nome;
	private ArrayList<Produto> produtos = new ArrayList<>();
	
	public Fabricante(String nome) {
		this.nome = nome;
	}
	
	public void adicionar(Produto p) {
		this.produtos.add(p);
	}
	
	public void remover(Produto p) {
		this.produtos.remove(p);
	}
	
	public Produto localizar(String nome) {
		for(Produto p : this.produtos) {
			if(p.getNome().equals(nome)) {
				return p;
			}
		}
		
		return null;
	}
}
