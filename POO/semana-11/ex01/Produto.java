public class Produto {
	private String nome;
	private double preco;
	private Prateleira prateleira;
	private Fabricante fabricante;
	
	public Produto(String nome, double preco) {
		this.nome = nome;
		this.preco = preco;
	}
	
	public Prateleira getPrateleira() {
		return this.prateleira;
	}
	
	public Fabricante getFabricante() {
		return this.fabricante;
	}
	
	public String getNome() {
		return this.nome;
	}
	
	public void setPrateleira(Prateleira prateleira) {
		this.prateleira = prateleira;
	}
	
	public void setFabricante(Fabricante fabricante) {
		this.fabricante = fabricante;
	}
}
