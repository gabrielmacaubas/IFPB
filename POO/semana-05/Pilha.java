import java.util.ArrayList;

class CustomException extends Exception {
    public CustomException(String mensagem) {
        super(mensagem);
    }
}

public class Pilha {
    private ArrayList<String> pilha;
    private String topo;

    public Pilha() {
        this.pilha = new ArrayList<>();
        this.topo = "VAZIO";
    }

    public void push(String dado) {
        this.pilha.add(dado);
        this.topo = this.pilha.get(this.pilha.size() - 1);
    }

    public String top() {
        return this.topo;
    }

    public void pop() throws Exception {
        try {
            this.pilha.remove(this.pilha.size() - 1);

            if(this.pilha.size() == 0) {
                this.topo = "VAZIO";
            }

            else {
                this.topo = this.pilha.get(this.pilha.size() - 1);
            }    

        } catch (ArrayIndexOutOfBoundsException e) {
            throw new CustomException("Erro: A pilha está vazia.");
        }
    }
}