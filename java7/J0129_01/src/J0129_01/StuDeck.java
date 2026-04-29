package J0129_01;

import java.util.Scanner;
import java.util.ArrayList;
import java.util.Iterator;

public class StuDeck {
	
	StuDeck(){
		list.add(new Sutscore("홍길동", 85, 90, 80));
		list.add(new Sutscore("김철수", 75, 70, 60));
		list.add(new Sutscore("이영희", 95, 100, 90));
	}
	
	//객체컬렉션 - 객체담을수 있는 배열(list)
	// add, get, remove, size(), isEmpty()
	ArrayList<Sutscore> list = new ArrayList<Sutscore>();
	Scanner scan = new Scanner(System.in);
	String name,search;
	int no, kor, eng, math, total,temp,choice;
	double avg;
	String[] title = {"번호","이름","국어","영어","수학","합계","평균"};
	
	//성적입력
	void stu_input() {
		System.out.println((Sutscore.count+1)+"번 학생이름을 입력하세요.>>");
		name = scan.next();
		System.out.println("국어점수를 입력하세요.>>");
		kor = scan.nextInt();
		System.out.println("영어점수를 입력하세요.>>");
		eng = scan.nextInt();
		System.out.println("수학점수를 입력하세요.>>");
		math = scan.nextInt();
		// 번호,합계,평균 자동부여
		list.add(new Sutscore(name, kor, eng, math));
		
		System.out.println(name+"[성적이 입력되었습니다.]");
		System.out.println();

	}
	//2. 성적출력
	void stu_output() {
		System.out.printf("%s\t%s\t%s\t%s\t%s\t%s\t%s\n",
				title[0],title[1],title[2],title[3],title[4],title[5],title[6]);
		
		//Iterator 사용출력
		Iterator<Sutscore> it = list.iterator();
		while(it.hasNext()) {
			Sutscore s = it.next();
			System.out.printf("%d\t%s\t%d\t%d\t%d\t%d\t%.2f\n",
					s.getNo(),s.getName(),s.getKor(),s.getEng(),s.getMath(),
					s.getTotal(),s.getAvg());
		}
		
		
//		System.out.println("-------------------------------------------------");
//		for(int i=0; i<list.size(); i++) {
//			Sutscore s = list.get(i);
////			System.out.println(list.get(i));
//			System.out.printf("%d\t%s\t%d\t%d\t%d\t%d\t%.2f\n",
//					s.getNo(),s.getName(),s.getKor(),s.getEng(),s.getMath(),
//					s.getTotal(),s.getAvg());
		}//for
//		System.out.println();
	
	
	
	//성적수정
	void stu_update() {
		System.out.println("수정할 학생이름을 입력하세요.>>");
		search = scan.next();
		temp = 0;
		for(int i=0;i<list.size();i++) {
			Sutscore s = list.get(i);
			//수정할 학생을 찾은경우
			if(s.getName().equals(search)) {
				temp = 1;
				System.out.println(search+"학생을 찾았습니다.");
				System.out.println("국어점수를 입력하세요.>>");
				kor = scan.nextInt();
				System.out.println("영어점수를 입력하세요.>>");
				eng = scan.nextInt();
				System.out.println("수학점수를 입력하세요.>>");
				math = scan.nextInt();
				
				//수정처리
				s.setKor(kor);
				s.setEng(eng);
				s.setMath(math);
				s.calTotal(kor, eng, math);
				s.calAvg(kor, eng, math);
				
				System.out.println("성적수정이 완료되었습니다.");
				break;
			}//if
		}//for
		if(temp==0) {
			System.out.println(search+"학생은 존재하지 않습니다.");
		}
		System.out.println();
		
		
	}
	
	//성적삭제
	void stu_delete() {
		System.out.println("삭제할 학생이름을 입력하세요.>>");
		search = scan.next();
		temp = 0;
		for(int i=0;i<list.size();i++) {
			Sutscore s = list.get(i);
			//삭제할 학생을 찾은경우
			if(s.getName().equals(search)) {
				temp = 1;
				System.out.println(search+"학생을 찾았습니다. 삭제하시겠습니까?(1.예 2.아니오)>>");
				choice = scan.nextInt();
				if(choice==1) {
					list.remove(i);
					System.out.println("삭제가 완료되었습니다.");
					break;
				}else {
					System.out.println("삭제가 취소되었습니다.");
					break;
				}				
				
			}//if
		}//for
		if(temp==0) {
			System.out.println(search+"학생은 존재하지 않습니다.");
		}
		System.out.println();
	}
	
	//성적검색
	void stu_search() {
		System.out.println("검색할 학생이름을 입력하세요.>>");
		search = scan.next();
		temp = 0;
		System.out.printf("%s\t%s\t%s\t%s\t%s\t%s\t%s\n",
				title[0],title[1],title[2],title[3],title[4],title[5],title[6]);
		for(int i=0;i<list.size();i++) {
			Sutscore s = list.get(i);
			//검색할 학생을 찾은경우
			if(s.getName().equals(search)) {
				temp = 1;
				System.out.printf("%d\t%s\t%d\t%d\t%d\t%d\t%.2f\n",
						s.getNo(),s.getName(),s.getKor(),s.getEng(),s.getMath(),
						s.getTotal(),s.getAvg());
			}//if
		}//for
		if(temp==0) {
			System.out.println(search+"학생은 존재하지 않습니다.");
		}
		System.out.println();
		
	}
		
	
	
	
	//화면출력
	void screen_print() {
		System.out.println("[학생성적프로그램]");
		System.out.println("1. 성적입력");
		System.out.println("2. 성적출력");
		System.out.println("3. 성적수정");
		System.out.println("4. 성적삭제");
		System.out.println("5. 성적검색");
		System.out.println("0. 프로그램종료");
		System.out.println("-------------------");
		System.out.print("원하는 번호를 입력하세요.>>");
	}
	

}
