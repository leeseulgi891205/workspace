package J0123_01;

public class Student {
    String name;
    int kor;
    int eng;
    int math;
    int total;
    double avg;

    // 1. 기본 생성자 (비어있는 객체 만들 때 씀)
    Student() {}

    // 2. 성적 입력용 생성자 (객체 만들면서 바로 점수까지 넣을 때 씀)
    Student(String name, int kor, int eng, int math) {
        this.name = name;
        this.kor = kor;
        this.eng = eng;
        this.math = math;
        // 생성될 때 합계와 평균을 자동으로 계산
        this.total = kor + eng + math;
        this.avg = this.total / 3.0;
    }

    // 3. 합계, 평균 재계산 메소드 (점수 수정할 때 호출)
    void calculate() {
        this.total = this.kor + this.eng + this.math;
        this.avg = this.total / 3.0;
    }

    // 4. 정보 출력 메소드 (출력할 때 일일이 쓰기 귀찮으니까 만듦)
    void printInfo() {
        System.out.printf("%s\t%d\t%d\t%d\t%d\t%.2f%n", 
                name, kor, eng, math, total, avg);
    }
}