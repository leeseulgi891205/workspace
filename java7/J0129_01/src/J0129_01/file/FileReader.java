package J0129_01.file;

import java.io.BufferedReader;
import java.io.FileNotFoundException;
import java.io.IOException;
import java.io.Reader;

public class FileReader extends Reader {
	private String filePath;
	private java.io.FileReader fileReader;
	
	public FileReader(String filePath) throws FileNotFoundException {
		this.filePath = filePath;
		this.fileReader = new java.io.FileReader(filePath);
	}
	
	@Override
	public int read(char[] cbuf, int off, int len) throws IOException {
		return fileReader.read(cbuf, off, len);
	}
	
	@Override
	public void close() throws IOException {
		if (fileReader != null) {
			fileReader.close();
		}
	}
	
	public String getFilePath() {
		return filePath;
	}
}
