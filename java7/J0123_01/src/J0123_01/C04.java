package J0123_01;

public class C04 {
	
	// 메소드에 리턴이 없으면 void
	static void add(int a, int b) { // 클래스메소드
		System.out.println(a+b);
		
	}
	
	static void total(int a, int b, int c) { // 클래스메소드 - 객체선언없이, 클래스명, 메소드명으로 사용
		System.out.println(a+b+c); // 리턴이 없으면 void
	}
	
	public static void main(String[] args) {
		int a = 10; // 지역변수
		int b = 9;	
		int c = 5;
		
		//a,b를 보내서 평균값을 리턴받아 출력
		Method m = new Method(); // 객체선언
		double result = m.avg(a, b); // 인스턴스메소드 호출
		System.out.println(result);
		
		
		// a,b,c를 보내서 합계를 리턴해서 출력하시오.
		int result2 = m.total(a, b, c); // 인스턴스메소드 호출
		System.out.println(result2);
		
		// input() 호출해서 출력하시오.
		m.input();
		
		// input2() 호출해서 합의 값을 리턴받아 출력하시오.
		int result3 = m.input2();	// 합의 값을 리턴받음
		System.out.println(+result3);
		
		
		// 함수호출
		m.addSubMulti();
		
		// 2개 숫자를 입력받아 더하기, 빼기, 곱하기 값을 리턴받아 출력하는 메소드 호출
//		int[] result4 = m.addSubMulti2(a, b);
//		for(int i=0;i<result4.length;i++) {
//			System.out.println(result4[i]);
//		}
		
		// 함수호출 - 메개변수 보내서 받기
		int[] score = new int[3];
		m.addSubMulti3(score); // 메소드 호출
		for(int i=0;i<score.length;i++) {
			System.out.println(score[i]);
		}
		
		
		
		
		
		
		
		
		
		
		
		
//		C04.add(a,b); // 클래스명.메소드명
		

	}

}
