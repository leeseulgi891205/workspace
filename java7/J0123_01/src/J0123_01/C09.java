package J0123_01;

import java.util.Scanner;

public class C09 {

	public static void main(String[] args) {
		Scanner scanner = new Scanner(System.in);
		
		Student[] s = new Student[10];
		
		// 초기 데이터 4명 (인덱스 0, 1, 2, 3)
		s[0] = new Student("홍길동", 100, 100, 99);
		s[1] = new Student("유관순", 90, 90, 91);
		s[2] = new Student("이순신", 80, 80, 85);
		s[3] = new Student("강감찬", 95, 85, 90);
		
		// 중요!! 0~3번까지 찼으니 다음 번호는 4번!
		int count = 4; 
		
		while(true) {
			System.out.println("-----------------------------------------------------");
			System.out.println("1.입력:");
			System.out.println("2.출력:");
			System.out.println("3.수정:");
			System.out.println("4.삭제:");
			System.out.println("5.검색:");
			System.out.println("0.종료:");
			System.out.println("-----------------------------------------------------");
			System.out.print("번호를 입력하세요 >> ");
			int choice = scanner.nextInt();
			
			switch(choice) {
			case 1: // 입력
				if (count >= s.length) {
					System.out.println("더 이상 입력할 수 없습니다.");
					break;
				}
				System.out.println("[ 성적 입력 ]");
				System.out.print((count+1) + "번째 이름을 입력하세요: ");
				String name = scanner.next();
				System.out.print("국어: ");
				int kor = scanner.nextInt();
				System.out.print("영어: ");
				int eng = scanner.nextInt();
				System.out.print("수학: ");
				int math = scanner.nextInt();
				
				// 생성자를 통해 값을 쏙 넣으면 합계/평균 자동 계산됨 (Student.java 참고)
				s[count] = new Student(name, kor, eng, math);
				count++; 
				System.out.println("입력 완료!");
				break;
				
			case 2: // 출력
				System.out.println("[ 성적 출력 ]");
				System.out.println("이름\t국어\t영어\t수학\t총점\t평균");
				System.out.println("--------------------------------------------");
				for(int i=0; i<count; i++) {
					// 일일이 printf 하지 않고, 객체한테 "네 정보 출력해"라고 시킴
					s[i].printInfo(); 
				}
				break;
				
			case 3: // 수정
				System.out.println("[ 성적 수정 ]");
				System.out.print("수정할 학생 이름: ");
				String name1 = scanner.next();
				
				int idx = -1;
				for(int i=0; i<count; i++) {
					if(s[i].name.equals(name1)) {
						idx = i;
						System.out.println(name1 + " 학생을 찾았습니다.");
						
						System.out.print("수정할 국어 점수: ");
						s[i].kor = scanner.nextInt();
						System.out.print("수정할 영어 점수: ");
						s[i].eng = scanner.nextInt();
						System.out.print("수정할 수학 점수: ");
						s[i].math = scanner.nextInt();
						
						// 핵심 점수가 바뀌었으니 계산해! (메소드 호출)
						s[i].calculate();
						
						System.out.println("수정 완료!");
						break; 
					}
				}
				if(idx == -1) System.out.println("찾는 학생이 없습니다.");
				break;
				
			case 4: // 삭제
				System.out.println("[ 성적 삭제 ]");
				System.out.print("삭제할 학생 이름: ");
				String name2 = scanner.next();
				
				int idx2 = -1;
				for(int i=0; i<count; i++) {
					if(s[i].name.equals(name2)) {
						idx2 = i;
						break;
					}
				}
				
				if(idx2 != -1) {
					for(int i=idx2; i<count-1; i++) {
						s[i] = s[i+1];
					}
					s[count-1] = null;
					count--;
					System.out.println("삭제 완료!");
				} else {
					System.out.println("찾는 학생이 없습니다.");
				}
				break;
				
			case 5: // [검색]
				System.out.println("[ 성적 검색 ]");
				System.out.print("검색할 학생 이름: ");
				String name3 = scanner.next();
				
				int idx3 = -1;
				System.out.println("이름\t국어\t영어\t수학\t총점\t평균");
				System.out.println("--------------------------------------------");
				for(int i=0; i<count; i++) {
					if(s[i].name.equals(name3)) {
						s[i].printInfo(); // 여기서도 메소드 활용
						idx3 = i;
					}
				}
				if(idx3 == -1) System.out.println("검색된 학생이 없습니다.");
				break;
				
			case 0: // [종료]
				System.out.println("프로그램을 종료합니다.");
				return;
				
			default:
				System.out.println("잘못된 번호입니다. 다시 입력하세요.");
			} 
		} 
	} 
}