package j0119_01;

import java.util.Scanner;

public class C0119_04 {

	public static void main(String[] args) {
		Scanner scanner = new Scanner(System.in);
		
		// 이름,국어,영어,수학 입력받아 이름,국어,영어,수학,합계,평균을 출력하시오.
		// 홍길동,100,100,99,299,99.33 
		System.out.println("이름을 입력하세요.");
		String name = scanner.next();
		System.out.println("국어점수를 입력하세요.");
		int kor = scanner.nextInt();
		System.out.println("영어점수를 입력하세요.");
		int eng = scanner.nextInt();
		System.out.println("수학점수를 입력하세요.");
		int math = scanner.nextInt();
		int total = kor+eng+math;
		double avg = total/3.0;
		System.out.println("               [ 학생성적프로그램 ]");
		System.out.println("이름\t국어\t영어\t수학\t합계\t평균");
		System.out.println("---------------------------------------------------");
		System.out.printf("%s\t%d\t%d\t%d\t%d\t%.2f\n",name,kor,eng,math,total,avg);
		
		
		
		
//		System.out.println("숫자를 입력하세요.");
//		int input = scanner.nextInt();
//		String result = ((input%2)==0)?"짝수":"홀수";
//		System.out.println(result);
		
		
//		double a = 0.1;
//		float b = 0.1F;
//		
//		String result = (a==b)?"a와 b는 같다.":"a와 b는 다르다";
//		System.out.println(result);
//		
//		System.out.println((double)b);
//		
//		float c = (float)a;
//		System.out.println(c);
//		
		
//		int a = 10;
//		System.out.println(10*100/100);
		
		//0.1
//		System.out.println("소수점이 있는 숫자를 입력하세요>> ");
//		double input = scanner.nextDouble();
//		double result = Math.round(input*100)/100.0;
//		double result2 = Math.floor(input*100)/100.0;
//		double result3 = Math.ceil(input*100)/100.0;
//		System.out.printf("%.2f, %.2f, %.2f \n",result,result2,result3);
		
		// 소수점 3자리에서 반올림,올림,버림을 모두 해보시오.
		
		// 소수점 2자리에서 반올림을 하시오. 34.195 -> 34.2
		// round 소수점 첫째자리에서 반올림 341.95
//		double result = (int)(input*100)/100.0;
//		double result = Math.round(input*10)/10.0;
//		System.out.println(result);
		
		
		
		// 소수점첫째자리 - 반올림:round, 올림:ceil, 버림:floor
//		System.out.println(Math.round(3.592));
//		System.out.println(Math.ceil(5.12));
//		System.out.println(Math.floor(6.99));
		
		
		
		// 숫자를 입력받아 소수점 2자리에서 절사해서 출력하시오.
		// 3.141592 -> 3.14
		// 405.7931 -> 405.79
		
//		System.out.println("숫자를 입력하세요.");
//		double input = scanner.nextDouble();
//		// result = (int)(* 100) / 100
//		double result = (int)(input*100)/100.0;
//		System.out.println("결과값 : "+result);

	}

}
