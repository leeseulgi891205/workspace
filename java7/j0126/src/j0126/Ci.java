package j0126;

public class Ci extends Shape {
	Point center; // int x,int y
	int r;
	
	Ci(){ //기본생성자
		this(new Point(0,0),100);
	}
	Ci(Point center,int r){//전체생성자
		this.center = center;
		this.r = r;
	}

}
