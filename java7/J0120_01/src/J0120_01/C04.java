package J0120_01;

import java.util.Scanner;
import java.util.Arrays;

public class C04 {

	public static void main(String[] args) {
		Scanner scanner = new Scanner(System.in);
		
		// 1. 1-45까지의 랜덤번호 생성 및 섞기
		int[] num = new int[45];
		int[] user = new int[6];
		
		// 순차 입력
		for(int i=0; i<num.length; i++) {
			num[i] = i+1;
		}
		System.out.println("순차번호 :"+Arrays.toString(num));
		
		// 섞기 (Shuffle)
		for(int i=0; i<1000; i++) {
			int no = (int)(Math.random()*45); 
			int temp = num[0];
			num[0] = num[no];
			num[no] = temp;
		}
		
		// 2. 사용자 번호 6개 입력받기
		// 1-45번에 아닌 번호를 입력했을때 다시 입력받을 수 있도록 출력하시오.
		System.out.println("번호 6개를 입력하세요.");
		for (int i=0; i<6; i++) {
		System.out.print((i+1)+"번째 번호 입력:");
			int input = scanner.nextInt(); // 입력을 일단 임시 변수에 받음
					
			// 1~45 범위인지 확인
			if(input < 1 || input > 45) {
			System.out.println("1~45 사이의 숫자만 입력하세욧!!!!");
			i--; // 중요: 카운트를 하나 줄여서 다시 입력받게 함
			} else {
			user[i] = input; // 범위가 맞으면 배열에 저장
			}
		}
		
		// 3. 번호 출력
		System.out.println("-------------------------");
		System.out.print("입력한 번호 : "); // 입력한 번호 출력
		for (int i=0; i<6; i++) {
			System.out.print(user[i]+" ");
		}
		System.out.println();
		
		System.out.print("당첨 번호   : "); // 랜덤번호(당첨번호) 출력
		for (int i=0; i<6; i++) {
			System.out.print(num[i]+" ");
		}
		System.out.println();
		System.out.println("-------------------------");
		
	
		// 4. 랜덤숫자 맞은개수 출력
		int count = 0; // 맞은 개수 카운트 변수
		
		for(int i=0; i<6; i++) {          // user 배열 (내 번호)
			for(int j=0; j<6; j++) {      // num 배열 (당첨 번호, 앞 6개만 비교)
				if(user[i] == num[j]) {   // 번호가 같으면
					count++;              // 카운트 증가
					break;                // 찾았으면 더 비교할 필요 없으므로 안쪽 for문 탈출
				}
			}
		}
		
		System.out.println("맞은개수 : " + count);
	}
}