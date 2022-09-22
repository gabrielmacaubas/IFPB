public class TesteEstacionamento {
    public static void main(String[] args) throws Exception {
        Estacionamento e1 = new Estacionamento(10);

        /*
        int[] vagasLivres = e1.consultarVagasLivres();
        for(int vaga : vagasLivres) {
            System.out.println(vaga);
        }
        */

        e1.lerDados();
        e1.gravarDados();

        String[] placas = e1.consultarGeral();
        for(String placa : placas) {
            System.out.println(placa);
        }
    }
}
