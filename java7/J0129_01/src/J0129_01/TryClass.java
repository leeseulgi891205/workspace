package J0129_01; // 패키지- 없으면 에러, 없으면 자동생성

public class TryClass{ //없으면 자동 생성(Object상속) - 11개메소드 자동생성
	public static void main(String[] args) throws Exception {
		
		//기본생성자 - 없으면 에러 , 없으면 자동생성
		TryClass(){
			super(); //자동생성 - 부모생성자호출
		}
		
		
		// equals(),toString(), hashCode()...11개메소드 자동생성
		
	
	void method() throws Exception {
		System.out.println(1);
		System.out.println(2);
		System.out.println(3);
		System.out.println(0/0);//에러
		System.out.println(4);
		System.out.println(5);
	}
}
