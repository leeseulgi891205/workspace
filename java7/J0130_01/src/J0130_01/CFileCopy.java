package J0130_01;

import java.io.File;
import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.io.FileOutputStream;
import java.io.IOException;
import java.io.OutputStream;
import java.io.InputStream;

public class CFileCopy {
	public static void main(String[] args) {
		//이미지 파일복사
		File f = new File("c:/aaa/nct1.jpg");
		FileInputStream fis = null;
		FileOutputStream fos = null;
		try {
			// 파일 읽어오기
			fis = new FileInputStream(f);
			//파일저장하기
			fos = new FileOutputStream("c:/bbb/nct1.jpg");
			while(true) {
				int read = fis.read();
				if(read==-1) break;
				fos.write(read);
			}
			System.out.println("파일 복사가 완료되었습니다.");
		} catch (FileNotFoundException e) {
			e.printStackTrace();
			System.out.println("파일을 찾을 수 없습니다.");
		} catch (IOException e) {
			e.printStackTrace();
			System.out.println("파일 입출력 오류가 발생했습니다.");
		} finally {
			try {
				if(fis != null) fis.close();
				if(fos != null) fos.close();
			} catch (IOException e) {
				e.printStackTrace();
			}
		}
	}

}
