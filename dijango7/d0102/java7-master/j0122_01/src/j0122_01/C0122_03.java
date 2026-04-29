package j0122_01;

import java.util.Arrays;
import java.util.Scanner;

public class C0122_03 {

	public static void main(String[] args) {
		
		Tv t1 = new Tv(); //객체선언,객체생성
		
		Scanner scanner = new Scanner(System.in);
		String[] title = {"번호","이름","국어","영어","수학","합계","평균"};
		Stuscore[] s = new Stuscore[10];
		int count = 0;
		while(true) {
			s[count] = new Stuscore();
			s[count].no = count+1;
			System.out.printf("%d번째 이름을 입력하세요.(0.모두출력)>> ",count+1);
			s[count].name = scanner.next();
			//0 -> 모두출력으로 이동
			if(s[count].name.equals("0")) {
				break;
			}
			System.out.println("국어점수를 입력하세요.>> ");
			s[count].kor = scanner.nextInt();
			System.out.println("영어점수를 입력하세요.>> ");
			s[count].eng = scanner.nextInt();
			System.out.println("수학점수를 입력하세요.>> ");
			s[count].math = scanner.nextInt();
			s[count].total = s[count].kor+s[count].eng+s[count].math;
			s[count].avg = s[count].total/3.0;
			count++;
		}
		
		System.out.printf("%s\t%s\t%s\t%s\t%s\t%s\t%s\n",title[0],title[1],title[2],title[3],title[4],title[5],title[6]);
		System.out.println("-----------------------------------------------------------");
		for(int i=0;i<count;i++) {
			System.out.printf("%d\t",s[i].no);   //번호
			System.out.printf("%s\t",s[i].name);   //이름
			System.out.printf("%s\t",s[i].kor);   //국어
			System.out.printf("%s\t",s[i].eng);   //영어
			System.out.printf("%s\t",s[i].math);   //수학
			System.out.printf("%s\t",s[i].total);   //합계
			System.out.printf("%.2f\n",s[i].avg); //평균
		}
		System.out.println();
		
		
		
		
		
//		s[0] = new Stuscore();
//		s[0].no = 1;
//		s[0].name = "홍길동";
//		s[0].kor = 100;
//		s[0].eng = 100;
//		s[0].math = 99;
//		s[0].total = s[0].kor+s[0].eng+s[0].math;
//		s[0].avg = s[0].total/3.0;
		
		// 홍길동
//		Stuscore s1 = new Stuscore();
//		s1.no = 1;
//		s1.name = "홍길동";
//		s1.kor = 100;
//		s1.eng = 100;
//		s1.math = 99;
//		s1.total = s1.kor+s1.eng+s1.math;
//		s1.avg = s1.total/3.0;
//		// 유관순 90,90,91 입력해보세요.
//		Stuscore s2 = new Stuscore();
//		s2.no = 2;
//		s2.name = "유관순";
//		s2.kor = 90;
//		s2.eng = 90;
//		s2.math = 91;
//		s2.total = s2.kor+s2.eng+s2.math;
//		s2.avg = s2.total/3.0;
		
		
		
		
		// 다른 클래스 사용하는 방법 - 객체선언후 사용가능
		
//		int[] a = {1,2,3};
//		int[] b = {4,5,6};
//		
//		System.out.println(Arrays.toString(a)); //1,2,3
//		System.out.println(Arrays.toString(b)); //4,5,6
//		
//		b = a;
//		System.out.println(Arrays.toString(a)); //1,2,3
//		System.out.println(Arrays.toString(b)); //1,2,3
//		
//		a[1] = 1000;
//		System.out.println(Arrays.toString(b));
//		System.out.println(a);
//		
//		Tv t1 = new Tv();
//		System.out.println(t1);
		
		
		
		
		
		
//		int a = 10;
//		int b = 0;
//		b = a;
//		System.out.println(a); //10
//		System.out.println(b); //10
//		a=100;
//		System.out.println(a); //100
//		System.out.println(b); //10
//		System.out.println("-------------");
//		Tv t1 = new Tv();
//		Tv t2 = new Tv();
//		System.out.println(t1.channel);//0
//		System.out.println(t2.channel);//0
//		
//		t2 = t1;
//		t1.channel = 7;
//		System.out.println(t1.channel);//7
//		System.out.println(t2.channel);//7
		
		
		
//		Tv t1 = new Tv();
//		t1.color = "white";
//		System.out.println(t1.color);
//		System.out.println(t1.power); //false
//		t1.power = true;
//		System.out.println(t1.power); //true
//		t1.power(); //!true => false
//		System.out.println(t1.power);
//		System.out.println(t1.channel);
//		t1.channel = 11;
//		System.out.println(t1.channel);
		
		
	}

}
