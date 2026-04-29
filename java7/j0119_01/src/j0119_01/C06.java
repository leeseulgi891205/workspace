package j0119_01;

public class C06 {

public static void main(String[] args) {
		int count = 0;
		String num = "789057899979971234567";
		
		// indexOf() 메소드와 for문을 이용해서 7이 있는 위치들과 총 개수를 출력하시오.
		for(int i = 0; i<num.length();i++) {
		    if(num.indexOf('7',i)==i){
		       System.out.println("7의 위치: "+i);
		       count++;
		    }
		}
		
		System.out.println("7의 총 개수: "+count);
	}

}