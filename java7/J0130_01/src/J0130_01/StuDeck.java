package J0130_01;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.FileWriter;
import java.io.FileReader;
import java.util.ArrayList;
import java.util.Comparator;
import java.util.Scanner;
import java.util.List;

public class StuDeck {
	Scanner scan = new Scanner(System.in);
	ArrayList<Stuscore> list = new ArrayList();
	
	int no,kor,eng,math,total,choice,temp;
	String name;
	double avg;
	
	String[] title = {"번호","이름","국어","영어","수학","합계","평균"};
	String filePath = "c:/aaa/stu2.txt";
	
	// 1. 성적입력
	void stu_input() {
		System.out.println((Stuscore.count+1)+"번 학생 이름을 입력하세요(0. 이전페이지 이동)>> ");
		name = scan.next();
		if(name.equals("0")) return;
		System.out.println("국어 점수를 입력하세요.>> ");
		kor = scan.nextInt();
		System.out.println("영어 점수를 입력하세요.>> ");
		eng = scan.nextInt();
		System.out.println("수학 점수를 입력하세요.>> ");
		math = scan.nextInt();
		list.add(new Stuscore(name,kor,eng,math));
		System.out.println(name+" 학생 성적 저장완료!!");
		System.out.println();
	} // stu_input end
	
	// 2. 성적출력
	void stu_output() {
		System.out.printf("%s\t%s\t%s\t%s\t%s\t%s\t%s\n",
				title[0],title[1],title[2],title[3],title[4],title[5],title[6]);
		System.out.println("-------------------------------------------------------");
		for(int i=0;i<list.size();i++) {
			Stuscore s = list.get(i);
		System.out.printf("%d\t%s\t%d\t%d\t%d\t%d\t%.2f\n",
				s.getNo(),s.getName(),s.getKor(),s.getEng(),s.getMath(),s.getTotal(),s.getAvg());
		}
		System.out.println();
	} // stu_output end
	
	// 2-2. 성적출력 (매개변수가 있는 메서드)
		void stu_output(List<Stuscore> list) {
			System.out.printf("%s\t%s\t%s\t%s\t%s\t%s\t%s\n",
					title[0],title[1],title[2],title[3],title[4],title[5],title[6]);
			System.out.println("-------------------------------------------------------");
			for(int i=0;i<list.size();i++) {
				Stuscore s = list.get(i);
			System.out.printf("%d\t%s\t%d\t%d\t%d\t%d\t%.2f\n",
					s.getNo(),s.getName(),s.getKor(),s.getEng(),s.getMath(),s.getTotal(),s.getAvg());
			}
			System.out.println();
		} // stu_output end
		
		
	// 3. 성적수정
		void stu_update() {
		    System.out.println("수정하려는 학생 이름을 입력하세요(0. 이전페이지 이동)>> ");
		    String inputName = scan.next(); // 필드 name 대신 지역변수 권장
		    if (inputName.equals("0")) return;

		    int temp = 0;
		    for (int i = 0; i < list.size(); i++) {
		        Stuscore s = list.get(i); // 찾은 학생 객체를 변수에 저장

		        if (s.getName().equals(inputName)) {
		            temp = 1;
		            System.out.println(inputName + " 학생을 찾았습니다.");
		            System.out.println("1. 점수수정  2. 수정취소");
		            System.out.print("선택 >> ");
		            choice = scan.nextInt();

		            if (choice == 1) {
		                System.out.println("--- 현재 점수 정보 ---");
		                System.out.println("국어: " + s.getKor() + ", 영어: " + s.getEng() + ", 수학: " + s.getMath());
		                System.out.println("-----------------------------");
		                System.out.println("수정할 과목을 선택하세요.");
		                System.out.println("1.국어  2.영어  3.수학  0.취소");
		                int subChoice = scan.nextInt();

		                switch (subChoice) {
		                    case 1:
		                        System.out.println("현재 국어점수: " + s.getKor());
		                        System.out.print("새 점수 입력 >> ");
		                        int input = scan.nextInt();
		                        s.setKor(input);
		                        s.calTotal();
		                        s.calAvg();
		                        System.out.println("수정이 완료되었습니다.");
		                        break;
		                    case 2:
		                        System.out.println("현재 영어점수: " + s.getEng());
		                        System.out.print("새 점수 입력 >> ");
		                        s.setEng(scan.nextInt());
		                        s.calTotal();
		                        s.calAvg();
		                        System.out.println("수정이 완료되었습니다.");
		                        break;
		                    case 3:
		                        System.out.println("현재 수학점수: " + s.getMath());
		                        System.out.print("새 점수 입력 >> ");
		                        s.setMath(scan.nextInt());
		                        s.calTotal();
		                        s.calAvg();
		                        System.out.println("수정이 완료되었습니다.");
		                        break;
		                    default:
		                        System.out.println("수정이 취소되었습니다.");
		                        break;
		                }
		                // 합계와 평균도 여기서 다시 계산해주는 로직을 넣으면 좋습니다 (예: s.calc())
		            } else {
		                System.out.println("수정 취소를 선택하셨습니다.");
		            }
		            break; // 학생을 찾았으므로 for문 탈출
		        }
		    } // for end

		    if (temp == 0) {
		        System.out.println("찾고자 하는 학생이 없습니다. 다시 입력하세요.");
		    }
		}// stu_update end
		
		
		
		
	
	// 4. 성적삭제
	void stu_delete() {
		System.out.println("삭제하려는 학생 이름을 입력하세요(0. 이전페이지 이동)>> ");
		name = scan.next();
		if(name.equals("0")) return;
		temp = 0;
		for(int i=0;i<list.size();i++) {
			if(list.get(i).getName().equals(name)) {
				temp = 1;
				System.out.println(name+"학생을 찾았습니다. 삭제하시겠습니까?(1.예 2.아니오)>> ");
				choice = scan.nextInt();
				if(choice == 1) {
					list.remove(i);
					System.out.println(name+" 학생 성적이 삭제되었습니다.");
				}
			}
		} // for end
		if(temp == 0) {
			System.out.println("찾고자 하는 학생이 없습니다. 다시 입력하세요.");
			System.out.println();
		}
	} // stu_delete end
	
	
	
	// 5. 성적검색
	void stu_search() {
		System.out.println("[학생검색]");
		System.out.println("1. 이름검색");
		System.out.println("2. 성적검색");
		System.out.print("--------------------------------");
		System.out.print("원하는 번호를 입력하세요.>>");
		choice = scan.nextInt();
		List<Stuscore> sList = new ArrayList();
		switch(choice) {
		case 1:
			temp = 0;
			System.out.println("검색할 이름을 입력하세요.>>");
			String search = scan.next();
			for(int i=0;i<list.size();i++) {
				Stuscore s = list.get(i);
				//equals:동일한이름, contains:포함되어 있는 이름
				if(s.getName().contains(search)) {
//				if(s.getTotal() >= 70) {//70점 이상 검색
					temp = 1;
					sList.add(s);
					
					
				}
			}
			if(temp == 0) { // 검색된 학생이 없으면
				System.out.println("검색한 이름이 없습니다. 다시 입력하세요.");
				System.out.println();
			}else {// 검색된 학생이 있으면 출력
				stu_output(sList);
			}
		}// switch end
	}
	
	
	
	
	
	// 6. 성적정렬
	void stu_sort(int choice) {
		System.out.println("[성적정렬]");
		System.out.println("1. 합계순 역순정렬");
		System.out.println("2. 이름순 순차정렬");
		System.out.print("--------------------------------");
		System.out.print("원하는 번호를 입력하세요.>>");
		choice = scan.nextInt();
		switch(choice) {
		case 1: // 합계순 역순정렬
				list.sort(new Comparator<Stuscore>() {
			    @Override
			    public int compare(Stuscore o1, Stuscore o2) { // c2를 o2로 변경
			        // 합계(total) 기준 내림차순 정렬
			        return o2.getTotal() - o1.getTotal(); 
			    }
			});
			break;
		case 2:// 이름순 순차정렬
			list.sort(new Comparator<Stuscore>() {
			    @Override
			    public int compare(Stuscore o1, Stuscore o2) { // c2를 o2로 변경
			        // 이름(name) 기준 오름차순 정렬
			        return o1.getName().compareTo(o2.getName()); 
			    }
			});
			break;
		}
	} // stu_sort end
	
	
	
	
	// 8. 파일불러오기
	void fileOpen() {
		try {
			FileReader fr = new FileReader(filePath);
			BufferedReader br = new BufferedReader(fr);
			while(true) {
				String line = br.readLine();
				if(line == null) break;
				String[] st = line.split(",");
				no = Integer.parseInt(st[0]);
				name = st[1];
				kor = Integer.parseInt(st[2]);
				eng = Integer.parseInt(st[3]);
				math = Integer.parseInt(st[4]);
				total = Integer.parseInt(st[5]);
				avg = Double.parseDouble(st[6]);
				list.add(new Stuscore(no,name,kor,eng,math,total,avg));
			}
			System.out.println("파일불러오기 완료!");
			System.out.println();
		} catch (Exception e) { e.printStackTrace(); }
		
		
	} // fileOpen end
	
	// 09. 파일저장
	void fileSave() {
		// 파일저장하기
		filePath = "c:/aaa/stu2.txt";
		try {
			FileWriter fw = new FileWriter(filePath);
			BufferedWriter bw = new BufferedWriter(fw);
			for(int i=0;i<list.size();i++) {
				Stuscore s = list.get(i);
				String st = String.format("%d,%s,%d,%d,%d,%d,%.2f\n", s.getNo(), s.getName(), s.getKor(), 
						s.getEng(), s.getMath(), s.getTotal(), s.getAvg());
				bw.write(st);
			}
			bw.close();
			fw.close();
		}catch (Exception e) { e.printStackTrace(); }
		
		System.out.println("파일이 저장되었습니다!");
		System.out.println();
	}
	
	
	
	
	// 00. 화면출력
	void screen() {
		System.out.println("[ 학생성적프로그램 ]");
		System.out.println("1. 성적입력");
		System.out.println("2. 성적출력");
		System.out.println("3. 성적수정");
		System.out.println("4. 성적삭제");
		System.out.println("5. 성적검색");
		System.out.println("6. 성적정렬");
		System.out.println("8. 파일불러오기");
		System.out.println("9. 파일저장");
		System.out.println("0. 프로그램종료");
		System.out.println("---------------------");
		System.out.println("원하는 번호를 입력하세요.>> ");
	} // screen end
	
}