package J0123_01;

public class Car {
	
	Car(){
		this.color = "white"; // 다른 생성자에서 다른 생성자를 호출(this)
	}
		
	
	// 매개변수가 있는 생성자
	Car(String c, String g, int d){ // 매개변수 생성자
		color = c;
		gearType = g;
		door = d;
	}
	
	String color;
	String gearType;
	int door;
	// red,stick,4
	// grene,auto,5
	// gray,stick,3
	// blue,auto,6
	
	
	

}
