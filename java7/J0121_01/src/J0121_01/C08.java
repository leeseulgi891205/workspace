package J0121_01;

import java.util.Scanner;
import java.util.Arrays;

public class C08 {
	
	public static void main(String[] args) {
		Scanner scanner = new Scanner(System.in);
		
		// 1-45 랜덤번호 6개를 추출해서
		// 입력받은 6개 숫자와 몇개 맞는지 출력하시오.
		// 로또번호:
		// 입력번호:
		// 당첨된번호:
		// 당첨개수:
		// 당첨금액:
		int[] num = new int[45];	// 1-45까지 번호
		int[] random = new int[6];	// 랜덤으로 뽑힌 6개 번호
		int[] input = new int[6];	// 사용자가 입력한 6개 번호
		int[] lotto = new int[6];	// 입력한번호와 당첨번호가 같은경우 저장
		int count = 0; 			    // 당첨번호 개수
		int money = 0;				// 당첨금액
		

		
		// 1. 순차번호 넣기
		for(int i=0;i<num.length;i++) {	// 0-44
			num[i]=i+1;	// 1-45
		}
		// 2. 번호섞기
		for(int i=0;i<1000;i++) { // 300번 섞기
			int no = (int)(Math.random()*45); // 0-44
			int temp = num[0];	// 임시저장
			num[0] = num[no];	// 랜덤번호의 값을 0번방에 입력
			num[no] = temp;	// 랜덤번호에 임시저장값 입력
		}
		// 3. 6개 번호추출
		for(int i=0;i<6;i++) {	// 0-5
			random[i] = num[i];	// 섞인 번호의 앞에서 6개 추출
		}
		
		// 4. 6개의 숫자를 입력하시오.
		for(int i=0;i<6;i++) {	// 0-5
			System.out.printf("%d번째: 1부터45번까지 숫자를 입력해주세요.>> ", (i+1));	// i는 0부터 시작하므로 +1
			input[i] = scanner.nextInt();	// 입력받은 숫자 저장
		}
		
		// 5. 맞춘 개수 확인 
		for (int i=0;i<6;i++) {	// 0-5
			for(int j=0;j<6;j++) { 	// 0-5
				if(random[i]==input[j]) { 	// 번호가 일치하면
					lotto[count] = random[i]; // 맞춘번호 저장
					count++;	// 맞춘개수 증가
					break;	// 중복체크 방지
				}
			}
		}
		
		// 6. 당첨금 계산 
		int[] num2 = {0,5000,10000,50000,1000000,20000000,1000000000}; 	// 당첨금 배열
		for(int i=0;i<num2.length;i++) { 	// 0-6
			if(count == i) {	// 맞춘개수와 인덱스가 같으면
				money = num2[i];	// 당첨금 저장
				break;	// 종료
			}
		}
		
		String str = Arrays.toString(random);	// 배열을 문자열로 변환
		System.out.println("랜덤번호 : "+str);	// 랜덤번호 출력
		System.out.println("입력번호 : "+Arrays.toString(input));	// 입력번호 출력
		
		int[] result = Arrays.copyOf(lotto,count); 	// 맞춘번호만 복사
		System.out.println("맞춘번호 : " + Arrays.toString(result)); // 맞춘번호 출력
		System.out.println("맞춘번호 개수 : "+count);		// 맞춘개수 출력
		System.out.println("당첨금 : "+String.format("%,d",money)+"원"); // 당첨금 출력 (천단위 콤마포함)
	}
}
