package J0123_01;

public class Stuscore {
	static int count = 1; // 클래스변수
	String no;
	String name;
	int kor;
	int eng;
	int math;
	int total;
	double avg;

	// 기본생성자
	Stuscore(){
		this.no = String.valueOf(count);
		count++;
	}
	
	// 매개변수 생성자 (String name)
	Stuscore(String name){
		this.name = name;
		this.no = String.valueOf(count);
		count++;
	}
	
	// 복사생성자
	Stuscore(Stuscore stu){
		this.name = stu.name;
		this.no = String.valueOf(count);
		count++;
	}
	
	// 전체 매개변수 생성자
	Stuscore(String name, int kor, int eng, int math){
		this.name = name;
		this.kor = kor;
		this.eng = eng;
		this.math = math;
		this.total = kor + eng + math;
		this.avg = total / 3.0;
		this.no = String.valueOf(count);
		count++;
	}
}