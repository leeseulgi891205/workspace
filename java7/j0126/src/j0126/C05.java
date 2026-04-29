package j0126;

public class C05 {

	public static void main(String[] args) {
		Deck d = new Deck(); //객체선언
		
		//지정한 카드 1장뽑기
		Card c = d.pick(1); //1-52
		System.out.println(c.kind+","+c.number);
		
		// 랜덤카드 1장뽑기
		Card c2 = d.pick(); //1-52
		System.out.println(c2.kind+","+c2.number);
		
		// 카드 5장 뽑기
		Card[] cArr= d.pick5();
		for(int i=0;i<cArr.length;i++) {
			System.out.println(cArr[i].kind+","+cArr[i].number);
		}
		
		d.shuffle();
		
		cArr= d.pick5();
		for(int i=0;i<cArr.length;i++) {
			System.out.println(cArr[i].kind+","+cArr[i].number);
		}
		
		System.out.println("--------------------");
		//지정한 카드 1장뽑기
		Card c3 = d.pick(1); //1-52
		System.out.println(c3.kind+","+c3.number);
		
		
		
		
		
		
		//		Card[] c = new Card[52];
//		c[0] = new Card();
//		c[0].kind = "SPADE";
//		c[0].number = 1;
//		c[1].kind = "SPADE";
//		c[1].number = 2;
//		c[2].kind = "SPADE";
//		c[2].number = 3;
//		c[13].kind = "HEART";
//		c[13].number = 1;		
//		c[14].kind = "HEART";
//		c[14].number = 2;		

	}

}
