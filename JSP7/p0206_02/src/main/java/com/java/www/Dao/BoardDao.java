package com.java.www.Dao;

import java.sql.Connection;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.util.ArrayList;
import java.util.List;
import javax.sql.DataSource;
import javax.naming.Context;
import javax.naming.InitialContext;
import com.java.www.Dto.BoardDto;

public class BoardDao {
    
    private Connection conn;
    private PreparedStatement pstmt;
    private ResultSet rs;
    private String query;

    public BoardDao() {}

    private Connection getConnection() throws Exception {
        Context context = new InitialContext();
        DataSource ds = (DataSource) context.lookup("java:comp/env/jdbc/Oracle11g");
        return ds.getConnection();
    }

    public List<BoardDto> selectBoardList() {
        List<BoardDto> boardList = new ArrayList<>();
        
        try {
            conn = getConnection();
            query = "SELECT * FROM board ORDER BY bno DESC";
            pstmt = conn.prepareStatement(query);
            rs = pstmt.executeQuery();
            
            while (rs.next()) {
                int bno = rs.getInt("bno");
                String btitle = rs.getString("btitle");
                String bcontent = rs.getString("bcontent");
                String bwriter = rs.getString("bwriter");
                java.sql.Date bdate = rs.getDate("bdate");
                int bhit = rs.getInt("bhit");
                
                BoardDto boardDto = new BoardDto(bno, btitle, bcontent, bwriter, bdate, bhit);
                boardList.add(boardDto);
            }
        } catch (Exception e) {
            e.printStackTrace();
        } finally {
            closeResources(conn, pstmt, rs);
        }
        
        return boardList;
    }

    public List<BoardDto> selectAllBoards() {
        List<BoardDto> boardList = new ArrayList<>();

        try {
            conn = getConnection();
            query = "SELECT * FROM board ORDER BY bno DESC";
            pstmt = conn.prepareStatement(query);
            rs = pstmt.executeQuery();
            
            while (rs.next()) {
                int bno = rs.getInt("bno");
                String btitle = rs.getString("btitle");
                String bcontent = rs.getString("bcontent");
                String bwriter = rs.getString("bwriter");
                java.sql.Date bdate = rs.getDate("bdate");
                int bhit = rs.getInt("bhit");

                BoardDto boardDto = new BoardDto(bno, btitle, bcontent, bwriter, bdate, bhit);
                boardList.add(boardDto);
            }
        } catch (Exception e) {
            e.printStackTrace();
        } finally {
            closeResources(conn, pstmt, rs);
        }

        return boardList;
    }

    private void closeResources(Connection conn, PreparedStatement pstmt, ResultSet rs) {
        try {
            if (rs != null) rs.close();
            if (pstmt != null) pstmt.close();
            if (conn != null) conn.close();
        } catch (SQLException e) {
            e.printStackTrace();
        }
    }
}