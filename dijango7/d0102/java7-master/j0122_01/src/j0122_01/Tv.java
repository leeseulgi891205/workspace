package j0122_01;

public class Tv {

	String color;  //인스턴스변수
	boolean power;
	int channel;
	void power() {power = !power;}
	void channelUp() {channel++;}
	void channelDown() {channel--;}
}
