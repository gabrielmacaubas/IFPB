public class TesteConta {
	public static void main (String[] args) {
		Conta conta1 = new Conta("101", "123456");
		conta1.creditar(300.0);
		conta1.debitar(200.0);
		conta1.debitar(100.0);
		System.out.println(conta1.vazia());
	}
}
