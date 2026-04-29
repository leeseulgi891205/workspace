package J0129_01;
import java.util.Scanner;
public class StuMain {

	public static void main(String[] args) {
		Scanner scan = new Scanner(System.in);
		StuDeck s = new StuDeck();
		
		loop:while(true) {
			s.screen_print();
			int choice = scan.nextInt();
			switch(choice) {
			case 1:
				s.stu_input(); //성적입력
				
				break;
			case 2:
				s.stu_output(); //성적출력
				
				break;
			case 3:
				s.stu_update(); //성적수정
				
				break;
			case 4:
				s.stu_delete(); //성적삭제
				
				break;
			case 5:
				s.stu_search(); //성적검색
				
				break;
			case 0:
				System.out.println("[프로그램을 종료합니다]");
				break loop;
			}
		}//while
		


	}

}
