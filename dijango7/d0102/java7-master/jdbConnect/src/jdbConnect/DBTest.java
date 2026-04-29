package jdbConnect;

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.PreparedStatement;
import java.sql.ResultSet;

public class DBTest {

	public static void main(String[] args) {
		String url = "jdbc:oracle:thin:@localhost:1521:xe";
        String user = "ora_user";
        String password = "1111";

        try {
            // 드라이버 로딩
            Class.forName("oracle.jdbc.driver.OracleDriver");

            // DB 연결
            Connection conn =
                DriverManager.getConnection(url, user, password);
            String sql = "SELECT * FROM member";
            PreparedStatement pstmt = conn.prepareStatement(sql);
            ResultSet rs = pstmt.executeQuery();
            while (rs.next()) {
            	String id = rs.getString("id");
            	String pw = rs.getString("pw");
            	String name = rs.getString("name");
//              int empno = rs.getInt("employee_id");

                System.out.println(id + " " + pw + " " + name);
            }
            
            System.out.println("Oracle DB 연결 성공!");
            rs.close();
            pstmt.close();
            conn.close();

        } catch (Exception e) {
            e.printStackTrace();
        }


	}

}
