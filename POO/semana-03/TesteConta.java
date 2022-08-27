public class TesteConta {
	public static void main (String[] args) {
		Conta conta1 = new Conta("333", "123456");
		conta1.creditar(300.0);
		Conta conta2 = conta1.clonar();

        System.out.println(conta1);
        System.out.println(conta2);
	}
}
