import java.awt.EventQueue;

import javax.swing.JFrame;
import javax.swing.JButton;
import java.awt.event.ActionListener;
import java.awt.event.ActionEvent;

public class Janela3 {

	private JFrame frmJanela;

	/**
	 * Launch the application.
	 */
	public static void main(String[] args) {
		EventQueue.invokeLater(new Runnable() {
			public void run() {
				try {
					Janela3 window = new Janela3();
					window.frmJanela.setVisible(true);
				} catch (Exception e) {
					e.printStackTrace();
				}
			}
		});
	}

	/**
	 * Create the application.
	 */
	public Janela3() {
		initialize();
		frmJanela.setVisible(true);
	}

	/**
	 * Initialize the contents of the frame.
	 */
	private void initialize() {
		frmJanela = new JFrame();
		frmJanela.setTitle("janela 3");
		frmJanela.setBounds(100, 100, 450, 300);
		frmJanela.setDefaultCloseOperation(JFrame.DISPOSE_ON_CLOSE);
		frmJanela.getContentPane().setLayout(null);
		
		JButton btnNewButton = new JButton("fechar");
		btnNewButton.addActionListener(new ActionListener() {
			public void actionPerformed(ActionEvent e) {
				frmJanela.dispose();
			}
		});
		btnNewButton.setBounds(157, 112, 89, 23);
		frmJanela.getContentPane().add(btnNewButton);
	}

}
