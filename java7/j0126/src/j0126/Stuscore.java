package j0126;

public class Stuscore {
	{ // 초기화블록:생성자의 공통적으로 사용되는 것들을 정의
	  count++;
	  no = count;
	}
	
	Stuscore(){} //기본생성자-클래스명같다,리턴값이 없다,void안붙임.
	Stuscore(String name,int kor,int eng,int math){
		this.name = name;
		this.kor = kor;
		this.eng = eng;
		this.math = math;
		this.total = kor+eng+math;
		this.avg = this.total/3.0;
	}
	
	static int count;
	int no;   //인스턴스변수-객체선언후 참조변수명.변수명
	String name;
	int kor;
	int eng;
	int math;
	int total;
	double avg;
	
	public void calTotal(int kor,int eng,int math) {
		this.total = kor+eng+math;
	}
	
	public void calAvg(int kor,int eng,int math) {
		this.avg = this.total/3.0;
	}

}
