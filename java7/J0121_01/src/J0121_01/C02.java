//package J0121_01;
//
//import java.util.Scanner;
//
//public class C02 {
//	
//	public static void main(String[] args) {
//		
//		Scanner scanner = new Scanner(System.in);
//		
		//퀴즈 - 1조123456
		//끝번호 6 - 500원
		//56 - 1,000원
		//456 - 10,000원
		//3456 - 100,000원
		//23456 - 1,000,000원
		//123456 - 10,000,000원
		//6자리를 랜덤으로 복권번호 생성
		// 100000~199999 랜덤번호 생성해서 출력하시오.
		
//		int random=(int)(Math.random()*100000)+100000;
//		String lotto = String.format("%06d", random);
//		System.out.println(lotto);
//		
//		//프로그램을 구현하시오.
//		// 입력번호(000005)와 끝번호가 맞는지 확인해서 맞춤, 틀림 출력하시오.
//		System.out.print("복권번호 6자리를 입력하세요.>>");
//		String input = scanner.next();
//		if (input.length() != 6) {
//			System.out.println("6자리를 입력해야 합니다.");
//			return;
//			}
		
		
//		}
		
//		if(input.charAt(5)==lotto.charAt(5)) {
//			if(input.charAt(4)==lotto.charAt(4)) {
//				if(input.charAt(3)==lotto.charAt(3)) {
//					if(input.charAt(2)==lotto.charAt(2)) {
//						if(input.charAt(1)==lotto.charAt(1)) {
//							if(input.charAt(0)==lotto.charAt(0)) {
//								System.out.println("10,000,000원 당첨");
//							}else {
//								System.out.println("1,000,000원 당첨");
//							}
//						}else {
//							System.out.println("100,000원 당첨");
//						}
//					}else {
//						System.out.println("10,000원 당첨");
//					}
//				}else {
//					System.out.println("1,000원 당첨");
//				}
//			}else {
//				System.out.println("500원 당첨");
//			}
//		}else {
//			System.out.println("꽝! 다음 기회에");
//		}
//		
//	}
//}