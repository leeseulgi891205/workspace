package j0116_01;

import java.util.Scanner;

public class C06 {

	public static void main(String[] args) {
		// Scanner
		// 타입크기순서 : byte<short,char<int<long<float<double<String
		
		int a = 5;
		int b = 0;
		++a;
		b = a;
		System.out.println("a: "+a);
		System.out.println("b: "+b);
		
		
		
		//3개의 숫자를 입력받아, 가장큰수를 출력하시오.
		// 삼항연산자를 2번쓰면 됩니다.
		// (a>b)?( (a>c)?a:c   ):(     );
		// (a>c)?a:c
		// 최대값 - 삼항식
		// 최소값 - 삼항식
		// (a+b+c)-최대값-최소값 = 중간값
		// 최대값,중간값,최소값
//		int a = 5;
//		int b = 10;
//		int c = 7;
//		int result = (a>b)?( (a>c)?a:c ):( (b>c)?b:c );  //최대값
//		int result3 = (a<b)?( (a<c)?a:c ):( (b<c)?b:c ); //최소값
//		int result2 = (a+b+c)-result-result3;            //중간값
//		System.out.printf("숫자높은순 : %d,%d,%d \n",result,result2,result3);
		
		
//		Scanner scanner = new Scanner(System.in);
////		int result = Math.max(5, 10, 7);
//		int result = Math.max(5, Math.max(10,7));
//		System.out.println(result);
		
//		System.out.println("숫자를 입력하세요.>> ");
//		int a = scanner.nextInt();
//		int b = scanner.nextInt();
//		int c = scanner.nextInt();
//		int result = (a>b)?( (a>c)?a:c ):( (b>c)?b:c );
//		System.out.println("최대값 : "+result);
		
		
		
		
		
		//대입연산자
//		int a = 10;
//		int b = 3;
//		
//		//삼항연산자   /*  */
//		System.out.println("숫자를 입력하세요.>> ");
//		a = scanner.nextInt();
//		String result = (a>0)?"0보다 큰수입니다.":"0보다 작은수입니다.";
//		System.out.println(result);
		
		
		
//		a = -5;
//		int result = (a>0)?a:-a;
//		System.out.println("절대값 : "+result);
		
		
		
//		System.out.println("두수를 입력하세요.>> ");
//		a = scanner.nextInt();
//		b = scanner.nextInt();
//		int result = (a>b)?a:b;
//		System.out.println("더 큰수 : "+result);
		
		//논리연산자 (a>5)&&(b<5), (a>11)||(b<5)
		
		//비교연산자
//		System.out.println(a>b);
//		System.out.println(a<b);
//		System.out.println(a==b);
//		System.out.println(a!=b);
//		System.out.println(a<>b);//안됨.
		
		//산술연산자
//		System.out.println(a+b);
//		System.out.println(a-b);
//		System.out.println(a*b);
//		System.out.println(a/b);
//		System.out.println(a%b); //나머지
		
		
		
		
		
		// 이름,국어,영어 -> 이름,합계,평균을 출력하시오.
//		Scanner scanner = new Scanner(System.in);
//		// 이름,국어,영어 입력받아서, 출력하시오.
//		System.out.println("이름을 입력하세요. >> ");
//		String name = scanner.next();
//		System.out.println("국어점수를 입력하세요.>> ");
//		int kor = scanner.nextInt();
//		System.out.println("영어점수를 입력하세요.>> ");
//		int eng = scanner.nextInt();
//		int total = kor+eng;
//		int avg = total/2;
//		double avg2 = total/(double)2;
//		double avg3 = total/2.0;
//		System.out.printf("이름:%s,합계:%d,평균:%.2f",name,total,avg3);
		
		
		
		
		
		
//		int a = 10;
//		int b = 3;
//		System.out.println(a+b);
//		System.out.println(a-b);
//		System.out.println(a*b);
//		System.out.println(a/(double)b); //3.33333 -> 정수타입/정수타입 = 정수타입 3
//		
//		boolean bol = true;
//		System.out.println(!bol);

		//		System.out.println(2.0*100);
//		int a = 1;
//		a += 1; // a=a+1
//		a++;    // 증감연산자 : a=a+1
//		a--;    // a=a-1
//		System.out.println(a);

	}

}
