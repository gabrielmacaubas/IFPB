public class Calculadora {
    private Calculadora() {}

    public static String historico = "";

    public static String historico() {
        return historico;
    }

    public static int somar(int a, int b) {
        int resultado = a + b;
        historico = historico + "\n" + a + " + " + b + " = " + resultado;

        return resultado;
    }

    public static int subtrair(int a, int b) {
        int resultado = a - b;
        historico = historico + "\n" + a + " - " + b + " = " + resultado;

        return a - b;
    }

    public static int multiplicar(int a, int b) {
        int resultado = a * b;
        historico = historico + "\n" + a + " * " + b + " = " + resultado;

        return a * b;
    }

    public static int dividir(int a, int b) {
        int resultado = a / b;
        historico = historico + "\n" + a + " / " + b + " = " + resultado;

        return a / b;
    }
}