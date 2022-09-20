public class TesteEstacionamento {
    public static void main(String[] args) {
        Estacionamento e1 = new Estacionamento(10);
        e1.entrar("SPFC", 4);
        String[] placas = e1.mostrarPlacas();

        for(String placa : placas) {
            System.out.println(placa);
        }
    }
}
