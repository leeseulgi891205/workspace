package J0123_01;
import java.util.Arrays;

public class C05 {
	

	
	long a,b;
	int a2;
	
	long add() {
		return a+b; // 에러 안나는이유: long형이 int형보다 크기때문에 자동형변환
	}
	
	static long add(long a, long b) {
		return a+b; // 오버로딩뜻 - 같은 이름의 메서드를 여러개 정의하는것
	}
	
	static long add(long a, long b, long c) {
		return a+b+c;  
	}

	// 오버로딩 - 메소드명은 동일 - 매개변수 개수 또는 타입
	public static void main(String[] args) {
		//long a=0; 같은 메소드 내에 같은 이름의 변수를 선언할 수 없다.
		int[] num = new int[3];
		Amethod a = new Amethod();
		a.input(num);
		System.out.println(Arrays.toString(num));
		
		
		System.out.println(1);
		System.out.println(1.0);
	}
	
}
