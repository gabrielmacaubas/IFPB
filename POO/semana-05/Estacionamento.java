import java.io.File;
import java.util.Scanner;

public class Estacionamento {
    private String[] placas;

    public Estacionamento(int n) {
        this.placas = new String[n];
    }

    public void entrar(String placa, int vaga) {
        this.placas[vaga - 1] = placa;
    }

    public void sair(int vaga) {
        this.placas[vaga - 1] = null;
    }

    
    public int consultarPlaca(String placa) {
        for(int i = 0; i < this.placas.length; i++) {
            if(this.placas[i] == placa) {
                return i + 1;
            }
        }

        return -1;
    }

    public String consultarVaga(int vaga) {
        return this.placas[vaga - 1];
    }

    public void transferir(int vaga1, int vaga2) {
        this.placas[vaga2 - 1] = this.placas[vaga1 - 1];
        this.placas[vaga1 - 1] = null;
    }
    
    public int[] consultarVagasLivres() {
        int quant = 0;

        for(int i = 0; i < this.placas.length; i++) {
            if(this.placas[i] == null) {
                quant++;
            }
        }

        int[] vagasLivres = new int[quant];
        quant = 0;

        for(int i = 0; i < this.placas.length; i++) {
            if(this.placas[i] == null) {
                vagasLivres[quant] = i + 1;
                quant++;
            }
        }

        return vagasLivres;
    }

    public void lerDados() throws Exception {
        Scanner sc = new Scanner(new File("/home/macaubas/code/IFPB/POO/semana-05/placas.csv"));

        sc.next();

        while(sc.hasNext()) {
            String[] tokens = sc.next().split(";");
            this.entrar(tokens[1], Integer.parseInt(tokens[0]));
            
        }
        
    }

    public String[] consultarGeral() {
        return this.placas;
    }
}