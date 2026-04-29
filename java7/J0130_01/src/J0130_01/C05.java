package J0130_01;

import java.util.Scanner;

public class C05 {

	public static void main(String[] args) {
		Scanner scan = new Scanner(System.in);
		// 특정한 값만 입력을 받고자 할때 enum형태를 입력받음.
		Gender g = Gender.남성;
		System.out.println(g);
		
		Person p = new Person();
		p.g = Gender.남성; // g -> "남성";
		
		
		
		
		
//		Day today = Day.월요일;
//		System.out.println(today);
//		
		
		
		
		
		
		
		
//		while(true) {
//		System.out.print("요일을 입력하세요");
//		String day = scan.next();
//		System.out.println("입력한 요일은: "+day);
//		
//	}
		

	}

}
