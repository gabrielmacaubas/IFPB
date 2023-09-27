package baralho;
// Fig. 7.11: DeckOfCardsTest.java
// Aplicativo de embaralhar e distribuir cartas.

public class DeckOfCardsTest
{
   // executa o aplicativo
   public static void main( String args[] )
   {
      DeckOfCards myDeckOfCards = new DeckOfCards();
      myDeckOfCards.shuffle();

      System.out.println( "---Baralho original---");
      System.out.println( myDeckOfCards);
      System.out.println( "Size: " + myDeckOfCards.size());
      System.out.println("endereço na memória: " + myDeckOfCards.hashCode());

      System.out.println( "---Baralho clone---");
      DeckOfCards myDeckOfCards2 = myDeckOfCards.clone();
      System.out.println( myDeckOfCards2);
      System.out.println( "Size: " + myDeckOfCards2.size());
      System.out.println("endereço na memória: " + myDeckOfCards2.hashCode());

   } // fim de main
} // fim da classe DeckOfCardsTest


