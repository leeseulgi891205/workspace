package J0129_01;

import java.util.Scanner;
import java.util.Random;

public class c0909 {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		Random rd = new Random();

		System.out.println("==== 사다리 타기 게임 ====");
		System.out.print("참여 인원 수를 입력하세요: ");
		int count = sc.nextInt();
		sc.nextLine(); // 버퍼 비우기

		String[] players = new String[count];
		for (int i = 0; i < count; i++) {
			System.out.print((i + 1) + "번 참가자 이름: ");
			players[i] = sc.nextLine();
		}

		// 사다리 생성 (층수는 5층으로 고정)
		int height = 5;
		boolean[][] ladder = new boolean[height][count - 1];

		for (int i = 0; i < height; i++) {
			for (int j = 0; j < count - 1; j++) {
				// 50% 확률로 가로줄 생성
				ladder[i][j] = rd.nextBoolean();
				
				// 가로줄이 연속으로 생기지 않게 방지 (사다리 규칙)
				if (j > 0 && ladder[i][j - 1]) {
					ladder[i][j] = false;
				}
			}
		}

		// 사다리 출력
		System.out.println("\n---- 사다리 모양 ----");
		for (int i = 0; i < height; i++) {
			System.out.print("|");
			for (int j = 0; j < count - 1; j++) {
				if (ladder[i][j]) {
					System.out.print("-|"); // 가로줄 있음
				} else {
					System.out.print(" |"); // 가로줄 없음
				}
			}
			System.out.println();
		}

		// 결과 출력 (이름 출력)
		for (String name : players) {
			System.out.print(name + " ");
		}
		System.out.println("\n======================");
		
		System.out.println("대박 기운이 느껴지네요! 화이팅!");
		
		sc.close();
	}
}