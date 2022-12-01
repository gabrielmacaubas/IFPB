public class Aluguel {
    private Casa imovel;
    private Pessoa inquilino;
    
    public Aluguel(Casa imovel, Pessoa inquilino) {
        this.imovel = imovel;
        this.inquilino = inquilino;
    }

    public double getValorAluguel() {
        return 0.003 * this.imovel.getPreco();
    }
}