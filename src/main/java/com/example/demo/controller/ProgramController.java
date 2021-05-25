package com.example.demo.controller;

import java.util.HashMap;
import java.util.List;
import java.util.Map;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.CrossOrigin;
import org.springframework.web.bind.annotation.DeleteMapping;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.PutMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

import com.example.demo.exception.ResourceNotFoundException;
import com.example.demo.model.Program;
import com.example.demo.model.School;
import com.example.demo.repository.ProgramRepository;

@CrossOrigin
@RestController
@RequestMapping("api/v1/")
public class ProgramController {
	
	@Autowired
	private ProgramRepository programRepository;
	
	// get all programs REST API
	@GetMapping("/programs")
	public List<Program> getAllPrograms() {
		return programRepository.findAll();
	}
	
	// create program REST API
	@PostMapping("/programs")
	public Program createProgram(@RequestBody Program program) {
		return programRepository.save(program);
	}
	
	// get program by id REST API
	@GetMapping("/programs/{id}")
	public ResponseEntity<Program> getProgramById(@PathVariable int id) {
		Program program = programRepository.findById(id)
				.orElseThrow(() -> new ResourceNotFoundException("Program with id " + id + "does not exist"));
		return ResponseEntity.ok(program);
	}
	
	// get program by name REST API
//	@GetMapping("/programs/name/{name}")
//	public ResponseEntity<Program> getProgramByName(@PathVariable String name) {
//		Program program = programRepository.findByName(name);
////						.orElseThrow(() -> new ResourceNotFoundException("School with id " + id + "does not exist"));
//		return ResponseEntity.ok(program);
//	}
	
	// get list of programs by name REST API
	@GetMapping("/programs/names/{name}")
	public ResponseEntity<List<Program>> getProgramsByName(@PathVariable String name) {
		List<Program> program = programRepository.findAllByName(name);
//								.orElseThrow(() -> new ResourceNotFoundException("School with id " + id + "does not exist"));
		return ResponseEntity.ok(program);
	}
	
	// get programs by school id REST API
	@GetMapping("/programs/school/{schoolId}")
	public ResponseEntity<List<Program>> getProgramBySchoolId(@PathVariable int schoolId) {
		List<Program> program = programRepository.findBySchoolId(schoolId);
		return ResponseEntity.ok(program);
	}

	// update program REST API
	@PutMapping("/programs/{id}")
	public ResponseEntity<Program> updateProgram(@PathVariable int id, @RequestBody Program programDetails) {
		Program program = programRepository.findById(id)
				.orElseThrow(() -> new ResourceNotFoundException("Program with id " + id + "does not exist"));
		
		program.setName(programDetails.getName());
		program.setSchool(programDetails.getSchool());
		
		Program updatedProgram = programRepository.save(program);
		return ResponseEntity.ok(updatedProgram);
	}
	
	// delete program REST API
	@DeleteMapping("/programs/{id}")
	public ResponseEntity<Map<String, Boolean>> deleteProgram(@PathVariable int id) {
		Program program = programRepository.findById(id)
				.orElseThrow(() -> new ResourceNotFoundException("Program with id " + id + "does not exist"));
		
		programRepository.delete(program);
		Map<String, Boolean> response = new HashMap<>();
		response.put("deleted", Boolean.TRUE);
		return ResponseEntity.ok(response);
	}
	
}
