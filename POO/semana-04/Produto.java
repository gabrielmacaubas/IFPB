public class Produto {
    private String nome;
    private String estoque;
    private double preco;

    public Produto(String nome, String estoque, double preco) {
        this.nome = nome;
        this.estoque = estoque;
        this.preco = preco;
    }

    public String getNome() {
        return this.nome;
    }

    public String getEstoque() {
        return this.estoque;
    }

    public double getPreco() {
        return this.preco;
    }

    public void setNome(String nome) {
        this.nome = nome;
    }

    public void setEstoque(String estoque) {
        this.estoque = estoque;
    }

    public void setPreco(double preco) {
        this.preco = preco;
    }

    public String toString() {
        return " nome=" + nome +
               " Estoque=" + estoque +
               " Preço=" + preco;
    }
}