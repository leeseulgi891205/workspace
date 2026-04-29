package j0126_02;

public class Deck {
	Card[] c = new Card[52];
	String[] shape = {"SPADE","HEART","DIAMOND","CLOVER"};
	
	Deck(){
		for(int i=0;i<c.length;i++) {
			//1,2,3,4,5,6,7,8,9,10,11,12,13,1,2,3,4,.... 4번반복
			c[i] = new Card();
			c[i].number = (i%13)+1; // 0,1,2,3,4,5,6,7,8,9,10,11,12
			c[i].kind = shape[i/13];   // 0-12:spade,13-26:heart,....
		}
	}
	
	//5장 뽑기
	void card5Print() {
		for(int i=0;i<5;i++) {
			System.out.println(c[i].kind+","+c[i].number);
		}
	}
	//지정한 번호부터 5장 뽑기
	void card5Print(int index) {
		for(int i=index;i<index+5;i++) {
			System.out.println(c[i].kind+","+c[i].number);
		}
	}
	
	// 카드 섞기
	void shuffle() {
		for(int i=0;i<500;i++) {
			int random = (int)(Math.random()*52);
			Card temp = c[0];
			c[0] = c[random];
			c[random] = temp;
		}
	}
	
	
	
	
	
}
