package J0129_01;

import java.util.Scanner;
import java.util.Arrays;
import java.math.BigInteger;

public class C08 {

	public static void main(String[] args) {
		Scanner scan = new Scanner(System.in);
		
		
		int a = 10;
		Integer b = new Integer(10);
		BigInteger bigInt = new BigInteger("123456789012345678901234567890");
		
		
		
		
//		StringBuffer sb = new StringBuffer("0123");
//		sb.append("4");
//		System.out.println(sb);
//		
//		System.out.println(sb.charAt(0));
//		
//		String str = "0123";
//		str = str+4;
//		System.out.println(str.charAt(0));
		
		
		
		
		
		
		
//		//String, StringBuffer
//		
		
//		String str = "0"; // 10123456789
//		//str = str + "0";
//		int a = 0;
//		for(int i=1;i<10;i++) {
//			str += i;
//		}
//		
//		
//		System.out.println(str);
		
		
		
		
		
		
		//subString-문자열자르기
		//10조12345번
		//12345
//		String txt = "10조12345번";
//		System.out.println(txt.substring(3,8)); //3~7번째까지 잘라라
//		System.out.println(txt.substring(3)); //3~끝까지 잘라라
//		System.out.println(txt.substring(0));
//		
//		
//		// charAt(); - 문자1개 잘라내기
//		System.out.println(txt.charAt(2)); //0번째 문자1개 잘라내기
		
		
		
		
		//split(",")-특정문자분리,valueOf-타입변경,parseInt-타입변경
//		String txt = "1,홍길동,100,100,100,300,100.0";
//		String[] arr = txt.split(",");
//		int no = Integer.parseInt(arr[0]);
//		String name = arr[1];
//		int kor = Integer.parseInt(arr[2]);
//		int eng = Integer.parseInt(arr[3]);
//		int math = Integer.parseInt(arr[4]);
//		int total = Integer.parseInt(arr[5]);
//		double avg = Double.parseDouble(arr[6]);
//		
//		System.out.println(Arrays.toString(arr));
		
		
		
		
		//trim-빈공백제거, replace-문자대체
//		String txt = "     a     b    c    d";
//		String txt2 = "     abc      ";
//		System.out.println(txt);
//		System.out.println("원문:"+txt+"-");
//		System.out.println("앞뒤공백제거:"+txt2.trim()+"-"); //앞뒤공백제거
//		System.out.println("공백제거:"+txt.replace(" ", "")); //문자대체, 빈공백을 공백없이 대체
		
		
		
		
		
		
//		String txt = "aaabbbcdeaaabcccceaeaeab";
//		String txt2 =  txt.replace("a", "A");
//		System.out.println(txt2);
//		System.out.println(txt.length()-txt.replace("b", "").length());
//		
//		//indexOf();
//		System.out.println("문자길이:"+txt.length());
//		int count =0;
//		for(int i=0;i<txt.length();i++) {
//			if(txt.indexOf("a",i)!=-1) {
//				System.out.println("위치값 : "+txt.indexOf("e",i));
//				i=txt.indexOf("a",i)+1;
//				count++;
//			}else {
//				break;
//			}
//			System.out.println("----------");
//			System.out.println("a의 개수는? : "+count);
//			
//		}
		
		
		
//		System.out.println(txt.indexOf("e",8+1)); //8번째 이후부터 e를 찾아라
//		System.out.println(txt.indexOf("e",17+1));
//		System.out.println(txt.indexOf("e",19+1));
//		System.out.println(txt.indexOf("e",21-1));
//		System.out.println("-------------------");
		
		// e의 위치를 출력하시오.
//		for(int i=0;i<txt.length();i++) {
//			if(txt.charAt(i)=='e') {
//				System.out.println("E의 위치는? : "+i);
//			}
//		}
		
		
		
//		String[] name = {
//			"홍길동","유관순","이순신","강감찬","김구",
//			"김유신","홍길자","홍길순","신사임당","정약용"
//		};
//		
//		// 홍이 들어가 있는 사람을 모두 출력하시오.
//		int temp = 0;
//		System.out.println("[검색출력]");
//		for(int i=0;i<name.length;i++) {
//			if(name[i].contains("순")) {
//				System.out.println(i+","+name[i]);
//				temp=1;
//				
//				
//			}
//		}
//		System.out.println("----------------");
//		System.out.println("번호를 선택하세요:");
//		
//		int no = scan.nextInt();
//		
//		// 변경 이름을 입력받아, 수정을 시키고 전체출력을하시오.
//		System.out.println(name[no]+"을(를) 변경이름 입력하세요.");
//		String newName = scan.next();
//		name[no]=newName;
//		
//		System.out.println("[전체출력]");
//		for(int i=0;i<name.length;i++) {
//			System.out.println(i+": "+name[i]);
//		}
//		
//		
//		
//		
//		
//		if(temp==0)	{
//			System.out.println("검색된 사람이 없습니다.");
//			}else {
//				System.out.println("검색이 완료되었습니다.");
//		}

	}

}
