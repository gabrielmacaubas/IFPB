public class Teste {
	public static void main (String[] args) {
		/* TESTE 1 */
		Retangulo r = new Retangulo();
		r.id = 1;
		r.largura = 1;
		r.comprimento = 7;
		System.out.println(r.calcularArea());
		r.largura = 3;
		r.comprimento = 4;
		System.out.println(r.calcularArea());
		
		/* TESTE 2*/
		Retangulo r1 = new Retangulo(1, 3, 4);
		System.out.println(r1.calcularArea());
		
		Retangulo r2 = new Retangulo();
		System.out.println(r2.calcularArea());
		
		/* TESTE 3*/
		r = new Retangulo(1, 3, 5);
		System.out.println(r.calcularArea());
		r.enquadrar();
		System.out.println(r.calcularArea());
		
		/* TESTE 4*/
		r = new Retangulo(1, 3, 3);
		System.out.println(r.ehQuadrado());
		r = new Retangulo(2, 2, 7);
		System.out.println(r.ehQuadrado());
		
		/* TESTE 5 */
		r = new Retangulo(1, 3, 5);
		System.out.println(r);
		
		/* TESTE 6 */
		r1 = new Retangulo(1, 3, 3);
		r2 = new Retangulo(2, 2, 4.5);
		System.out.println(r1.ehEquivalente(r2));
		System.out.println(r2.ehEquivalente(r1));
	}
}












