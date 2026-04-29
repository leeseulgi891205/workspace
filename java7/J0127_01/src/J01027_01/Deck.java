package J01027_01;

public class Deck {
	// 카드 52장
	Card[] c = new Card[52];
	String[] shape = {"SPADE", "DIAMOND", "HEART", "CLOVER"};
	
	// 기본생성자
	Deck() {
		for (int i = 0; i < c.length; i++) {
			c[i] = new Card(shape[i / 13], (i % 13) + 1);
		}
	}
	
	void shuffle() {
		Card temp;
		for (int i = 0; i <1000;i++) {
			int no = (int)(Math.random()*52);
			temp = c[0];
			c[0] = c[no];
			c[no] = temp;
		}
	}
	
	
	// 카드 전체 출력
	void cardAllPrint() {
		for (int i = 0; i < c.length; i++) {
	        // c[i].number가 1이면 num[1]인 "A"가 출력됨
	        System.out.println(c[i].kind + " " + c[i].num[c[i].number]);
		}
	}
	// 카드 5장 출력
	void card5Print() {
		for (int i = 0; i < 5; i++) {
			System.out.println(c[i].kind + " " + c[i].number);
		}
	}
	// 무작위 카드 한 장 출력
	void pick() {
		int random = (int) (Math.random() * 52);
		System.out.println(c[random].kind + " " + c[random].number);
	}
	// 지정된 인덱스 카드 출력
	void pick(int index) {
		index = index % 52;
		System.out.println(c[index].kind + " " + c[index].number);
	}
}