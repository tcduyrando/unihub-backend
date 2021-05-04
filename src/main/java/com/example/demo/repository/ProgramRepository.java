package com.example.demo.repository;

import java.util.List;

import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;

import com.example.demo.model.Program;
import com.example.demo.model.School;

@Repository
public interface ProgramRepository extends JpaRepository<Program, Integer> {
	
	public List<Program> findBySchool(School school);
	public List<Program> findBySchoolId(int id);
	public List<Program> findByName(String name);

}
