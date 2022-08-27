public class Retangulo {
	public int id;
	public double largura;
	public double comprimento;

	public Retangulo(int id, double largura, double comprimento) {
		super();
		this.id = id;
		this.largura = largura;
		this.comprimento = comprimento;
	}

	public Retangulo() { }
	
	public double calcularArea() {
		return largura * comprimento;
	}
	
	public void enquadrar() {
		double media = (largura + comprimento) / 2;
		largura = media;
		comprimento = media;
	}
	
	public boolean ehQuadrado() {
		if (largura == comprimento)
			return true;
		
		else
			return false;
	}
	
	public String toString() {
		return " id=" + id + 
			   " largura=" + largura +
			   " comprimento=" + comprimento;
	}
	
	public boolean ehEquivalente(Retangulo outro) {
		if (this.calcularArea() == outro.calcularArea())
			return true;
		else
			return false;
	}
}



















