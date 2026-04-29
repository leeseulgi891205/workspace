package J0123_01;
import java.util.Scanner;
public class Amethod {
	
	// 3개의 input를 받아, num에 저장해서 출력하시오.
	void input(int[] num) {
		Scanner scanner = new Scanner(System.in);
		for(int i=0;i<num.length;i++) {
			System.out.println("숫자를 입력하세요.");
			num[i] = scanner.nextInt();
		}
	}

	public static void main(String[] args) {
		

	}

}
