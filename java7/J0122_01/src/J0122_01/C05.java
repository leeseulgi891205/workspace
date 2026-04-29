package J0122_01;

public class C05 {
	
	int aa = 0; // 인스턴스 변수 - 객체 생성 후 사용 가능
	static int bb = 0; // 클래스 변수 - static 메서드 내에서 사용 불가
	
	int add(int a,int b) { // 인스턴스 메서드 - 객체 생성 후 사용 가능
		System.out.println("합:"+(a+b));
		return a+b;
		
	}
	
	static int[] addSub(int a,int b) { // 클래스 메서드 - 객체 생성 없이 사용 가능
		int result = a + b;
		int result2 = a - b;
		return new int[] {result, result2}; // 배열로 리턴s
//		int[] arr = {result, result2};
//		return arr; // 배열로 리턴
	}
	
	static int add2(int a,int b) { // 클래스 메서드 - 객체 생성 없이 사용 가능
		System.out.println("합:"+(a+b));
		return a+b;
	}
	
	static int sub(int a,int b) { // 클래스 메서드 - 객체 생성 없이 사용 가능
		System.out.println("빼기:"+(a-b));
		return a-b;
	}
	
	// multi,divide 메서드 작성
	
	static int multi(int a,int b) { // 클래스 메서드 - 객체 생성 없이 사용 가능
		System.out.println("곱:"+(a*b));
		return a*b;
	}
	static double divide(int a,int b) { // 클래스 메서드 - 객체 생성 없이 사용 가능
		if(b != 0) {
			System.out.println("나누기:"+(a/(double)b));
			return a/(double)b;
		}
		return 0.0;
	}

	
	
	
	public static void main(String[] args) {
		
		
		int a = 10;	// 지역변수 - 메서드 내에서 선언된 변수
		int b =3;	// 지역변수 - 메서드 내에서 선언된 변수
		
		int result = 0, result2 = 0, result3 = 0;
		double result4 = 0;

		
		// return문 사용
		// 더하기
		
		result = add2(a,b); // 클래스 메서드 사용 - 클래스명 생략가능
		result2 = sub(a,b); // 클래스 메서드 사용 - 클래스명 생략가능
		result3 = multi(a,b); // 클래스 메서드 사용 - 클래스명 생략가능
		result4 = divide(a,b); // 클래스 메서드 사용 - 클래스명 생략가능
		System.out.printf("%d,%d,%d,%.2f\n", result, result2,result3,result4);
		
		int[] aArr = {1,2,3};
		System.out.println(aArr); // 배열 주소값 출력
		tv t = new tv();
		System.out.println(t); // 객체 주소값 출력
		
		
		
		
		
		
		
		
		// 인스턴스 메서드 사용방법
//		C05 c1 = new C05(); // 객체 생성
//		c1.add(a,b); // 인스턴스 메서드 사용
//		
//		// 클래스 메서드 사용방법
//		add2(a,b); // 클래스 메서드 사용 - 클래스명 생략가능
//		sub(a,b); // 클래스 메서드 사용 - 클래스명 생략가능
//		
		
		
		/**
		 * 지역변수 - 메서드 내에서 선언된 변수
		 */
//		int a = 10;
//		int[] aArr = {1,2,3};
//		
//		System.out.println(a);
//		System.out.println(aArr);
		
		
//		C05 c1 = new C05(); // 객체 생성
//		System.out.println(c1.aa); // 인스턴스 변수 사용
//		System.out.println(bb); // 같은 클래스 변수 사용
//		
//		
//		
//		
//		int a = 10;	// 지역변수 - 메서드 내에서 선언된 변수
//		
//		//흰색,true,7
//		tv t = new tv();	// tv 객체 생성
//		t.color = "white";	// 색상 설정
//		t.power = true;		// 전원 켜기 버튼
//		t.channel = 7;		// 채널 설정
//		System.out.printf("%s,%b,%d\n",t.color,t.power,t.channel);	// 출력
//		
//		
//		//검정,false,10
//		tv t2 = new tv();	// tv 객체 생성
//		t2.color = "black";	// 색상 설정
//		t2.power = false;	// 전원 끄기 버튼
//		t2.channel = 10;	// 채널 설정
//		System.out.printf("%s,%b,%d\n",t2.color,t2.power,t2.channel);	// 출력

	}

}
