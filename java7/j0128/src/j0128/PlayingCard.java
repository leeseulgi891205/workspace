package j0128;

//인터페이스 - interface 붙이고, 상수와 미완성메소드로 이뤄짐.
public interface PlayingCard {
	public static final int SPADE = 4;
	int DIAMOND = 3;
	int HEART = 2;
	int CLOVER = 1;

	public abstract String getCardNumber();
	void pick();
	String getCardKind();
}
