public class TesteEstacionamento {
    public static void main(String[] args) {
        Estacionamento e1 = new Estacionamento(10);
        e1.entrar("SPFC", 10);
        e1.transferir(10, 3);

        String[] placas = e1.consultarGeral();

        /* 
        for(String placa : placas) {
            System.out.println(placa);
        }
*/

        e1.consultarVagasLivres();
    }
}
