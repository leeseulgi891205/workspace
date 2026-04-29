package j0119_01;
import java.util.Scanner;

public class C02 {

	public static void main(String[] args) {
		// 변수 - byte, short, int, long, float, double, char, boolean, String
		// 변수 - boolean, char,(정수: byte, short, int, long), (실수: float, double), String
		// Scanner ->(Sturing) nextLine(),(int) nextInt(),(double) nextDouble()
		// netxBoolean(), nextInt(), nextLong(), nextDouble(), nextFloat()
		
		Scanner scanner = new Scanner(System.in);
		
		System.out.println("이름을 입력하세요.>>");
		String name = scanner.nextLine();     //next()사이띄움불가, nextLine()사이띄움가능
		System.out.println("이름 : "+name);
		
		
		
		
		
//		System.out.println("이름을 입력하세요.>>");
//		String name = scanner.nextLine();
//		System.out.println("실수를 입력하세요.>>");
//		double num = scanner.nextDouble();
//		
//		// 출력 소수점 3자리, 1자리까지 출력
//		System.out.printf("%s님의 실수는 %.1f입니다.",name, num);
		
//		System.out.println("안녕"+5.8);
//		System.out.print(3+5+"방가"+4+2+"\n");
//		System.out.printf("%s:%d","홍길동",15);
		
		
		
		
		
//		int a = 10;
//		int b = 3;
//		System.out.println(a/+(double)(b));
//		// 소수점 자리수 출력가능, 공백크기 지정가능, 공백 0 표시 가능
//		System.out.printf(".2f",(a/(double)(b)));

	}

}
