package j0128;

public class Car {
	// 클래스마다 생성자가 1개이상 꼭 있어야 함.
	// 없으면 에러
	// 없으면 컴파일시 자동으로 생성해줌.
	
	//기본생성자
	Car(){}
	
	static String name; //클래스변수 - 객체선언없이 클래스명.변수명
	int door;           //인스턴스변수 - 객체선언후 참조변수명.변수명
	int speed;
	
	void speedUp() {
		System.out.println("속도를 높입니다.");
	}
	
	void stop() {
		System.out.println("정지합니다.");
	}
	
	
	
	
	
	
	
	
	
	//오버로딩 - 전혀다른 메소드의미
	int move() {
		return 10;
	}
	
	//인스턴스메소드 - 객체선언후 참조변수명.메소드명
	int move(int num) {
		int no=5; //지역변수-메소드내, 메소드를 벗어나면 사라짐.
		System.out.println("출발");
		return no*num;
	}

}
