public class TesteLoja {
    public static void main(String[] agrs) {
        Loja loja1 = new Loja(1, "rua das flores");//id, endereco
        loja1.adicionar(new Produto("arroz", 3.0) );
        loja1.adicionar(new Produto("feijao", 4.0));
        loja1.adicionar(new Produto("carne", 30.0));
        loja1.adicionar(new Produto("leite", 6.0));

        System.out.println("\n 1. Remover o feijao");
        Produto feijao = loja1.localizar("feijao");
        loja1.remover(feijao);

        System.out.println("\n 2. Media de preco dos produtos");
        System.out.println(loja1.obterPrecoMedio());//13.0

        System.out.println("\n 3. Alterar preco do leite para 5.0");
        Produto leite = loja1.localizar("leite");
        leite.setPreco(5.0);
        
        System.out.println(loja1);
    }
}
