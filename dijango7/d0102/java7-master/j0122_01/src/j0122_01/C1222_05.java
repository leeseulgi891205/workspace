package j0122_01;

public class C1222_05 {

	int aa = 0;        //인스턴스변수 - 객체선언후 참조변수명.변수명.
	static int bb = 0; //클래스변수 - 객체선언없이 클래스명.변수명.
	
//	 void add2(int a,int b) { //인스턴스메소드 - 객체선언후 참조변수명.메소드명
//		System.out.println("합 : "+(a+b));
//	}
	
	static int addSub(int a,int b) {
		int result = a+b;
		int result2 = a-b;
		return result;
//		return result,result2; //리턴값은 1개만 전송가능
	}
	
	static int add(int a,int b) { //클래스 메소드 - 객체선언없이 클래스명.메소드명
		//System.out.println("합 : "+(a+b));
		return a+b;
	}
	
	static int sub(int a,int b) {
		//System.out.println("빼기 : "+(a-b));
		return a-b;
	}
	
	//multi,divide
	static int multi(int a,int b) {
		//System.out.println("곱하기 : "+(a*b));
		return a*b;
	}
	
	static double divide(int a,int b) {
		//System.out.println("나누기 : "+(a/b));
		return a/(double)b;
	}


	
	public static void main(String[] args) {
		int a = 10;
		int b = 3;
		
		int result=0,result2=0,result3=0;
		double result4=0;
		
		// return문 사용
		result = add(a,b);
		result2 = sub(a,b);
		result3 = multi(a,b);
		result4 = divide(a,b);
		System.out.printf("%d,%d,%d,%.2f \n",result,result2,result3,result4);
		
		int[] aArr = {1,2,3};
		System.out.println(aArr);
		Tv t = new Tv();
		System.out.println(t);
		
		
		

		
		
		
		//인스턴스 메소드 사용방법
//		C1222_05 c1 = new C1222_05();
//		c1.add2(a, b);
		
		//클래스 메소드 사용방법 - 같은 클래스 내에는 클래스명 생략가능
//		add(a,b);
//		sub(a,b);
//		multi(a,b);
//		divide(a,b);
		
		
		
		
//		int a = 10;
//		int[] aArr = {1,2,3};
//		
//		System.out.println(a);
//		System.out.println(aArr);
		
		
		
//		C1222_05 c1 = new C1222_05();
//		System.out.println(c1.aa);
//		System.out.println(bb); //같은클래스내에서는 클래스명 생략가능
//		
//		int a = 0; //지역변수 - 메인메소드 내 선언
//		
//		// 흰색,true,7
//		Tv t1 = new Tv();
//		t1.color = "흰색";
//		t1.power = true;
//		t1.channel = 7;
//		// 검정,false,10
//		Tv t2 = new Tv();
//		t2.color = "검정";
//		t2.power = false;
//		t2.channel = 10;

	}

}
