package J0123_01;

public class C02 {

	public static void main(String[] args) {
		//객채사용 목적 - 여러개 값을 한번에 저장하기위해
		//배열사용 모적 - 각각 여러개 값을 저장하기위해
		
		int[] a = {1,4,3};
		int[] b = {1,2,3};
		
		
		
		//클래스명.변수명
		Card.width = 200;
		Card.height = 300;
		System.out.println(Card.width);
		System.out.println(Card.height);
		
		Card c1 = new Card();
		c1.kind = "SPADES";
		c1.number = 10;
		c1.width = 500;
		System.out.println(c1.width);
		Card c2 = new Card();
		c2.kind = "HEARTS";
		System.out.println(c2.height);
		

	}

}
