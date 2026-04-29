package j0116_01;

public class Class0116_03 {
	public static void main(String[] args) {
		System.out.println("안녕하세요.");
		
		System.out.println("hello");
		System.out.println("java");
		
		char ch = 'A';
		char ch2 = 'a';
		char ch3 = '\u0041'; //유니코드
		char tab = '\t'; //탭
		
		System.out.println(ch);
		System.out.println(ch2);
		System.out.println(ch3);
		System.out.println("A"+tab+"a");
		
		
		char ch4 = 'a';
		// char ch4 = 'aa'; //문자 1개만 가능 -> 오류

		// char ch5 = ''; //'' 넣지 않는 것은 에러
		char ch5 = '0'; //빈 문자는 허용되지 않으므로 임의 문자 사용
		char ch6 = ' '; //공백 문자 가능
		
		String str = ""; //빈 문자열 가능
		
		// 문자열은 모든 타입을 포함시킬수 있음
		String str2 = "7";
		// String str3 = '7'; //문자열은 "" 사용, '' 사용 불가 -> 오류
		System.out.println();
		
		String str4 = "7";
		// int num = str4; //문자열을 정수형에 바로 넣을수 없음 -> 오류
		System.out.println("7"+7+7);
		
		
		String str3 = "aaa";
		str3 = str3 + 7; //문자열에 정수값 이어붙이기
		System.out.println(str3);
		
		int a = 7;
		int b = 8;
		System.out.println(a+b+str4); //15
		
		
	}

}