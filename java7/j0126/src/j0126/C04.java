package j0126;

public class C04 {

	public static void main(String[] args) {
		// 원 그림 점과 반지름이 있으면 그림이 생성
		Ci c1 = new Ci();
		c1.draw(); // 상속받은 변수,메소드는 바로 사용
//		Point p = new Point(5,5);
		Ci c2 = new Ci(new Point(5,5),50);
		c2.draw();
		
		// 삼각형을 그리려면 점이 몇개 필요할까요? 3개
		// 점 3개 - > Point 몇개 필요할까요? 3개
//		Point p1 = new Point(0,0);
//		Point p2 = new Point(10,0);
//		Point p3 = new Point(0,10);
//		
//		Point[] p = {p1,p2,p3};
//		
//		Triangle t1 = new Triangle(new Point(0,0),p2,p3);
//		t1.draw();
//		
//		Triangle t2 = new Triangle(p);
//		t2.draw();
		
		
		
		// 객체선언 : 다른클래스를 클래스내에 사용하려면 객체선언
//		Circle c = new Circle();
//		c.x = 0;
//		c.y = 0;
//		c.r = 10;
		
//		Circle2 cc = new Circle2();
//		cc.x = 0;
//		cc.y = 0;
//		cc.r = 10;
//		cc.z = 0; //없는 변수 사용시 에러
		
//		Circle3 ccc = new Circle3();
////		ccc.x = 0;
//		ccc.p.x = 0;
//		ccc.p.y = 0;
//		ccc.r = 10;
		

	}

}
