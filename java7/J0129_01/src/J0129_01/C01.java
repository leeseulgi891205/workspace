package J0129_01;

public class C01 {
	
	
	static int a;// 클래스변수 - 자동 초기화
	int b;		 // 인스턴스 변수 : 객체선언후 참조변수명.변수명 - 자동 초기화
	

	public static void main(String[] args) {
		
		int c=0;	//지역변수 - 자동초기화 안됨.
		System.out.println(c);
		
		//b를 출력하시오.
		C01 c1 = new C01();
		System.out.println(c1.b);
		
		System.out.println(c1.a);
		System.out.println(a);//같은 클래스내에서는 클래스변수명만으로 접근가능.
		
		System.out.println(new Stuscore("홍길동",85,90,80));
	}

}
