package pro01;

public class MainMethod {

	public static void main(String[] args) {
		System.out.println("메인프로그램");
		// 클래스에서 다른클래스 사용하려면 객체선언해야 사용가능
		//Tv tv = new Tv();
		//Tv2 tv2 = new Tv2();
		Product p = new Tv3();
		p.name = "삼성Tv";
		System.out.println(p.name);
		Audio audio = new Audio();
		audio.name = "하만오디오";
		System.out.println(audio.name);

	}

}
