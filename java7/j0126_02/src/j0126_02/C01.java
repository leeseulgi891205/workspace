package j0126_02;

public class C01 {

	public static void main(String[] args) {

		// 0-4번까지 5장의 카드를 출력하시오.
		Deck d = new Deck();
		d.card5Print();
		d.card5Print(5);
		
		
		// 카드 5장 출력.
		d.shuffle();
		d.card5Print();
		
		//

		
		
		

	}

}
