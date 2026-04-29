package J0130_01;

import java.util.ArrayList;

public class C04 {

	public static void main(String[] args) {
		ArrayList<Card> list = new ArrayList();
		Card c1 = new Card("SPADE", 1);
		Card c2 = new Card("SPADE", 2);
		Card c3 = new Card("SPADE", 3);
		Stuscore s1 = new Stuscore("홍길동", 100, 100,100);
		Stuscore s2 = new Stuscore("유관순", 90, 80,70);
		Stuscore s3 = new Stuscore("이순신", 95, 85,75);
		String str1 = "홍길자";
		String str2 = "홍길순";
		list.add(c1);
		list.add(c2);
		list.add(c3);
//		list.add(s1);
//		list.add(s2);
//		list.add(s3);
//		list.add(str1);
//		list.add(str2);
		
		for(int i=0;i<list.size();i++) {
			// 지네릭스를 사용하면 형변환을 하지 않음.
			Card c = list.get(i);
		    System.out.println(c.kind);
		}
		
		
		
		// 출력하시오.
//		for (int i=0;i<list.size();i++) {
//		    Object o = list.get(i);
//		    if (list.get(i) instanceof Card) {
//		        Card c = (Card) o;
//		        System.out.println(c);
//		    } else if (list.get(i) instanceof Stuscore) {
//		        Stuscore s = (Stuscore) o;
//		        System.out.println(s.getName());
//		    } else if (list.get(i) instanceof String) {
//		        String str = (String) o;
//		        System.out.println(str);
//		       
//		    }
//		}
//		
		

	}

}
