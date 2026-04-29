package J0130_01;

import java.util.ArrayList;
import java.util.List;
import java.util.Iterator;

public class C01 {

	public static void main(String[] args) {
//		list-순서가있고 중복가능,
//		set-순서없고 중복불가,
//		map-key-중복불가,value-중복가능
		
		ArrayList list = new ArrayList();// 기본타입으로 객체 생성 - 자식타입으로 참조 가능
//		List list2 = new ArrayList(); // 다형성 - 부모타입으로 자식객체를 참조
		
		//입력
		int a = 11;
		list.add(11); //int(Integer wrapper클래스) -> Object 자동 박싱
		list.add(22);
		list.add(33);
		list.add(11);
		list.add(33);
		
		//1개 가져오기
		int aa = (int)list.get(0); //Object -> Integer -> int 자동 언박싱
//		System.out.println(aa);
		
		
		//삭제
		list.remove(3);
		
		
		
		//전체출력
		for(int i=0; i<list.size();i++) {
			int no = (int)list.get(i);
			System.out.println(no);
		}
		
		// Iterator
		System.out.println("=== Iterator ===");
		// 원래 규칙 Iterator를 사용해서 전체출력을 해야 함.
		Iterator it = list.iterator();
		while(it.hasNext()) {//다음에 가져올 객체가 있니? hasNext()
			int list_date = (int)it.next();
			System.out.println(list_date);
			
		}

	}

}
