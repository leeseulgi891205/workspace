package J0130_01;

import java.util.HashSet;
import java.util.Iterator;
import java.util.HashMap;
import java.util.Map;
import java.util.List;
import java.util.ArrayList;


public class C03 {

	public static void main(String[] args) {
		
//		HashMap<String,Object> map = new HashMap();
		Map<String, Object> map = new HashMap<>();
		List list = new ArrayList();
		List list2 = new ArrayList();
		List list3 = new ArrayList();
		list.add(1);//[0]
		list.add(2);//[1]
		list.add(list2);//[2]:list2참조값
		list.add(list3);//[3]:list3참조값
		
		// 입력 - put()
		map.put("name", "홍길동");
		map.put("boardList", list);
		map.put("memberList", list2);
		// 읽어오기, 출력 get()
		System.out.println(map.get("name"));
		
		
		// 전체출력 - map은 list를 상속하지 않기 때문에 Iterator를 바로 사용할 수 없음.
		// map -> set으로 변경해서 Iterator를 사용함.
		
		Iterator it = map.entrySet().iterator();
		while(it.hasNext()) {
			System.out.println(it.next());
		}
		
		
		
//		//set 순서X, 중복X
//		HashSet set = new HashSet();
//		set.add(1);	//int -> Integer -> Object
//		set.add(2);
//		set.add(3);
//		set.add(4);
//		set.add(5);
//		set.add(3);
//		set.add(2);
//		
//		Iterator it = set.iterator();
//		while(it.hasNext()) {
//			int a = (int)it.next();
//			System.out.println(a);
//		}
	}

}
