package J0122_01;

import java.util.Arrays;
import java.util.Scanner;

/// 클래스 변수 , 인스턴트 변수, 지역변수

public class C03 {

	public static void main(String[] args) {
		Scanner scanner = new Scanner(System.in);
		String title[] = {"번호","이름","국어","영어","수학","합계","평균"};	// 제목 배열
		Stuscore [] s = new Stuscore[10];	// 학생 10명 정보 저장 가능
		int count = 0;	// 입력된 학생 수
		while(count < 3) {	// 최대 10명까지 입력 가능
			s[count] = new Stuscore();	// Stuscore 객체 생성
			s[count].no = count+1;	// 번호는 1부터 시작
			System.out.printf("%d번째 이름을 입력하세요 : (0.모두출력)", count+1);	// 이름 입력
			s[count].name = scanner.next();	// 이름 저장
			// 0 -> 모두출력으로 이동
			if(s[count].name.equals("0")) {	// 0입력시 모두출력으로 이동
				break;
			}
			System.out.println("국어점수를 입력하세요 : ");	// 국어점수 입력
			s[count].kor = scanner.nextInt();	// 국어점수 저장
			System.out.println("영어점수를 입력하세요 : ");	// 영어점수 입력
			s[count].eng = scanner.nextInt();	// 영어점수 저장
			System.out.println("수학점수를 입력하세요 : ");	// 수학점수 입력
			s[count].math = scanner.nextInt();	// 수학점수 저장
			s[count].total = s[count].kor+s[count].eng+s[count].math;	// 합계 계산
			s[count].avg = s[count].total/3.0;	// 평균 계산
			
			
			count++;
		}
		
		System.out.printf("%s %s %s %s %s %s %s\n", title[0],title[1],title[2],title[3],title[4],title[5],title[6]);
		System.out.println("=============================================");
		for(int i=0;i<count;i++) {	// 입력된 학생 수만큼 출력
			System.out.printf("%d\t",s[i].no); // 번호
			System.out.printf("%s\t",s[i].name); // 이름
			System.out.printf("%d\t",s[i].kor); // 국어
			System.out.printf("%d\t",s[i].eng); // 영어
			System.out.printf("%d\t",s[i].math); // 수학
			System.out.printf("%d\t",s[i].total); // 합계
			System.out.printf("%.2f\n",s[i].avg); // 평균
		}
		
		
		
		
		
//		Stuscore [] s = new Stuscore[3];
//		s[0] = new Stuscore();
//		s[0].no = 1;
//		s[0].name = "홍길동";
//		s[0].kor = 100;
//		s[0].eng = 100;
//		s[0].math = 99;
//		s[0].total = s[0].kor+s[0].eng+s[0].math;
//		s[0].avg = s[0].total/3.0;
//		
		// 홍길동
//		Stuscore s1 = new Stuscore();
//		s1.no = 1;
//		s1.name = "홍길동";
//		s1.kor = 100;
//		s1.eng = 100;
//		s1.math = 99;
//		s1.total = s1.kor+s1.eng+s1.math;
//		s1.avg = s1.total/3.0;
//		
//		// 유관순 90,90,91 입력
//		Stuscore s2 = new Stuscore();
//		s2.no = 2;
//		s2.name = "유관순";
//		s2.kor = 90;
//		s2.eng = 90;
//		s2.math = 91;
//		s1.total = s2.kor+s2.eng+s2.math;
//		s2.avg = s2.total/3.0;
		
		
		
		
		
//		int[] a = {1,2,3};
//		int[] b = {4,5,6};
//		
//		System.out.println(Arrays.toString(a)); // [1, 2, 3]
//		System.out.println(Arrays.toString(b)); // [4, 5, 6]
//		
//		
//		b = a; // b에 a의 주소값 대입(얕은복사)
//		System.out.println(Arrays.toString(a)); // [1, 2, 3]
//		System.out.println(Arrays.toString(b)); // [1, 2, 3]
//		
//		a[1] = 1000;// a배열의 두번째 요소값 변경
//		System.out.println(Arrays.toString(a)); // [1, 1000, 3]
//		System.out.println(a); // [I@15db9742
//		
//		tv t1 = new tv(); // tv클래스의 객체 t1선언
//		System.out.println(t1); // J0122_01.tv@6d06d69c
		
		
		
		
		
		
//		int a = 10;
//		int b = 0;
//		b = a;
//		System.out.println(b); // 10
//		
//		a = 100;
//		System.out.println(a); // 100
//		System.out.println(b); // 10
//		System.out.println("=========");
//		
//		tv t1 = new tv(); // tv클래스의 객체 t1선언
//		tv t2 = new tv(); // tv클래스의 객체 t2선언
//		System.out.println(t1.channel); // 0
//		System.out.println(t2.channel); // 0
//		
//		
//		t2 = t1; // t2에 t1의 주소값 대입(얕은복사)
//		t1.channel = 7;
//		System.out.println(t1.channel); // 7
//		System.out.println(t2.channel); // 7
		
		
		
		
		
		
		
		
		
		
		
//		tv t1 = new tv(); // tv클래스의 객체 t1선언
//		t1.color = "white";
//		System.out.println(t1.color); // white
//		System.out.println(t1.power); // false
//		t1.power = true; // 전원토글
//		System.out.println(t1.power); // true
//		t1.power(); // !true -> false
//		System.out.println(t1.power); // false
//		System.out.println(t1.channel); // 0
//		t1.channel = 11;
//		System.out.println(t1.channel); // 11
	}

}
