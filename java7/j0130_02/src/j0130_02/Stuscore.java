package j0130_02;

public class Stuscore {

    // 자동 번호용 카운트
    static int count = 0;

    private int no;
    private String name;
    private int kor;
    private int eng;
    private int math;
    private int total;
    private double avg;

    // 기본생성자(자동 번호 부여)
    public Stuscore() {
        this.no = ++count;
    }

    // 성적입력용 생성자(자동 번호 부여)
    public Stuscore(String name, int kor, int eng, int math) {
        this(); // 자동 번호 부여
        this.name = name;
        this.kor = kor;
        this.eng = eng;
        this.math = math;
        calc();
    }

    // 파일 불러오기용 생성자(파일에 있는 번호 그대로 사용)
    public Stuscore(int no, String name, int kor, int eng, int math, int total, double avg) {
        this.no = no;
        this.name = name;
        this.kor = kor;
        this.eng = eng;
        this.math = math;
        this.total = total;
        this.avg = avg;

        // ✅ 파일에서 불러온 가장 큰 번호로 count를 맞춰서
        // 이후 입력 시 번호가 이어지게 함
        if (no > count) count = no;
    }

    private void calc() {
        this.total = kor + eng + math;
        this.avg = this.total / 3.0;
    }

    // getter/setter
    public int getNo() { return no; }
    public void setNo(int no) { this.no = no; }

    public String getName() { return name; }
    public void setName(String name) { this.name = name; }

    public int getKor() { return kor; }
    public void setKor(int kor) { this.kor = kor; calc(); }

    public int getEng() { return eng; }
    public void setEng(int eng) { this.eng = eng; calc(); }

    public int getMath() { return math; }
    public void setMath(int math) { this.math = math; calc(); }

    public int getTotal() { return total; }
    public void setTotal(int total) { this.total = total; }

    public double getAvg() { return avg; }
    public void setAvg(double avg) { this.avg = avg; }
}
