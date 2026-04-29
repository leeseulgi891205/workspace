package j0128;

public class C06 {

	public static void main(String[] args) {
		
		SCV s = new SCV();
		
		//-----------------
		Tank t = new Tank();
		System.out.println("현재체력 : "+t.hitPoint);
		// 폭탄 -30 줄어듬.
		System.out.println("폭탄 맞음.");
		t.hitPoint -= 30;
		System.out.println("현재체력 : "+t.hitPoint);
//		System.out.println(m.hitPoint);
		System.out.println("------");
		System.out.println("탱크 충전중");
		s.repair(t); //기계만 수리를 해야 함.
		System.out.println("현재체력 : "+t.hitPoint);
		System.out.println("------");
		
		Marine m = new Marine();
		// 총 -10 줄어듬
		System.out.println("현재체력 : "+m.hitPoint);
		System.out.println("총을 맞음");
		m.hitPoint -= 10;
		System.out.println("현재체력 : "+m.hitPoint);
//		s.repair(m);
		System.out.println("현재체력 : "+m.hitPoint);
	}

}
