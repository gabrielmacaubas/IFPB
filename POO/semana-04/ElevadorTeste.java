public class ElevadorTeste {
    public static void main(String[] args) {
        Elevador elevador = new Elevador(10);
        System.out.println(elevador.getAndarAtual());
        int[] andares;
        andares = elevador.irPara(5);
        for (int i=0; i<andares.length; i++)
            System.out.println("=>" + andares[i]);

        System.out.println(elevador.getAndarAtual());
        andares = elevador.irPara(8);
        for (int i=0; i<andares.length; i++)
            System.out.println("=>" + andares[i]);

        System.out.println(elevador.getAndarAtual());
        andares = elevador.irPara(6);
        for (int i=0; i<andares.length; i++)
            System.out.println("=>" + andares[i]);

        System.out.println(elevador.getAndarAtual());
    }
}