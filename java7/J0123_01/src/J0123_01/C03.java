package J0123_01;

public class C03 {
	// 클래스변수, 인스턴스변수, 지역변수 -메소드내선언
	// 클래스메소드- 객체선언없이 클래스명. 메소드명
	// 인스턴스메소도 - 객체선언후 참조변수.메소드명
//	int add(int a, int b) { // 인스턴스 메소드
//		return a+b;
//	}
	
	//sub,multi,divide 메소드 선언
	int sub(int a, int b) {	// 인스턴스메소드
		return a-b;// return
	}
	int multi(int a, int b) {// 인스턴스메소드 - 객체를 선언 후 참조변수, 메소드명으로 사용
		return a*b;
	}
	double divide(int a, int b) {
		return a/(double)b;
	}
	
	
	
	public static void main(String[] args) {
		// 객체선언후 사용
//		C03 c = new C03();
//		int a = 10;
//		int b = 3;
//		int result = c.add(10,3);
//		System.out.println(result);
		
		C03 c = new C03();	// 객체선언
		int a = 20;	// 지역변수
		int b = 5;
		int result1 = c.sub(20,5);
		int result2 = c.multi(20,5);
		double result3 = c.divide(20,5);
		System.out.println(result1);// 출력
		System.out.println(result2);
		System.out.println(result3);
		
	}

}
