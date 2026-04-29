package J0123_01;

public class C01 {
	
	int aa; //인스턴스 변수 - 객체 생성후 사용가능
	static int aaa; //정적변수 - 클래스명.변수명 으로 사용가능
	
	static void staticChange() { //클래스 메소드 = 객체선언없이 클래스명. 메소드명
		int abc = 0; //지역변수 - 메소드내에서만 사용가능
	}
	
	void change() { //인스턴스 메소드 - 객체 생성후 참조변수명. 메소드명
		int ab = 0;	//지역변수 - 메소드내에서만 사용가능
	}

	public static void main(String[] args) {
		
		
		
		
		//클래스명 참조변수명 = new 클래스명();
//		Tv t = new Tv(); //Tv객체생성
//		
//		Student s = new Student(); //객체선언 방법
//		s.no = "2023001";
//		s.id = "aaa";
//		s.pw = "1111";
//		s.name = "홍길동";
//		s.phone = "010-1111-1111";
//		s.gender = "남자";
//		s.hobby = "운동";
//		Student s2 = new Student();
//		s2.no = "2023002";
//		s2.id = "bbb";
//		Student s3 = new Student();
//		s3.no = "2023003";
//		s3.id = "ccc";
		
		
		//Stuscore 클래스명 생성
		//no, name, kor, eng, math,total, avg 변수넣고
		//main메소드에서
		//1.홍길동 100,100,100,300,100.0 입력하시오.
		
		Stuscore[] ss = new Stuscore[5];	
		ss[0] = new Stuscore();
		ss[0].no = "1";
		ss[0].name = "홍길동";
		ss[0].kor = 100;
		ss[0].eng = 100;
		ss[0].math = 100;
		ss[0].total = ss.kor + ss.eng + ss.math;
		ss[0].avg = ss.total / 3.0;
		System.out.println(ss.no);
		System.out.println("이름:" + ss.name);
		System.out.println("국어점수: " + ss.kor);
		System.out.println("영어점수:" + ss.eng);
		System.out.println("수학점수:" + ss.math);
		System.out.println("합계:" + ss.total);
		System.out.println("평균:" + ss.avg);
		
		
		
		
		
		
		
		//객체 - 여러타입 여러개 저장방법,메소드도 입력가능
//		Tv aaa = new Tv();
//		aaa.channel = 10;
//		aaa.color = "white";
//		System.out.println(aaa);
//		System.out.println(aaa.channel);//객체변수 접근방법 - .(도트연산자)
		
		
		
		
//		//배열 - 같은타입 여러개 저장방법
//		int[] aa = {1,2};
////		System.out.println(aa);
////		System.out.println(aa[0]);
//		
//		int [] bb = {0,0};
//		bb = aa;
//		System.out.println(bb[0]+"," + bb[1]);
//		aa[0] = 100;	//aa배열의 0번지 값을 100으로 변경
//		System.out.println(bb[0]+"," + bb[1]);	//bb배열의 0번지 값도 변경됨 - 주소값이 복사되어서 그렇다.
		
		
		//기본형 8가지 타입 - 변수 하나에 하나의 값 저장
//		boolean a = true;
//		char b = 'a';
//		byte c = 1;
//		short d = 1;
//		int e = 1;
//		long f = 1L;
//		float g = 1.0f;
//		double h = 1.0;
//		System.out.println(a);
	}

}
