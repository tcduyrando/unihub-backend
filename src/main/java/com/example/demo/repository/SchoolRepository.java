package com.example.demo.repository;

import java.util.List;

import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;

import com.example.demo.model.School;

@Repository
public interface SchoolRepository extends JpaRepository<School, Integer> {
	
	public School findByName(String name);
	public List<School> findAllByName(String name);

}
