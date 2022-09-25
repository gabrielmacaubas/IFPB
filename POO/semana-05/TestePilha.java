public class TestePilha {
    public static void main(String[] args) throws Exception{
        try {
            Pilha p1 = new Pilha();
            p1.push("joao");
            p1.push("maria");
            p1.push("jose");
            String topo;
            topo = p1.top();
            System.out.println(topo);
            p1.pop();
            p1.pop();
            topo = p1.top();
            System.out.println(topo);  
        } catch (Exception e) {
            System.out.println(e.getMessage());
        }
        
    }
}
