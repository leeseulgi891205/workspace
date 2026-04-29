package com.java.repository;

import java.util.Optional;

import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.data.jpa.repository.Query;
import org.springframework.data.repository.query.Param;

import com.java.dto.MemberDto;

// jpaRepository는 인터페이스로 만들어야 한다. 그리고 JpaRepository를 상속받아야 한다.
// <dto객체, dto객체 primary key타입>
// findAll(), findById(), save(), delete() ,deleteById() ,count()

public interface MemberRepository extends JpaRepository<MemberDto, String> {

	// 로그인 확인 - 1개 데이터 전달 : Optional타입이어야 함.
	Optional<MemberDto> findByIdAndPw(String id, String pw);

	// 로그인 확인
//	@Query(value = "select * from MemberDto where id =? and pw = ?", nativeQuery = true)
//	Optional<MemberDto> selectLogin(String id, String pw);

	// MemberDto 이름을 클래스명과 동일하게 해야함
	@Query("select m from MemberDto m where id =:id and pw =:pw")
	Optional<MemberDto> selectLogin(@Param("id") String id, @Param("pw") String pw);

}
