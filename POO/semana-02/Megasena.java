import java.util.Arrays;
import java.util.Random;

public class Megasena {

	public static void main(String[] args) {
		int[] numeros = new int[6];
		Random sorteio = new Random();
		
		for (int i = 0; i < 6; i++) {
			boolean passou = false;
			int sorteado = sorteio.nextInt(60);
			
			while(!passou) {
				boolean repetiu = false;
				
				for (int n : numeros)
					if (sorteado == n) {
						repetiu = true;
					}
				
				if (repetiu) 
					sorteado = sorteio.nextInt(60);
				else 
					passou = true;
				
			}
			
			numeros[i] = sorteado;	
			
		}
		
		Arrays.sort(numeros);
		System.out.println(Arrays.toString(numeros));
		
	}
}