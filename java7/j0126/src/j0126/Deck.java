package j0126;

public class Deck {
	
	final int CARD_NUM = 52; //카드는 총 52장
	Card[] c = new Card[CARD_NUM];
	String[] shape = {"SPADE","HEART","DIAMOND","CLOVER"};
	
	// 기본생성자
	Deck() {
		for(int i=0;i<c.length;i++) {
			//1,2,3,4,5,6,7,8,9,10,11,12,13,1,2,3,4,.... 4번반복
			c[i] = new Card();
			c[i].number = (i%13)+1; // 0,1,2,3,4,5,6,7,8,9,10,11,12
			c[i].kind = shape[i/13];   // 0-12:spade,13-26:heart,....
		}
	} 
	
	// 카드 1장 뽑기
	Card pick(int index) {
		return c[index-1];
	}
	
	// 랜덤 1장 뽑기
	Card pick() {
		return c[(int)(Math.random()*52)];
	}
	
	// 5장 카드뽑기
	Card[] pick5() {
		return  new Card[]{c[0],c[1],c[2],c[3],c[4]};
	}
	
	
    // 카드섞기
	void shuffle() {
		for(int i=0;i<500;i++) {
			int random = (int)(Math.random()*52); //0-51
			Card temp = c[0];
			c[0] = c[random];
			c[random] = temp;
		}
		System.out.println("카드섞기가 완료되었습니다.");
	}
	
	
	

}
