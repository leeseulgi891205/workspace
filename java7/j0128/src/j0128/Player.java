package j0128;

abstract public class Player {
	
	int currentPlay;
	
	abstract void play(int cp); //미완성메소드
	abstract void stop();       //미완성메소드
	
	
	void play() { //오버로딩 - 완성메소드
		System.out.println("실행합니다.");
	}

}
