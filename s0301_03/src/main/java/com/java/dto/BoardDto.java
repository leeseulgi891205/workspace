package com.java.dto;

import java.sql.Timestamp;

import org.hibernate.annotations.ColumnDefault;
import org.hibernate.annotations.CreationTimestamp;

import jakarta.persistence.Column;
import jakarta.persistence.Entity;
import jakarta.persistence.FetchType;
import jakarta.persistence.GeneratedValue;
import jakarta.persistence.Id;
import jakarta.persistence.JoinColumn;
import jakarta.persistence.Lob;
import jakarta.persistence.ManyToOne;
import jakarta.persistence.SequenceGenerator;
import lombok.AllArgsConstructor;
import lombok.Builder;
import lombok.Data;
import lombok.NoArgsConstructor;

//@GeneratedValue(strategy = GenerationType.SEQUENCE, generator = "boardDto_seq_generater") // 오라클 시퀀스
@SequenceGenerator( // boardDto 100개 게시글을 할당
		name = "boardDto_seq_generater", // 제너레이터 이름
		sequenceName = "boardDto_seq", // 오라클테이블에서 시퀀스 이름
		initialValue = 101, // 시작번호
		allocationSize = 1 // 메모리 할당범위
)

@Builder
@AllArgsConstructor
@NoArgsConstructor
@Data
@Entity
public class BoardDto {
//	@GeneratedValue(strategy = GenerationType.IDENTITY) // db 시퀀스
//	@GeneratedValue(strategy = GenerationType.SEQUENCE, generator = "boardDto_seq") // 오라클 시퀀스
	@GeneratedValue(generator = "boardDto_seq_generater")
	@Id
	private Integer bno;
	@Column(length = 1000, nullable = false)
	private String btitle;
	@Lob // 대용량 데이터 - CLOB -> 4GB
	private String bcontent;

//	private String id; // member Primary Key -> Foreign Key 사용
//	@ManyToMany // 1명의 회원이 여러 게시글 작성 가능, 1개의 게시글에 여러 회원 작성 가능
//	@OneToMany // 1개의 게시글에 여러 댓글 작성 가능
	// 연관관계가 형성이 됨 - Foreign Key를 구성하게 됨.
	@ManyToOne(fetch = FetchType.EAGER) // 1명의 회원이 여러 게시글 작성 가능
	@JoinColumn(name = "id") // db에 저장되는 컬럼은 id
	private MemberDto memberDto;
	@Column
	private int bgroup;
	@ColumnDefault("0")
	private int bstep;
	@ColumnDefault("0")
	private int bindent;
	@ColumnDefault("0")
	private int bhit;
	@Column(length = 100)
	private String bfile;
	@CreationTimestamp
	private Timestamp bdate;

}
