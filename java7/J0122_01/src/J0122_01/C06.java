package J0122_01; // 패키지 선언 (파일이 저장된 폴더 위치)

public class C06 { // 클래스 선언 시작
	
	// ==========================================
	// 1. 사칙연산 기능을 수행하는 메서드(함수)들
	// ==========================================

	// [더하기 기능] 
	// static: 객체 생성(new) 없이 바로 쓸 수 있게 함
	// int: 결과값으로 정수를 돌려줌
	// (int a, int b, int c): 재료(매개변수)로 정수 3개를 받음
	static int add(int a, int b, int c) {	
		return a + b + c; // 세 수를 더한 값을 호출한 곳으로 돌려줌
	}

	// [빼기 기능]
	static int sub(int a, int b, int c) {
		return a - b - c; // 세 수를 뺀 값을 돌려줌
	}

	// [곱하기 기능]
	static int multi(int a, int b, int c) {
		return a * b * c; // 세 수를 곱한 값을 돌려줌
	}

	// [나누기 기능] ★중요: 결과가 소수점일 수 있어서 반환형이 double
	static double divide(int a, int b, int c) {
		// 0으로 나누면 에러가 나므로, 나누는 숫자가 0이 아닌지 먼저 검사
		if(b != 0 && c != 0) {
			// (double)b : 정수끼리 나누면 소수점이 버려지므로, 
			// b를 강제로 실수(double)로 바꿔서 정확한 소수점 계산을 함
			return a / (double)b / c; 
		}
		return 0.0; // 0으로 나누려는 경우, 0.0을 돌려줌 (에러 방지)
	}
	
	// ==========================================
	// 2. 모든 계산을 한 번에 처리하는 종합 메서드
	// ==========================================
	
	// [종합 계산 기능]
	// double[] : 결과값 여러 개(배열)를 돌려준다는 뜻 (나누기 결과 때문에 double 배열 사용)
	static double[] cal(int a, int b, int c) {
		
		// 1. 결과를 담을 '바구니(배열)' 만들기
		// double[4] : 방 4개짜리 실수형 배열 생성 (0번~3번 방)
		double[] result = new double[4]; 
		
		// 2. 각 방에 계산 결과 채워 넣기
		// add의 결과는 int(정수)지만, double(실수) 방에 넣으면 자동으로 13.0 처럼 변환됨
		result[0] = add(a, b, c);    // 0번 방: 더하기 결과
		result[1] = sub(a, b, c);    // 1번 방: 빼기 결과
		result[2] = multi(a, b, c);  // 2번 방: 곱하기 결과
		result[3] = divide(a, b, c); // 3번 방: 나누기 결과 (여기만 원래 실수)
		
		// 3. 꽉 채운 바구니(배열)를 통째로 돌려줌
		return result;
	}

	// ==========================================
	// 3. 메인 메서드 (프로그램 시작점)
	// ==========================================
	public static void main(String[] args) {
		// 사용할 변수(데이터) 준비
		int a = 10;
		int b = 3;
		int c = 2;
		
		// 결과를 받을 빈 배열 변수 선언
		// cal 함수가 double[]을 리턴하므로, 받는 쪽도 반드시 double[]이어야 함
		double[] re = cal(a, b, c); 
		
		// 결과 출력하기 (printf 사용)
		// %.0f : 소수점 없이 출력 (정수처럼 보임) -> 더하기, 빼기, 곱하기용
		// \n : 줄바꿈
		System.out.printf("더하기: %.0f\n", re[0]); 
		System.out.printf("빼기: %.0f\n", re[1]);
		System.out.printf("곱하기: %.0f\n", re[2]);
		
		// %.2f : 소수점 둘째 자리까지 출력 -> 나누기용
		System.out.printf("나누기: %.2f\n", re[3]); 
	}
}