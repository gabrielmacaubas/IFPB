public class Estacionamento {
    private String[] placas;

    public Estacionamento(int n) {
        this.placas = new String[n];
    }

    public void entrar(String placa, int vaga) {
        this.placas[vaga - 1] = placa;
    }

    /*public void sair(vaga) {
        this.placas[]
    }
    */

    public String[] mostrarPlacas() {
        return this.placas;
    }
}