public class TesteTriangulo {
	public static void main (String[] args) {
		Triangulo t = new Triangulo();
		t.id = 1;
		t.base = 1;
		t.altura = 7;
		
		System.out.println(t.calcularArea());
		
		t.base = 3;
		t.altura = 4;
		
		System.out.println(t.calcularArea());
		System.out.println(t);
	}

}
