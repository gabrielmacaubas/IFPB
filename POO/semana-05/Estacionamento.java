import java.util.ArrayList;
import java.util.List;

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
    
    public Object[] consultarVagasLivres() {
        ArrayList<Integer> vagasLivresAL = new ArrayList<>();

        for(int i = 0; i < this.placas.length; i++) {
            if(this.placas[i] == null) {
                vagasLivresAL.add(i + 1);
            }
        }

        Object[] vagasLivres = vagasLivresAL.toArray();
        return vagasLivres;
    }

    public String[] consultarGeral() {
        return this.placas;
    }
}