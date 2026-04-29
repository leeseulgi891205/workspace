package j0122_01;

public class Stuscore {
	static int count; //클래스변수
	int no;           //인스턴스변수
	String name;
	int kor;
	int eng;
	int math;
	int total;
	double avg;
	
	public void calTotal() {
		total = kor+eng+math;
	}
	
	public void calAvg() {
		avg = total/3.0;
	}
	
}
