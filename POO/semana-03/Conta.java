public class Conta {
	public String numero;
	public String cpf;
	public double saldo;
	
	public Conta(String numero, String cpf) {
		this.numero = numero;
		this.cpf = cpf;
		this.saldo = 0;
	}
	public void creditar(double... lista) {
		for(double valor : lista)
			saldo = saldo + valor;
	}
	public void debitar(double valor) {
		saldo = saldo - valor;
	}
	public void transferir(double valor, Conta destino) {
		this.debitar(valor);
		destino.creditar(valor);
	}
	
	public boolean vazia() {
		if(saldo == 0)
			return true;
		else
			return false;
	}
}
