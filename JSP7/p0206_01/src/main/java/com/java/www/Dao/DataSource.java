package com.java.www.Dao;

import java.sql.Connection;
import java.sql.DriverManager;

public class DataSource {
	
	private static DataSource instance = null;
	private String driver = "com.mysql.cj.jdbc.Driver";
	private String url = "jdbc:mysql://localhost:3306/jspdb?useUnicode=true&characterEncoding=utf-8";
	private String user = "root";
	private String password = "1234";
	
	// 싱글톤 패턴을 사용하여 인스턴스는 오직 하나만 생성
	private DataSource() throws ClassNotFoundException {
		Class.forName(driver);
	}
	
	// 싱글톤 인스턴스 반환
	public static DataSource getInstance() throws ClassNotFoundException {
		if (instance == null) {
			instance = new DataSource();
		}
		return instance;
	}
	
	// DB 연결 획득
	public Connection getConnection() throws Exception {
		Connection conn = null;
		try {
			conn = DriverManager.getConnection(url, user, password);
			System.out.println("DB 연결 성공");
		} catch (Exception e) {
			System.out.println("DB 연결 실패: " + e.getMessage());
			e.printStackTrace();
		}
		return conn;
	}

}
