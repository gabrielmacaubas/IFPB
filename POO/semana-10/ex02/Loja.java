import java.util.ArrayList;

public class Loja {
    private int id;
    private ArrayList<Produto> produtos = new ArrayList<>();

    public Loja(int id, String endereco) {
        this.id = id;
    }   
    
    public void adicionar(Produto produto) {
        this.produtos.add(produto);
    }

    public Produto localizar(String nome) {
        for(Produto p : this.produtos) {
            if(p.getNome().equals(nome)) {
                return p;
            }
        }

        return null;
    }

    public void remover(Produto produto) {
        produtos.remove(produto);
    }

    public double obterPrecoMedio() {
        double soma = 0;

        for(Produto p : this.produtos) {
            soma = soma + p.getPreco();
        }

        return soma / this.produtos.size();
    }

    public String toString() {
        String produtosString = "";

        for(Produto p : this.produtos) {
            produtosString = produtosString + p.getNome() + ", " + p.getPreco() + ". ";
        }

        return produtosString;
    }
}
