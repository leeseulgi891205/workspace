package J0123_01;

public class C07 {

	public static void main(String[] args) {
		Stuscore[] s = new Stuscore[3];
		s[0] = new Stuscore("홍길동", 100, 100, 99);
		s[1] = new Stuscore("유관순", 90, 90, 91);
		s[2] = new Stuscore("이순신", 80, 80, 85);
		
		for(int i=0;i<Stuscore.count-1;i++) {
			System.out.printf("%s,%s,%d,%d,%d,%d,%.2f%n",s[i].no,s[i]
					.name,s[i].kor,s[i].eng,s[i].math,s[i].total,s[i].avg);
			
		}
	}

}
