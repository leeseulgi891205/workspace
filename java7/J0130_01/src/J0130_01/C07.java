package J0130_01;

import java.io.BufferedWriter;
import java.io.FileWriter;

public class C07 {

	public static void main(String[] args) {
		String filePath = "c:/aaa/a1.txt";
		try {
			// 설정이 되어 있지 않으면 : 덮어쓰기
			FileWriter fw = new FileWriter(filePath,true); // true: 이어쓰기
			BufferedWriter bw = new BufferedWriter(fw);
			String txt = "다시 입력222222!!\r\n";//\r:줄에 제일 끝으로 이동 \n:다음줄로 이동
			bw.write(txt);
			bw.close();
			fw.close();
			System.out.println("파일이 정상적으로 작성되었습니다.");
			
		} catch (Exception e) {
			e.printStackTrace();
			System.out.println("파일 작성 중 오류가 발생했습니다.");
		}
	}

}
