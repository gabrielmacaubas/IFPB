public class TesteAlunoFlex {
    public static void main (String[] args) {
        AlunoFlex a1 = new AlunoFlex("123456", "gabriel", "10.0", "7.0", "8.0");

        AlunoFlex a2 = new AlunoFlex("123457", "Flávio", "10", "7", "5");
        
        System.out.println();
        System.out.println(a1);
        System.out.println(String.format("Média do aluno: %s", a1.calcularMedia()));
        
        // Printa resultado
        System.out.println(a2);
    }
    
}