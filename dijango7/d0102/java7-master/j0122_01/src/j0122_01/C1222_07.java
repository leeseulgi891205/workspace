package j0122_01;

public class C1222_07 {
	
//	static void change(int[] a) {
//		a[0] = 1000;
//		System.out.println("change a : "+a[0]);
//	}
	
	static void change(int a,int b,int c,AA aObj) {
		aObj.result = a+b+c;
		aObj.result2 = a-b-c;
		aObj.result3 = a*b*c;
		aObj.result4 = a/b/c;
	}

	public static void main(String[] args) {
		
		AA aObj = new AA();
		int a = 10;
		int b = 3;
		int c = 2;
		
		System.out.print("초기값 : ");
		System.out.printf("%d,%d,%d,%.2f\n",aObj.result,aObj.result2,aObj.result3,aObj.result4);
		change(a,b,c,aObj);
		
		System.out.print("결과값 : ");
		System.out.printf("%d,%d,%d,%.2f\n",aObj.result,aObj.result2,aObj.result3,aObj.result4);
		
		// aObj -> result,result2,result3,result4
		// 더하기값,빼기값,곱하기값,나누기값을 입력받아
		// 출력하시오.
		
		
		
		// 매개변수가 참조형변수로 전달될때는 값이 변경됨.
//		int[] a = {50};
//		System.out.println("1번째 : "+a[0]);
//		//함수호출
//		change(a); //참조형변수
//		//함수호출후 결과값
//		System.out.println("함수호출후 값 : "+a[0]);
		
		
		
		
		// 매개변수가 기본형변수로 전달될때는 값이 변경되지 않음.
//		int a = 50;
//		System.out.println("1번째 : "+a);
//		//함수호출
//		change(a); //기본형변수
//		
//		//함수호출후 결과값
//		System.out.println("함수호출후 값 : "+a);

	}

}
