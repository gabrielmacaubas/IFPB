
public class TesteAluno {
	public static void main (String[] args) {
		Aluno a1 = new Aluno("2022237001", "joao", 10.0, 7.0);
		
		System.out.println(String.format("%,.2f", a1.calcularMedia()));
		System.out.println(a1.calcularSituacao());
		System.out.println(a1);
		
		Aluno a2 = new Aluno("2022237002", "maria", 6.0, 7.0);
		
		System.out.println(String.format("%,.2f", a2.calcularMedia()));
		System.out.println(a2.calcularSituacao());
		System.out.println(a2);
	}
}
