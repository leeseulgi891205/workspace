package com.java.repository;

import java.util.Optional;

import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.data.jpa.repository.Modifying;
import org.springframework.data.jpa.repository.Query;
import org.springframework.data.repository.query.Param;

import com.java.dto.BoardDto;

public interface BoardRepository extends JpaRepository<BoardDto, Integer> {

	// 답변달기: 기존 답변들의 bstep을 1씩 증가
	@Modifying
	@Query(value = "UPDATE boarddto SET bstep = bstep + 1 WHERE bgroup = :bgroup AND bstep > :bstep", nativeQuery = true)
	void replyBstepUP(@Param("bgroup") int bgroup, @Param("bstep") int bstep);

	// 이전글 가져오기: 하드코딩된 111을 :bno 파라미터로 수정
	@Query(value = "SELECT * FROM boarddto WHERE bno = ( " + "SELECT pre_bno FROM ( "
			+ "SELECT bno, LAG(bno, 1, -1) OVER(ORDER BY bgroup DESC, bstep ASC) AS pre_bno "
			+ "FROM boarddto) WHERE bno = :bno)", nativeQuery = true)
	Optional<BoardDto> findByPre(@Param("bno") Integer bno);

	// 다음글 가져오기: nativeQuery = true 추가 및 파라미터 수정
	@Query(value = "SELECT * FROM boarddto WHERE bno = ( " + "SELECT next_bno FROM ( "
			+ "SELECT bno, LEAD(bno, 1, -1) OVER(ORDER BY bgroup DESC, bstep ASC) AS next_bno "
			+ "FROM boarddto) WHERE bno = :bno)", nativeQuery = true)
	Optional<BoardDto> findByNext(@Param("bno") Integer bno);
}
