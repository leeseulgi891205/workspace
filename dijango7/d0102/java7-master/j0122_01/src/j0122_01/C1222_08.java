package j0122_01;

public class C1222_08 {
	
	static void cal(int kor,int eng,int math,double[] cValue) {
		// 합계,평균을 구해서 전달
		cValue[0] = kor+eng+math;
		cValue[1] = (kor+eng+math)/3.0;
	}
	

	public static void main(String[] args) {
		
		double[] cValue = new double[2];
		
		int kor = 100;
		int eng = 100;
		int math = 99;
		
		// 함수호출후 합계,평균을 구해서 출력하시오.
		cal(kor,eng,math,cValue);
		
		System.out.println(cValue[0]+","+cValue[1]);
		
		
		
		
		

	}

}
