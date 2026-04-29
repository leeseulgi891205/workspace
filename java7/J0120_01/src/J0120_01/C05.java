package J0120_01;

import java.util.Scanner;
import java.util.Arrays;

public class C05 {
	
	public static void main(String[] args) {
		Scanner scanner = new Scanner(System.in);
		int[] num = new int[45];
		int[] random = new int[6];
		int[] input = new int[6];
		int[] lotto = new int[6];
		int count = 0; 
		
		// 1. 순차번호 넣기
		for(int i=0;i<num.length;i++) {
			num[i]=i+1;
		}
		// 2. 번호섞기
		for(int i=0;i<1000;i++) {
			int no = (int)(Math.random()*45);
			int temp = num[0];
			num[0] = num[no];
			num[no] = temp;
		}
		// 3. 6개 번호추출
		for(int i=0;i<6;i++) {
			random[i] = num[i];
		}
		
		// 6개의 숫자를 입력하시오.
		for(int i=0;i<6;i++) {
			System.out.printf("%d번째, 1-45까지 숫자를 입력하세요.>>",(i+1));
			input[i] = scanner.nextInt();
		}
		
		// 4. 맞춘 개수 확인 
		for (int i=0;i<6;i++) {
			for(int j=0;j<6;j++) {
				if(random[i]==input[j]) {
					// [핵심 변경 1] i가 아니라 count 방에 차곡차곡 넣습니다.
					lotto[count] = random[i]; 
					count++;
					break;
				}
			}
		}
		
		String str = Arrays.toString(random);
		System.out.println("랜덤번호 : " + str);
		System.out.println("입력번호 : " + Arrays.toString(input));
		
		// [핵심 변경 2] lotto 배열을 0번부터 count 개수만큼만 잘라서 출력
		// 만약 2개를 맞췄다면 배열 앞부분 2개만 출력
		int[] result = Arrays.copyOf(lotto, count); 
		System.out.println("맞춘번호 : " + Arrays.toString(result));
		System.out.println("맞춘번호 개수 : " + count);
	}
}