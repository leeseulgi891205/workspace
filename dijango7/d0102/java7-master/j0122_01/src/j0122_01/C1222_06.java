package j0122_01;

public class C1222_06 {

	// 함수선언
	static int add(int a,int b,int c) {
		return a+b+c;
	}
	static int sub(int a,int b,int c) {
		return a-b-c;
	}
	
	static int[] cal(int a,int b,int c) {
		
		int[] re = new int[2];
		int result = a+b+c;
		re[0] = a+b+c;
		re[1] = a-b-c;
		return re;
	}
	
	public static void main(String[] args) {
		int a = 10;
		int b = 3;
		int c = 2;
		int[] re;
		
		re = cal(a,b,c);
		
		System.out.println(re[0]+","+re[1]);
		
//		int result = 0,result2=0,result3=0;
//		double result4 = 0;
//		
//		// 매개변수 3개를 보내서 add,sub,multi,divide 함수를 만들어서
//		// 결과값을 리턴 받아, 출력하시오.
//		result = add(a,b,c);
//		result2 = sub(a,b,c);
//		System.out.printf("%d,%d \n",result,result2);

	}

}
