package j0119_01;
import java.util.Scanner;
public class C04 {

	public static void main(String[] args) {
		Scanner scanner = new Scanner(System.in);
		
		// 이름, 국어, 영어, 수학 점수를 입력받아 이름, 국어, 영어, 수학 점수, 총점, 평균을 출력하시오.
		// 홍길동,100,100,99,299,99.33
		
		System.out.print("이름을 입력하세요 >> ");
		String name = scanner.next();
		System.out.print("국어점수를 입력하세요 >> ");
		int kor = scanner.nextInt();
		System.out.print("영어점수를 입력하세요 >> ");
		int eng = scanner.nextInt();
		System.out.print("수학점수를 입력하세요 >> ");
		int math = scanner.nextInt();
		int sum = kor + eng + math;
		double avg = sum / 3.0;
		System.out.println("                 [학생성적프로그램]");
		System.out.println("이름\t국어\t영어\t수학\t총점\t평균");
		System.out.printf("%s\t%d\t%d\t%d\t%d\t%.2f\n", name, kor, eng, math, sum, avg);
		
		if (avg >= 90) {
			System.out.println("A학점");
		} else if (avg >= 80) {
			System.out.println("B학점");
		} else if (avg >= 70) {
			System.out.println("C학점");
		} else if (avg >= 60) {
			System.out.println("D학점");
		} else {
			System.out.println("F학점");
		}
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
//		System.out.print("숫자를 입력하세요 >> ");
//		int input = scanner.nextInt();
//		String result =(input%2==0)?"짝수":"홀수";
//		System.out.println(result);
		
		
		
		
//		double a = 0.1;
//		float b = 0.1f;
//		
//		String result = (a==b)?"a와 b는 같다.":"a와 b는 다르다.";
//		System.out.println(result);
//		
//		System.out.println((double)b);
//		
//		float c = (float)a;
//		System.out.println(c);
		
		
		
//		int a =10;
//		System.out.print(10*100/100);
		
		
		
		
		
		
//		System.out.println("소수점이 있는 숫자를 입력하세요 >> ");
//		double input = scanner.nextDouble();
//		
//		double result = Math.ceil(input * 100) / 100.0;
//		double result2 = Math.floor(input * 100) / 100.0;
//		double result3 = Math.round(input * 100) / 100.0;
//		
//		System.out.printf("%.2f, %.2f, %.2f \n" + result, result2, result3);
		
		
		
		
		
		
		
		//소수점 첫째자리 반올림 - 반올림: round(), 올림: ceil(), 내림: floor() - 메소드
//		System.out.println(Math.round(3.592)); //4
//		System.out.println(Math.ceil(5.12)); //6
//		System.out.println(Math.floor(6.99)); //6
		
		
		
		
//		System.out.print("숫자를 입력하세요 >> ");
//		double input = scanner.nextDouble(); // 예: 3.141592 입력
//		
//		// 핵심 공식! (소수점 2자리 절사)
//		// 1. 100을 곱해서 소수점을 뒤로 민다. (314.1592)
//		// 2. (int)로 강제로 바꿔서 소수점을 날린다. (314)
//		// 3. 다시 100.0으로 나눠서 소수점을 되돌린다. (3.14)
//		double result = (int)(input * 100) / 100.0;
//
//		System.out.println("결과: " + result);
		

	}

}
