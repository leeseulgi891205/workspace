package J0121_01;

import java.util.Arrays;
import java.util.Scanner;

public class C01 {

	public static void main(String[] args) {
		Scanner scanner = new Scanner(System.in);
		// [ 1-45까지 로또프로그램 구현 ]
		// 1. 순차번호 넣기
		// 1,2,3
		int[] num = new int[45];	// 1-45까지 번호
		int[] random = new int[6]; // 랜덤으로 뽑힌 6개 번호
		int[] input = new int[6]; // 사용자가 입력한 6개 번호
		int[] lotto = new int[6]; // 입력한번호와 당첨번호가 같은경우 저장
		int count = 0; 			  // 당첨번호 개수
		for(int i=0;i<45;i++) {
			num[i] = i+1;
		}
		
		System.out.println(Arrays.toString(num));
		
		// 2. 번호섞기
		for(int i=0;i<300;i++) {
			int no = (int)(Math.random()*45); //0-44
			int temp = num[0];
			num[0] = num[no]; // 랜덤번호의 값을 0번방에 입력
			num[no] = temp;
		}
		
		// 3. 6개 번호추출
		for(int i=0;i<random.length;i++){
			random[i] = num[i];
			
		}
		System.out.println(Arrays.toString(random));
		// 4. 6개의 입력숫자 저장
		for(int i=0;i<6;i++) {
			System.out.printf("%d번째, 1-45까지 번호를 입력하세요>> \n",i+1);
			input[i] = scanner.nextInt();
		}
		// 5. 입력번호와 당첨번호를 확인
		for(int i=0;i<6;i++) {
			for(int j=0;j<6;j++) {
				if(random[i]==input[j]) {
					lotto[count] = input[j];
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
