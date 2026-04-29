package com.java.repository;

import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;

import com.java.dto.CommentDto;

@Repository
public interface CommentRepository extends JpaRepository<CommentDto, Integer> {
	
}
