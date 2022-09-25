import java.io.File;
import java.io.FileWriter;
import java.io.IOException;
import java.nio.file.Path;
import java.nio.file.Paths;
import java.util.Scanner;

class CustomException extends Exception {
    public CustomException(String message)
    {
        super(message);
    }
}

public class Estacionamento {
    private String[] placas;
    public Path path;

    public Estacionamento(int n) throws Exception{
        this.placas = new String[n];
        this.path = Paths.get("placas.csv").toRealPath();
    }

    public void entrar(String placa, int vaga) throws Exception{
        if(this.placas[vaga -1] != null) {
            throw new CustomException("Vaga já ocupada.");
        }

        try {
            this.placas[vaga - 1] = placa;

        } catch (ArrayIndexOutOfBoundsException e) {
            throw new CustomException("Vaga inexistente.");
        }
    }

    public void sair(int vaga) throws Exception{
        try {
            this.placas[vaga - 1] = null;
        } catch (ArrayIndexOutOfBoundsException e) {
            throw new CustomException("Vaga inexistente.");
        }
    }

    
    public int consultarPlaca(String placa) {

        for(int i = 0; i < this.placas.length; i++) {
            if(this.placas[i] != null) {
                if(this.placas[i] == placa) {
                    return i + 1;
                }
                
            }
        }

        return -1;
    }

    public String consultarVaga(int vaga) throws Exception{
        try {
            return this.placas[vaga - 1];
    
        } catch (ArrayIndexOutOfBoundsException e) {
            throw new CustomException("Vaga inexistente.");
        }   

    }

    public void transferir(int vaga1, int vaga2) throws Exception{
        if(vaga1 >= 1 & vaga1 <= this.placas.length & vaga2 >= 1 & vaga2 <= this.placas.length) {
            this.placas[vaga2 - 1] = this.placas[vaga1 - 1];
            this.placas[vaga1 - 1] = null;
        }
        else {
            throw new CustomException("Vaga inexistente.");
        }
        
    }
    
    public int[] consultarVagasLivres() {
        int quant = 0;

        for(int i = 0; i < this.placas.length; i++) {
            if(this.placas[i] == null) {
                quant++;
            }
        }

        int[] vagasLivres = new int[quant];
        quant = 0;

        for(int i = 0; i < this.placas.length; i++) {
            if(this.placas[i] == null) {
                vagasLivres[quant] = i + 1;
                quant++;
            }
        }

        return vagasLivres;
    }

    public void lerDados() throws Exception {
        Scanner sc = new Scanner(new File(path.toString()));

        sc.next();

        while(sc.hasNext()) {
            String[] tokens = sc.next().split(";");
            this.entrar(tokens[1], Integer.parseInt(tokens[0]));
            
        }

        sc.close();
        
    }

    public void gravarDados() throws Exception {
        File file = new File(this.path.toString());

        try {
            FileWriter outputfile = new FileWriter(file, false);
            outputfile.append("vaga;placa");
            
            for(int i = 0; i < this.placas.length; i++) {
                if(this.placas[i] != null) {
                    String append = "\n" + (i + 1) + ";" + this.placas[i];
                    outputfile.append(append);
                }
            }

            outputfile.flush();
            outputfile.close();
        } 
        catch (IOException e) {
            e.printStackTrace();
        }
    }

    public String[] consultarGeral() {
        return this.placas;
    }
}