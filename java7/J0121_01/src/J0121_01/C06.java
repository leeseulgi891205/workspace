package J0121_01;

import java.util.Scanner;
import javax.swing.JOptionPane;

public class C06 {

	public static void main(String[] args) {
		Scanner scanner = new Scanner(System.in);
		String num2 = JOptionPane.showInputDialog("숫자를 입력하세요.");
		System.out.println("입력 : "+num2);
		scanner.close();
	}

}