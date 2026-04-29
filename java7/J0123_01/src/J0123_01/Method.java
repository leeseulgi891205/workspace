package J0123_01;
import java.util.Scanner;

public class Method {
	static Scanner scanner = new Scanner(System.in);
	
	//avg()
	double avg(int a, int b) {
		scanner.next();
		double result = (a+b)/2.0;
		return result;
	}
	
	//total()
	int total(int a, int b, int c) {
		int result = a+b+c;
		return result;
	}
	
	// input() 리턴없이 2개의 값을 입력받아, 합을 출력하는 메소드
	
	void input() {
		System.out.println("첫번째");	
		int a3 = scanner.nextInt();	
		System.out.println("두번째");
		int b3 = scanner.nextInt();
		int sum = a3+b3;
		System.out.println("합계:"+sum);
	}
	
		//input2() 합의 값을 리턴해줌.
	int input2() {// 리턴 타입이 int 이므로, 마지막에 반드시 정수값을 return 해줘야함
		System.out.println("숫자를 입력하세요."); // 사용자에게 안내 메세지 출력
		int a4 = scanner.nextInt();	// 키보드로 입력받은 첫 번째 정수를 변수 a4에 저장
		System.out.println("숫자를 입력하세요.");
		int b4 = scanner.nextInt();
		int sum2 = a4+b4;
		return sum2;// 계산된 합계(sum2)를 이 메서드를 호출한 곳으로 되돌려줌
		
	}
	
		//2개 숫자를 입력받아, 더하기, 빼기, 곱하기 값을 리턴 1개만 리턴 가능
		//1. 리턴없이 2개 숫자를 입력받아 더하기, 빼기, 곱하기 값을 출력하는 메소드 구현.
	void addSubMulti() {// 리턴타입 void - 리턴값이 없음
		System.out.println("첫번째 숫자를 입력하세요.>>");
		int a = scanner.nextInt();
		System.out.println("두번째 숫자를 입력하세요.>>");
		int b = scanner.nextInt();
		int add = a+b;
		int sub = a=b;
		int multi = a*b;
		System.out.println("더하기:"+add);
		System.out.println("빼기:"+sub);
		System.out.println("곱하기:"+multi);
		
	}
		//1. 리턴을 받아서 2개 숫자를 입력받아 더하기, 빼기, 곱하기 값을 출력하는 메소드 구현.
	int[] addSubMulti2(int a, int b) {
		int[] result = new int[3];
		System.out.println("첫번째 숫자를 입력하세요.>>");
		int a1 = scanner.nextInt();
		System.out.println("두번째 숫자를 입력하세요.>>");
		int b1 = scanner.nextInt();
		int add = a+b;
		int sub = a-b;
		int multi = a*b;
		System.out.println("더하기:"+add);
		System.out.println("빼기:"+sub);
		System.out.println("곱하기:"+multi);
		result[0] = add;
		result[1] = sub;
		result[2] = multi;
		return result;// 더하기 값만 리턴
		
	}
	
	// 배열,객체를 매개변수로 보낼시 리턴이 필요없음
	// 기본타입 8가지 -> 리턴을 받아야 함.
	void addSubMulti3(int[] result4) {
		System.out.println("첫번째 숫자를 입력하세요.>>");
		int a1 = scanner.nextInt();
		System.out.println("두번째 숫자를 입력하세요.>>");
		int b1 = scanner.nextInt();
		result4[0] = (a1+b1);
		result4[1] = (a1-b1);
		result4[2] = (a1*b1);
		
	}
		
		
		
	
	
	
	
	
	
}
