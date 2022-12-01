public class TestePessoa {
    public static void main(String[] args) {
        Pessoa joao = new Pessoa("joao da silva", "123.000.555-88");
        //nome cpf
        Pessoa maria = new Pessoa("maria de souza", "222.101.666-32");
        //nome cpf

        Casa mansao = new Casa(joao, "rua primeiro de maio, 45",
        "jaguaribe", 800000.0); //proprietario, endereco, bairro, preco

        Aluguel aluguel1 = new Aluguel(mansao, maria);//imovel, inquilino
        double valor = aluguel1.getValorAluguel();  //0.003 x preco

        System.out.println(valor);//2400.0 = 0.003*800000.0
    }
}
