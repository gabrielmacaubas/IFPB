import java.util.Scanner;

public class Eleicao {
    public static void main(String[] args) {
        String flag = "fim";
        Scanner teclado = new Scanner(System.in);
        String voto = teclado.nextLine();
        int joao = 0;
        int maria = 0;
        int nulo = 0;
        
        while(!voto.equals(flag)) {
            if(voto.equals("joao"))
                joao++;
            else
                if(voto.equals("maria"))
                    maria++;
                else
                    nulo++;
            
            voto = teclado.nextLine();
        }

        teclado.close();
        System.out.println(String.format("\n%d votos para joao", joao));
        System.out.println(String.format("%d votos para maria", maria));
        System.out.println(String.format("%d votos nulos", nulo));

        if(joao > maria)
            System.out.println("joao é vencedor");
        else
            if(maria > joao)
                System.out.println("maria é vencedor");
            else
                System.out.println("empate");
    }
}
