public class Casa {
    private Pessoa proprietario;
    private String endereco;
    private String bairro;
    private double precoVenda;
    
    public Casa(Pessoa proprietario, String endereco, String bairro, double precoVenda) {
        this.proprietario = proprietario;
        this.endereco = endereco;
        this.bairro = bairro;
        this.precoVenda = precoVenda;
    }

    public double getPreco() {
        return this.precoVenda;
    }
}
