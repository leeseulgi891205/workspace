package J0120_01;

import java.util.Scanner;

public class C06 {

	public static void main(String[] args) {
		Scanner scanner = new Scanner(System.in);
		int[] num = new int[45];
		int[] random = new int[6];
		int[] input = new int[6];
		int[] lotto = new int[6];
		int count = 0;
		
		// 1. 순차번호 넣기
		for(int i=0; i<num.length; i++) {
			num[i] = i+1;
			
		}
		// 2. 번호섞기
		for (int i=0; i<10000; i++) {
			int n1 = (int)(Math.random()*45);
			int n2 = (int)(Math.random()*45);
			
			int temp = num[n1];
			num[n1] = num[n2];
			num[n2] = temp;
		}
		
		
		// 3. 6개 번호추출
		for (int i=0; i<6; i++) {
			random[i] = num[i];
		}
		
		
		// 6개의 숫자를 입력하시오.
		for (int i=0; i<6; i++) {
			System.out.printf("%d번째 숫자를 입력하시오.>> ",i+1);
			input[i] = scanner.nextInt();
		}
		
		
		// 4. 맞춘 개수 확인
		for (int i=0; i<6; i++) {
			for (int j=0; j<6; j++) {
				if(random[i]==input[j]) {
					count++;
				}
			}
		}
		// 5. 결과출력
		System.out.print("추출번호: ");
		for (int i=0; i<6; i++) {
			System.out.printf("%d ",random[i]);
		}
		System.out.println();
		

		
		
	}

}
