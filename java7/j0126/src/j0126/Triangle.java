package j0126;

public class Triangle extends Shape {
	// 점3개
	Point[] p;
	
	Triangle(){}
	//생성자-3개 점을 배열로 받아 선언
	Triangle(Point[] p){
		this.p = p;
	}
	
	//생성자 - 3개 점을 개별로 받아 선언
	Triangle(Point p1,Point p2,Point p3){
		p = new Point[] {p1,p2,p3};
	}
	
	

}
