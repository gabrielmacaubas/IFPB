public class Matricula {
    private String ano;
    private String periodo;
    private String codigoCurso;
    private String sequencia;

    public Matricula(String matricula) {
        this.ano = matricula.substring(0, 4);
        this.periodo = matricula.substring(4, 5);
        this.codigoCurso = matricula.substring(5, 7);
        this.sequencia = matricula.substring(7, 11);
    }

    public String getAno() {
        return this.ano;
    }

    public String getPeriodo() {
        return this.periodo;
    }

    public String getCodigoCurso() {
        return this.codigoCurso;
    }

    public String getSequencia() {
        return this.sequencia;
    }
}