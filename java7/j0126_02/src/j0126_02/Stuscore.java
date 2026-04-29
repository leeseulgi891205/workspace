package j0126_02;

public class Stuscore {
	
	{ // 초기화블록 : 생성자를 실행시 먼저 실행되는 함수
		count++;
		no = count;
	}
	Stuscore(){}
	Stuscore(String name,int kor,int eng,int math){
		this.name = name;
		this.kor = kor;
		this.eng = eng;
		this.math = math;
	}
	
	static int count;
	int no;
	String name;
	int kor;
	int eng;
	int math;
	int total;
	double avg;

}
