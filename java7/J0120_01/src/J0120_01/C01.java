package J0120_01;
import java.util.Scanner;
public class C01 {

	public static void main(String[] args) {
		
		// boolean,char,byte,short,int,long,float,double,String
		// 등가비교 == 비교가능
		
//		int a = 10;
//		if(a==10) {
//			System.out.println("맞습니다.");
//		} else {
//			System.out.println("아닙니다.");
//		}
		
		// String타입은 등가비교가 안됨. == 사용불가!
		// 객체타입이기 때문에 . equals() 사용해야한다.
		
		String str1 = "10"; // 얕은복사
		String str2 = "100";
		String str3 = new String("10");
		String str4 = "10";
		
		System.out.printf("%s,%s,%s \n",str1,str2,str3);
		if(str1==str2) { // 10 == 100 -> false
			System.out.println("같습니다.");
		} else {
			System.out.println("다릅니다.");
		}
		if(str1==str3) { // 주소값 비교
			System.out.println("같습니다.");
		} else {
			System.out.println("다릅니다.");
		}
		if(str1.equals(str3)) { // 내용비교
			System.out.println("같습니다.");
		} else {
			System.out.println("다릅니다.");
		}
		
		
		
		
		
		
//		String str1 ="['게임','골프','수영','조깅','독서']";
//		String str2 ="['축구','족구','농구']";
//		String str3 ="['배구','골프','수영','조깅','독서']";
//		String str4 ="['양궁','골프','수영','조깅','독서']";
//		String str5 ="['배드민턴','골프','조깅','독서']";
//		
//		// 수영이 포함되어 수영있습니다. 수영이 없습니다. 출력하시오.
//		
//		//str1 수영이 포함되어 있나요?
//		if(str1.contains("수영")) System.out.println("수영이 포함되어 있습니다.");
//		else System.out.println("수영이 없습니다.");
//		
//		if(str2.contains("수영")) System.out.println("수영이 포함되어 있습니다.");
//		else System.out.println("수영이 없습니다.");
//		
//		if(str3.contains("수영")) System.out.println("수영이 포함되어 있습니다.");
//		else System.out.println("수영이 없습니다.");
//		
//		if(str4.contains("수영")) System.out.println("수영이 포함되어 있습니다.");
//		else System.out.println("수영이 없습니다.");
//		
//		if(str5.contains("수영")) System.out.println("수영이 포함되어 있습니다.");
//		else System.out.println("수영이 없습니다.");

		
		
		
		
		
//		Scanner scanner = new Scanner(System.in);
//		System.out.println("숫자를 입력하세요.>>");
//		String str = scanner.next();
//		System.out.println("찾고자 하는 번호를 입력하세요.>>");
//		String input = scanner.next();
//		// contains:포함되어 있는지 확인 indexOf: 포함되어 있는지 확인, 위치값
//		// indexOf
//		int startNo = 0;
//		int count = 0;
//		String s_print = "";
//		
//		for(;;) {
//			int temp = str.indexOf(input,startNo);
//			if(temp==-1) break;
//			// 3을 찾았을 경우
//			count++;
//			s_print += temp+" ";
//			startNo = temp+1;
//		}
//		
//		System.out.printf("%s의 위치값: %s \n",input,s_print);
//		System.out.printf("%s포함 개수: %d \n ",input,count);
		
		
		
		
		
		
		
		
		
		
		
		// contains
//		if (str.contains("비트코인")==true) {
//			System.out.println("3이 포함되어 있습니다.");
//		} else {
//			System.out.println("3이 포함되어 있지 않습니다.");
//		}
		
		
		
		
		
		
		
		
		
		
		
//		System.out.print("숫자입력하세요.>> : ");
//		String str = scanner.next();
//
//		int count = 0;
//		String s_print = "";
//		for (int i = 0; i < str.length(); i++) {
//		    int no = str.charAt(i) - '0';  // 문자 -> 숫자 변환 
//		    if (no == 7) {
//		        count++;
//		        if(count==1)s_print = i+"";
//		        else s_print += (","+i);
//		    }
//		}
//		System.out.println("입력된 숫자길이 : "+count);
//		System.out.println("입력값 : " + s_print);
//		System.out.println("결과값 : " + str);
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		// 1459 -> 입력받은 숫자들의 합을 구하시오.
//		System.out.print("숫자입력하세요.>> : ");
//		String str = "Scanner.next()";
//		// (char)(2+'0')
//		// '2'-'0'
//		int sum = 0;
//		String s_print = "";
//		for(int i = 0; i < str.length(); i++) {
//			int no = str.charAt(i)-'0';
//			sum += no;
//			if (i==0) s_print += no+"";
//			else s_print += (","+no);
//
//		}
////		System.out.printf("%d,%d,%d,%d \n",no1,no2,no3,no4);
//		System.out.println("입력된 숫자길이 : "+str.length());
//		System.out.println("입력값 : "+s_print);
//		System.out.println("결과값 : "+sum);


		
		
		
		
		
		
		
		// 34.1592
		// 소수점 3자리까지 출력
//		double num = 34.1592;
//		
//		double num2 = (Math.round(num*100))/100.0; // long타입으로 반환되기 때문에 double타입으로 나누기
//		System.out.println(num2);
		
		
		
		
		//소수점 반올림 : round, 올림, 내림 : ceil, floor
//		System.out.println(Math.round(34.95));
//		System.out.println(Math.ceil(34.95));
//		System.out.println(Math.floor(34.95));
		
		
		
		
		
		
		
		
		
		
		// Math.random() 0*10=0 <= int(Math.random()*10)+1 < 1*10
		
		
		// 1~5번까지 랜덤숫자를 입력하는데, 중복이 없도록 숫자를 입력하시오.
//		int no1 = 0;
//		int no2 = 0;
//		int no3 = 0;
//		
//		for(int i = 0; i < 100; i++) {
//			no1 = (int)(Math.random()*3)+1;
//			no2 = (int)(Math.random()*3)+1;
//			no3 = (int)(Math.random()*3)+1;
//			
//			if(no1!=no2&&no2!=no3&&no1!=no3){
//				break;
//			}
//		}
//		
//		System.out.println("no1:"+no1);
//		System.out.println("no2:"+no2);
//		System.out.println("no3:"+no3);
		
		
		
		
//		// 문자숫자타입을 숫자타입으로 변경
//		int no = '2'-'0';
//		System.out.println(no); // int숫자로 취환
//		
//		// 숫자를 문자로 취환
//		char ch = (char)(2 + '0'); // 2+48=50
//		System.out.println(ch); // char문자로 취환
//		
//		// String타입 -> char타입 변경
//		String str = "123";
//		char str2 = str.charAt(0); // 문자1개 가져옴.
//		
//		// 숫자타입 -> String타입 변경(문자열타입)
//		String str3 = 234+"";
//		
//		//문자열타입-> int타입 변경
//		String str4 = "20";
//		int num = Integer.parseInt(str4); // int타입으로 변경
//		String str5 = "10";
//		int num2 = Integer.parseInt(str5); // int타입으로 변경
//		System.out.println(num+num2);

	}

}
