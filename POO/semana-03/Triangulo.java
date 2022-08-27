public class Triangulo {
	public int id;
	public double base;
	public double altura;
	
	public Triangulo(int id, double base, double altura) {
		this.id = id;
		this.base = base;
		this.altura = altura;
	}
	
	public Triangulo() { }
	
	public double calcularArea() {
		return (base * altura) / 2;
	}
	
	public String toString() {
		return " id=" + id +
			   " base =" + base +
			   " altura=" + altura;
	}
}
