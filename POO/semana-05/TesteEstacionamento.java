import java.util.Arrays;

public class TesteEstacionamento {
    public static void main(String[] args) throws Exception {
        try {
            Estacionamento e1 = new Estacionamento(30);
            int[] vagasLivres = e1.consultarVagasLivres();

            System.out.println(Arrays.toString(vagasLivres));

            e1.lerDados();
            String[] vagas = e1.consultarGeral();
            System.out.println(Arrays.toString(vagas));
            System.out.println(e1.consultarPlaca("AAA1111"));
            System.out.println(e1.consultarPlaca("AAA2222"));
            System.out.println(e1.consultarPlaca("AAA3333"));

            e1.gravarDados();

            vagasLivres = e1.consultarVagasLivres();
            System.out.println(Arrays.toString(vagasLivres));


        } catch (Exception e) {
            System.out.println(e.getMessage());
        }
        
    }
}
