package j0128;

public class A {
	// 다형성
	void methodA(B b) {
		System.out.println("B클래스 호출");
		b.methodB();
	}

}
