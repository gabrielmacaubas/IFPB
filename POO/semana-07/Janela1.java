import java.awt.EventQueue;

import javax.swing.JFrame;
import javax.swing.JButton;
import java.awt.event.ActionListener;
import java.awt.event.ActionEvent;
import javax.swing.JMenuBar;
import javax.swing.JMenu;
import javax.swing.JMenuItem;
import java.awt.event.MouseAdapter;
import java.awt.event.MouseEvent;

public class Janela1 {

	private JFrame frmJanela;

	/**
	 * Launch the application.
	 */
	public static void main(String[] args) {
		EventQueue.invokeLater(new Runnable() {
			public void run() {
				try {
					Janela1 window = new Janela1();
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
	public Janela1() {
		initialize();
	}

	/**
	 * Initialize the contents of the frame.
	 */
	private void initialize() {
		frmJanela = new JFrame();
		frmJanela.setTitle("janela 1");
		frmJanela.setBounds(100, 100, 450, 300);
		frmJanela.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		frmJanela.getContentPane().setLayout(null);
		
		JButton btnNewButton = new JButton("abrir janela 2");
		btnNewButton.addActionListener(new ActionListener() {
			public void actionPerformed(ActionEvent e) {
				Janela2 tela = new Janela2();
			}
		});
		btnNewButton.setBounds(60, 80, 303, 23);
		frmJanela.getContentPane().add(btnNewButton);
		
		JButton btnNewButton_1 = new JButton("abrir janela 3");
		btnNewButton_1.addActionListener(new ActionListener() {
			public void actionPerformed(ActionEvent e) {
				Janela3 tela = new Janela3();
			}
		});
		btnNewButton_1.setBounds(60, 139, 303, 23);
		frmJanela.getContentPane().add(btnNewButton_1);
		
		JMenuBar menuBar = new JMenuBar();
		frmJanela.setJMenuBar(menuBar);
		
		JMenu mnNewMenu = new JMenu("Exibir");
		menuBar.add(mnNewMenu);
		
		JMenuItem mntmNewMenuItem = new JMenuItem("segunda janela");
		mntmNewMenuItem.addActionListener(new ActionListener() {
			public void actionPerformed(ActionEvent e) {
				btnNewButton.doClick();
			}
		});
		mnNewMenu.add(mntmNewMenuItem);
		
		JMenuItem mntmNewMenuItem_1 = new JMenuItem("terceira janela");
		mntmNewMenuItem_1.addActionListener(new ActionListener() {
			public void actionPerformed(ActionEvent e) {
				btnNewButton_1.doClick();
			}
		});
		mnNewMenu.add(mntmNewMenuItem_1);
		
		JMenu mnNewMenu_1 = new JMenu("Sair");
		mnNewMenu_1.addMouseListener(new MouseAdapter() {
			@Override
			public void mouseClicked(MouseEvent e) {
				frmJanela.dispose();
			}
		});
		menuBar.add(mnNewMenu_1);
	}
}
