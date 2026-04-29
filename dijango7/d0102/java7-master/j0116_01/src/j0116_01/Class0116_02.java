package j0116_01;

public class Class0116_02 {

	public static void main(String[] args) {
		// boolean - true,false
		boolean aa = true;
		boolean aa2 = false;
		System.out.println(aa);
		System.out.println(aa2);
		
		// char - 문자
		char bb = 'a';
		char bb2 = '1'; //문자 1
		System.out.println(bb);
		
		// 숫자 - 정수 : byte,short,int,long
		//byte -128 ~ 127
		byte cc = 1;
		byte cc2 = 127;
		byte cc3 = (byte) 5000; //오버플로우(overflow)
		System.out.println(cc);
		System.out.println(cc2);
		System.out.println(cc3);
		
		short dd = 1;
		System.out.println(dd);
		
		int ee = 1;
		int ee2 = (int)3300000000L; // 오버플로우 : 약 21억까지 입력가능
		System.out.println(ee2);
		
		long ff = 1;
		long ff2 = 220_000_000L; // 21억 밑으로는 생략가능, 21억이상은 무조건 접미사 L을 붙여야 함.
		System.out.println(ff2);
		
		//실수 - float,double
		float gg = 1.12345678F; // 접미사 F를 무조건 붙여야 함.
		double hh = 1.123456789123456789; //접미사 D는 생략가능
		
		//--------------------------------------------------
		
		// 참조형 변수 (객체변수) - 무조건 new 객체명()
		// 문자열 변수 - 일반형변수처럼 선언가능
		String str = new String("aaa");
		String str2 = "bbb";
		System.out.println(str);
		
		int abc = 10;
		abc = 20;
		abc = 30;
		System.out.println(abc);
			
		final int AAA = 100; // 상수
		// AAA = 20; // 변수형태만 봐도 상수구나 이해할수 있도록 대문자 사용권장
		
		char ch = '\u0041'; // \\u : 16진수를 의미함.
		System.out.println(ch);
		

	}

}
