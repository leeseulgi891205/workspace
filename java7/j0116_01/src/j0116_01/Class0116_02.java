package j0116_01;

public class Class0116_02 {

	public static void main(String[] args) {
		// boolean - true / false
		boolean aa = true;
		boolean aa2 = false;
		System.out.println(aa);
		System.out.println(aa2);
		
		// char - 문자
		char bb = 'A';
		char bb2 = 65; //문자 1
		System.out.println(bb);
		
		// 숫자 정수 - 
		//byte - 1byte
		byte cc = 1;
		byte cc2 = 127; //-128 ~ 127
		byte cc3 = (byte)5000;  //오버플로우(overflow)
		System.out.println(cc);
		System.out.println(cc2);
		System.out.println(cc3);
		
		short dd = 1; //-32768 ~ 32767
		System.out.println(dd);
		
		int ee = 1; //-21억 ~ 21억
		int ee2 = (int)3300000000L; //오버플로우(overflow) : 약 21억까지 입력가능
		System.out.println(ee2);
		
		long ff = 1;
		long ff2 = 220_000_000L; //21억 밑으로는 생략가능, 21억 이상은 무조건 접미사 L
		System.out.println(ff2);
		
		// 실수 - float(4byte), double(8byte)
		float gg = 1.12345678F; //접미사 F
		double hh = 1.123456789012345678; //접미사 D(생략가능)
		
		//----------------------------------------------------------------
		
		// 참조형 변수(객체변수) - 무조건 new 사용
		// 문자열 변수 - 일반형 변수처럼 선언가능
		String str1 = new String("안녕하세요.");
		String str2 = "반갑습니다."; //new 생략가능
		System.out.println(str1);
		System.out.println(str2);
		
		int abc = 10;
		abc = 20;
		abc = 30;
		System.out.println(abc);
		
		final int aaa = 100; //상수형 변수 - final 키워드 사용
		//AAA =20; // 변수형태만 봐도 상수구나 이해할수 있도록 대문자 사용권장
		
		char ch = '\u0041'; //유니코드 - 16진수
		System.out.println(ch);
		
		
		
		
		
	}
}
