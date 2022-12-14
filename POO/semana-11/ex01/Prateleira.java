import java.util.ArrayList;

public class Prateleira {
	private int id;
	private int tamanho;
	private ArrayList<Produto> produtos = new ArrayList<>();
	
	public Prateleira(int id, int tamanho) {
		this.id = id;
		this.tamanho = tamanho;
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
