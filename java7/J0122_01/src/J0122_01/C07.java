package J0122_01;

// 1). 데이터를 담을 클래스 (설계도)
class AA {
	int result;    // 더하기 결과 저장
	int result2;   // 빼기 결과 저장
	int result3;   // 곱하기 결과 저장
	double result4;// 나누기 결과 저장 (실수)
}

public class C07 {
	
	// 2). 계산 함수
	// 매개변수: 데이터를 담을 객체(AA), 계산할 숫자(a, b, c)
	static void cal(AA p,int a,int b,int c) {
		// p는 main의 aObj와 같은 주소를 가리킴 (동일한 바구니)
		p.result = a+b+c;
		p.result2 = a-b-c;
		p.result3 = a*b*c;
		p.result4 = a/(double)b/c; // 실수 계산을 위해 (double) 형변환
	}

	public static void main(String[] args) {
		
		// 1. 객체 생성 (빈 바구니 만들기)
		AA aObj = new AA();
		
		// 2. 계산할 데이터 준비
		int a = 10;
		int b = 3;
		int c = 2;
		System.out.println("더하기값: " + aObj.result); // 아직 0
		
		// 3. 함수 호출 (바구니와 재료를 보냄)
		// aObj(주소)를 보냈으므로, 함수가 저 바구니에 값을 채워줌
		cal(aObj, a, b, c); 
		
		// 4. 결과 출력
		System.out.printf("더하기: %d\n", aObj.result);
		System.out.printf("빼기: %d\n", aObj.result2);
		System.out.printf("곱하기: %d\n", aObj.result3);
		System.out.printf("나누기: %.2f\n", aObj.result4);
		
		
		// aObj -> result, result2, result3, result4
		// 더하기값, 빼기값, 곱하기값, 나누기값을 입력받아
		// 출력하시오.
		
		
		
		
		
		
//		// 매개변수가 참조형변수로 전달될때는 값이 변경됨.
//		int[] a = {50}; // 지역변수
//		System.out.println("1번째 :"+a[0]);	//지역변수
//		
//		//함수호출
//		change(a); // 배열은 참조형이므로 주소값이 전달됨.
////		System.out.println(a);
////		System.out.println(a[0]); // 값이 절대 변경되지 않음
////		
////		//함수호출후 결과값
//		System.out.println("함수호출후 값"+a[0]);	//지역변수
		
		
		
		
		
		
		
		
		// 매개변수가 기본형변수로 전달될때는 값이 변경되지 않음.
//		int a = 50; // 지역변수
//		System.out.println("1번째 :"+a);	//지역변수
//		
//		//함수호출
//		change(a);
//		
//		//함수호출후 결과값
//		System.out.println("함수호출후 값"+a);	//지역변수

	}

}
