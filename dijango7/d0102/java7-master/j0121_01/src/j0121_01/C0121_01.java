package j0121_01;

import java.util.Arrays;
import java.util.Scanner;

public class C0121_01 {

	public static void main(String[] args) {
		// [ 1-45까지 로또프로그램 구현 ]
		// 1. 순차번호 넣기
		Scanner scanner = new Scanner(System.in);
		int[] num = new int[45];   // 1-45까지 번호저장
		int[] random = new int[6]; // 당첨로또번호 6개 저장
		int[] input = new int[6];  // 입력번호 6개 저장
		int[] lotto = new int[6];  // 입력한 당첨번호 저장
		int count = 0;             // 당첨번호 개수
		for(int i=0;i<45;i++) {
			num[i] = i+1;
		}
		System.out.println(Arrays.toString(num));
		
		// 2. 번호섞기
		for(int i=0;i<300;i++) {
			int no = (int)(Math.random()*45);
			int temp = num[0];
			num[0] = num[no]; //랜덤번호의 값을 0번방에 입력
			num[no] = temp;
		}
		
		System.out.println(Arrays.toString(num));
		
		// 3. 6개 번호추출
		for(int i=0;i<random.length;i++) {
			random[i] = num[i];
		}
		
		// 4. 6개의 입력번호 저장
		for(int i=0;i<6;i++) {
			System.out.println("1-45까지 번호를 입력하세요.>> ");
			input[i] = scanner.nextInt();
		}
		
		// 5. 입력번호와 당첨번호를 확인
		for(int i=0;i<random.length;i++) {
			for(int j=0;j<input.length;j++) {
				if(random[i]==input[j]) {
					lotto[count] = random[i];
					count++;
					break;
				}
			}
		}
		
		// 6. 모두 출력
		System.out.println("당첨번호 : "+Arrays.toString(random));
		System.out.println("입력번호 : "+Arrays.toString(input));
		System.out.println("당첨된 번호 : "+Arrays.toString(lotto));
		System.out.println("당첨된 개수 : "+count);
		
		

	}

}
