package com.javaDao;

import java.util.List;

import org.apache.ibatis.annotations.Mapper;

import com.java.dto.BoardDto;

// component, ComponentScan, Repository, Service, Controller,Bean
@Mapper // mybatis에서 Dao로 사용할 인터페이스에 붙이는 어노테이션
public interface BoardDao {

	List<BoardDto> SelectAll();

}
