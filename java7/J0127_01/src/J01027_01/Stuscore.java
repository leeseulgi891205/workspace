package J01027_01;

public class Stuscore {
	
	static int count;
	int no;
	String name;
	int kor;
	int eng;
	int math;
	int total;
	double avg;
	
	void calTotal(int kor, int eng, int math) {
		this.total = kor + eng + math;
	}
	
	void calAvg(int kor, int eng, int math) {
		this.avg = (kor + eng + math) / 3.0;
	}
	
	//초기화블록
	{
		count++;
		no = count;	//번호 자동증가
	}
	
	
	
	// 기본생성자
	Stuscore() {}
	
	// 매개변수가 있는 생성자
	Stuscore(String name, int kor, int eng, int math) {
		count++;
		this.no = count;
		this.name = name;
		this.kor = kor;
		this.eng = eng;
		this.math = math;
		this.total = kor + eng + math;
		this.avg = this.total / 3.0;
	}
}
