import java.util.Scanner;

public class Citacao {
    public static void main(String[] args) {
        Scanner teclado = new Scanner(System.in);
        
        System.out.println("Digite o nome completo:");
        
        String s = teclado.nextLine().toUpperCase();

        teclado.close();

        String [] nome = s.split(" ");
        s = nome[nome.length -1 ] + ", ";

        for(int i = 0; i < nome.length-1; i++)
            s = s + nome[i] + " ";

        System.out.println(String.format("\nCitacao: \n%s", s));
    }
}
