package J01027_01;

public class Singleton {
	// private : 같은 클래스 내에서만 사용가능
	// static : 클래스변수(객체선언없이 클래스명.변수명)
	private static Singleton s = new Singleton();
	private int num;
	
	
	private Singleton() {}
	
	// 클래스메소드 : 객체선언없이 클래스명. 메소드명
	public static Singleton getInstance() { 
		return s;
	}
	
	public void setNum(int num) {
		this.num = num;
	}
	
	public int getNum() {
		return num;
	}
	
}
