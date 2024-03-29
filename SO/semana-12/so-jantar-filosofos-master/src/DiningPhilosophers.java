/**
 * Original: http://www.baeldung.com/java-dining-philoshophers
 * Pequenas alterações: Gustavo Wagner, gwmendes@trt13.jus.br
 * Criada em: 30/08/2017
 */

// public class DiningPhilosophers {

//     //V1 - Dará deadlock rapidamente, pois todos tentarão pegar o garfo da esquerda.
//     public static void main(String[] args) throws Exception {

//         Philosopher[] philosophers = new Philosopher[5];
//         Object[] forks = new Object[philosophers.length];

//         for (int i = 0; i < forks.length; i++) {
//             forks[i] = new Object();
//         }

//         for (int i = 0; i < philosophers.length; i++) {
//             Object leftFork = forks[i];
//             Object rightFork = forks[(i + 1) % forks.length];

//             philosophers[i] = new Philosopher(leftFork, rightFork);

//             Thread t
//                     = new Thread(philosophers[i], "Philosopher " + (i + 1));
//             t.start();
//         }
//     }

    //V2
    //TODO-2 Descomente o código abaixo e comente o main V1 acima
    /*
     * Com esse novo código, o último filósofo irá tentar pegar o garfo da direita, e não o da esquerda,
     * possibilitando assim que não ocorra uma espera circular, não causando deadlock (não fechará mais o círculo)
     */

    public static void main(String[] args) throws Exception {

        final Philosopher[] philosophers = new Philosopher[5];
        Object[] forks = new Object[philosophers.length];

        for (int i = 0; i < forks.length; i++) {
            forks[i] = new Object();
        }

        for (int i = 0; i < philosophers.length; i++) {
            Object leftFork = forks[i];
            Object rightFork = forks[(i + 1) % forks.length];

            if (i == philosophers.length - 1) {

                // The last philosopher picks up the right fork first
                philosophers[i] = new Philosopher(rightFork, leftFork);
            } else {
                philosophers[i] = new Philosopher(leftFork, rightFork);
            }

            Thread t
                    = new Thread(philosophers[i], "Philosopher " + (i + 1));
            t.start();
        }
    }
}