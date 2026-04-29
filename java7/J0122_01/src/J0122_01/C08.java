package J0122_01;

public class C08 {
	
	static void cal(int kor,int eng, int math, double[] cValue) { // 합계,평균을 구하는 함수
		// kor, eng, math: 입력값(매개변수)
		cValue[0] = kor+eng+math; // 합계
		cValue[1] = cValue[0]/3.0;   // 평균
	}

	public static void main(String[] args) { // 프로그램 시작점
		
		double[] cValue = new double[2]; // 합계,평균을 저장할 배열
		
		int kor = 100; // 국어점수
		int eng = 100; // 영어점수
		int math = 99; // 수학점수
		
		
		// 함수 호출 후 합계,평균을 구해서 출력하시오.
		cal(kor,eng,math,cValue);
		System.out.printf("합계: %.0f\n", cValue[0]);	// 소수점 없이 출력
		System.out.printf("평균: %.2f\n", cValue[1]);// 소수점 둘째자리까지 출력
		


	}

}
