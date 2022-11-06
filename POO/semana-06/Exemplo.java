import java.awt.EventQueue;

import javax.swing.JFrame;
import javax.swing.JLabel;
import javax.swing.JOptionPane;
import javax.swing.JTextField;
import javax.swing.JButton;
import java.awt.event.ActionListener;
import java.awt.event.ActionEvent;

public class Exemplo {

	private JFrame frame;
	private JLabel label;
	private JTextField textField;
	private JButton button;
	private JButton button_1;

	/**
	 * Launch the application.
	 */
	public static void main(String[] args) {
		EventQueue.invokeLater(new Runnable() {
			public void run() {
				try {
					Exemplo window = new Exemplo();
					
					window.frame.setVisible(true);
					
				} catch (Exception e) {
					e.printStackTrace();
				}
			}
		});
	}

	/**
	 * Create the application.
	 */
	public Exemplo() {
		initialize();
	}

	/**
	 * Initialize the contents of the frame.
	 */
	private void initialize() {
		frame = new JFrame();
		
		frame.setTitle("Primeira janela");
		frame.setBounds(100, 100, 450, 300);
		frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		frame.getContentPane().setLayout(null);
		
		label = new JLabel("Digite");
		
		label.setBounds(41, 47, 46, 14);
		frame.getContentPane().add(label);
		
		textField = new JTextField();
		
		textField.setBounds(97, 44, 86, 20);
		frame.getContentPane().add(textField);
		textField.setColumns(10);
		
		button = new JButton("ok");
		
		button.addActionListener(
				new ActionListener() {
					public void actionPerformed(ActionEvent e) {
						String mensagem = "vc escreveu: " + textField.getText() ;
						
						JOptionPane.showMessageDialog(null, mensagem);
					}
				}
				);	
		button.setBounds(212, 43, 89, 23);
		frame.getContentPane().add(button);
		
		button_1 = new JButton("Limpar");
		
		button_1.addActionListener(new ActionListener() {
			public void actionPerformed(ActionEvent e) {
				textField.setText("");
				textField.requestFocus();
			}
		});
		button_1.setBounds(212, 111, 89, 23);
		frame.getContentPane().add(button_1);
	}
}
