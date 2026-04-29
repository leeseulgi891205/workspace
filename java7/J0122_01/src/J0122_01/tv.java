package J0122_01;

public class tv {
	
	String color;	// 색상
	boolean power;	// 전원상태
	int channel;	// 채널
	void power() {	// TV 전원 켜기/끄기
		power = !power;}	// 토글
	void channelUp() {	// 채널 올리기
		channel++;}
	void channelDown() {	// 채널 내리기
		channel--;}
	
}
