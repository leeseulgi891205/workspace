package J0130_01;

import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.BufferedReader;

public class C06 {

    public static void main(String[] args) {
    	
    	// 문서파일 읽어오기 - BufferedReader 객체를 사용해서 진행함.
    	String filePath = "c:/aaa/a1.txt";
    	try {
    	    FileReader fr = new FileReader(filePath);
    	    BufferedReader br = new BufferedReader(fr);
    	    while (true) {
    	        String line = br.readLine();
    	        if (line == null) break;
    	        System.out.println(line);
    	    }
    	    br.close();
    	} catch (Exception e) {
    	    e.printStackTrace();
    	}
    	
    	
    	
    	
    	// FileInputStream ->2byte씩 읽어와서 문자를 출력하는 방식
//        String filePath = "c:/aaa/a1.txt";
//        try {
//            FileInputStream fis = new FileInputStream(filePath);
//            int read = 0;
//            //파일을 읽어옴
//            while ((read = fis.read()) != -1) {
//            	//파일을 출력
//                System.out.print((char) read);
//            }
//            fis.close();
//        } catch (Exception e) {
//            e.printStackTrace();
//            System.out.println("파일이 존재하지 않습니다.");
//        }
    }
}
