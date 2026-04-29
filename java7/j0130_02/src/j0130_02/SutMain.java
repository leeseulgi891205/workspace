package j0130_02;

import java.util.Scanner;

public class SutMain {

    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        StuDeck s = new StuDeck();

        while (true) {
            s.screen();
            int choice = scan.nextInt();

            switch (choice) {
                case 1:
                    s.stu_input();
                    break;
                case 2:
                    s.stu_output();
                    break;
                case 3:
                    s.stu_update();
                    break;
                case 4:
                    s.stu_delete();
                    break;
                case 8:
                    s.fileOpen();
                    break;
                case 9:
                    s.fileSave();
                    break;
                case 0:
                    System.out.println("프로그램을 종료합니다.");
                    scan.close();
                    return;
                default:
                    System.out.println("번호 다시 입력하세요.\n");
            }
        }
    }
}
