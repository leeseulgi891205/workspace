package J0121_01;

import java.util.Arrays;

public class C05 {

	public static void main(String[] args) {
//		int[] num = new int[5];
		int[] num = {1,2,3,4,5};
		
		int[] num2 = new int[10]; 
		
		System.out.println(Arrays.toString(num));
		num[2] = 50;
		System.out.println(Arrays.toString(num));
		num[1] = 0; //수정만 가능 - 추가,삭제 불가
		
		System.out.println(Arrays.toString(num));
		
		// 배열생성 -> 배열의 값을 복사
//		for(int i=0;i<num.length;i++) {
//			num2[i] = num[i];
//		}
		
		System.arraycopy(num,0,num2,0,num.length);
		
		System.out.println(Arrays.toString(num2));
	}

}
