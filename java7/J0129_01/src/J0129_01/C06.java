package J0129_01;

import java.io.FileInputStream;
import java.io.FileReader;

public class C06 {

	public static void main(String[] args) {
		FileReader fr = null;
		try {
//			fis = new FileInputStream("C:/aaa/a1.txt");//바이트단위
			fr = new FileReader("C:/aaa/a1.txt");//문자단위
			int data = 0;//byte단위
			while((data = fr.read()) != -1) {
				//2byte -> 1char
				System.out.print((char)data);
			}
		} catch (Exception e) {
			e.printStackTrace();
		}
		

	}

}
