package J0122_01;

public class C04 {
	
	public static void main(String[] args) {
		// 배열
		Stuscore[] sArr = new Stuscore[10];
		// 객체선언
		sArr[0] = new Stuscore();
		sArr[0].no = sArr[0].count + 1;
		sArr[0] = new Stuscore();
		
		// 객체선언
		Stuscore s = new Stuscore();
		s.no = Stuscore.count + 1; // 인스턴스 변수 no에 클래스 변수 count를 이용하여 번호 부여
		s.name = "홍길동"; // 이름 저장
		s.kor = 100; // 국어점수 저장
		s.eng = 100; // 영어점수 저장
		s.math = 99; // 수학점수 저장
		s.calTotal(); // 합계 계산 메서드 호출
		s.calAvg(); // 평균 계산 메서드 호출
		Stuscore.count++;
		Stuscore s2 = new Stuscore();
		s2.no = Stuscore.count + 1;
		s2.name = "유관순";
		s2.kor = 90;
		s2.eng = 90;
		s2.math = 91;
		s2.calTotal();
		s2.calAvg();
		
		
		
		System.out.printf("%d,%s,%d,%d,%d,%d,%.2f\n", s.no, s.name, s.kor, s.eng, s.math, s.total, s.avg);
		System.out.printf("%d,%s,%d,%d,%d,%d,%.2f\n", s2.no, s2.name, s2.kor, s2.eng, s2.math, s2.total, s2.avg);


	}
}
