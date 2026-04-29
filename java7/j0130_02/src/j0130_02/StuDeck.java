package j0130_02;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.FileReader;
import java.io.FileWriter;
import java.util.ArrayList;
import java.util.Scanner;

public class StuDeck {
    Scanner scan = new Scanner(System.in);
    ArrayList<Stuscore> list = new ArrayList<>();

    int kor, eng, math, choice, temp;
    String name;

    String[] title = {"번호","이름","국어","영어","수학","합계","평균"};
    String filePath = "c:/aaa/stu2.txt";

    // 1. 성적입력
    void stu_input() {
        System.out.println((Stuscore.count + 1) + "번 학생 이름을 입력하세요(0. 이전페이지 이동)>> ");
        name = scan.next();
        if (name.equals("0")) return;

        System.out.println("국어 점수를 입력하세요.>> ");
        kor = scan.nextInt();
        System.out.println("영어 점수를 입력하세요.>> ");
        eng = scan.nextInt();
        System.out.println("수학 점수를 입력하세요.>> ");
        math = scan.nextInt();

        list.add(new Stuscore(name, kor, eng, math));
        System.out.println(name + " 학생 성적 저장완료!!\n");
    }

    // 2. 성적출력
    void stu_output() {
        System.out.printf("%s\t%s\t%s\t%s\t%s\t%s\t%s\n",
                title[0], title[1], title[2], title[3], title[4], title[5], title[6]);
        System.out.println("-------------------------------------------------------");

        for (int i = 0; i < list.size(); i++) {
            Stuscore s = list.get(i);
            System.out.printf("%d\t%s\t%d\t%d\t%d\t%d\t%.2f\n",
                    s.getNo(), s.getName(), s.getKor(), s.getEng(), s.getMath(), s.getTotal(), s.getAvg());
        }
        System.out.println();
    }

    // 3. 성적수정
    void stu_update() {
        System.out.println("수정하려는 학생 이름을 입력하세요(0. 이전페이지 이동)>> ");
        name = scan.next();
        if (name.equals("0")) return;

        temp = 0;
        for (int i = 0; i < list.size(); i++) {
            if (list.get(i).getName().equals(name)) {
                temp = 1;
                System.out.println(name + "학생을 찾았습니다. 수정하시겠습니까?(1.예 2.아니오)>> ");
                choice = scan.nextInt();
                if (choice == 1) {
                    System.out.println("국어 점수를 입력하세요.>> ");
                    kor = scan.nextInt();
                    System.out.println("영어 점수를 입력하세요.>> ");
                    eng = scan.nextInt();
                    System.out.println("수학 점수를 입력하세요.>> ");
                    math = scan.nextInt();

                    Stuscore s = list.get(i);
                    s.setKor(kor);
                    s.setEng(eng);
                    s.setMath(math);

                    System.out.println(name + " 학생 성적이 수정되었습니다!!\n");
                }
                break;
            }
        }

        if (temp == 0) {
            System.out.println("찾는 학생이 없습니다.. 다시 입력하세요.\n");
        }
    }

    // 4. 성적삭제
    void stu_delete() {
        System.out.println("삭제하려는 학생 이름을 입력하세요(0. 이전페이지 이동)>> ");
        name = scan.next();
        if (name.equals("0")) return;

        temp = 0;
        for (int i = 0; i < list.size(); i++) {
            if (list.get(i).getName().equals(name)) {
                temp = 1;
                System.out.println(name + "학생을 찾았습니다. 삭제하시겠습니까?(1.예 2.아니오)>> ");
                choice = scan.nextInt();
                if (choice == 1) {
                    list.remove(i);
                    System.out.println(name + " 학생 성적이 삭제되었습니다!!\n");
                }
                break;
            }
        }

        if (temp == 0) {
            System.out.println("찾는 학생이 없습니다.. 다시 입력하세요.\n");
        }
    }

    // 8. 파일불러오기
    void fileOpen() {
        list.clear(); // ✅ 기존 리스트 초기화하고 불러오기

        try (BufferedReader br = new BufferedReader(new FileReader(filePath))) {

            while (true) {
                String line = br.readLine();
                if (line == null) break;
                line = line.trim();
                if (line.length() == 0) continue;

                // 1,홍길자,90,80,70,240,80.0
                String[] st = line.split(",");

                int no = Integer.parseInt(st[0].trim());
                String name = st[1].trim();
                int kor = Integer.parseInt(st[2].trim());
                int eng = Integer.parseInt(st[3].trim());
                int math = Integer.parseInt(st[4].trim());
                int total = Integer.parseInt(st[5].trim());
                double avg = Double.parseDouble(st[6].trim());

                list.add(new Stuscore(no, name, kor, eng, math, total, avg));
            }

            System.out.println("파일불러오기가 완료되었습니다.\n");

        } catch (Exception e) {
            System.out.println("파일불러오기 실패\n");
            e.printStackTrace();
        }
    }

    // 9. 파일저장
    void fileSave() {
        try (BufferedWriter bw = new BufferedWriter(new FileWriter(filePath))) {
            for (Stuscore s : list) {
                String line = s.getNo() + "," + s.getName() + "," + s.getKor() + "," + s.getEng() + "," + s.getMath()
                        + "," + s.getTotal() + "," + s.getAvg();
                bw.write(line);
                bw.newLine();
            }
            System.out.println("파일저장이 완료되었습니다.\n");
        } catch (Exception e) {
            System.out.println("파일저장 실패\n");
            e.printStackTrace();
        }
    }

    // 00. 화면출력
    void screen() {
        System.out.println("[ 학생성적프로그램입니다. ]");
        System.out.println("1. 성적입력");
        System.out.println("2. 성적출력");
        System.out.println("3. 성적수정");
        System.out.println("4. 성적삭제");
        System.out.println("8. 파일불러오기");
        System.out.println("9. 파일저장");
        System.out.println("0. 종료");
        System.out.println("---------------------");
        System.out.print("원하는 번호를 입력하세요!! >> ");
    }
}
