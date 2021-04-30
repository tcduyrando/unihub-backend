package com.example.demo.controller;

import java.util.HashMap;
import java.util.List;
import java.util.Map;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.DeleteMapping;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.PutMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

import com.example.demo.exception.ResourceNotFoundException;
import com.example.demo.model.School;
import com.example.demo.repository.SchoolRepository;

@RestController
@RequestMapping("api/v1/")
public class SchoolController {
	
	@Autowired
	private SchoolRepository schoolRepository;
	
	// get all schools REST API
	@GetMapping("/schools")
	public List<School> getAllSchools() {
		return schoolRepository.findAll();
	}
	
	// create school REST API
	@PostMapping("/schools")
	public School createSchool(@RequestBody School school) {
		return schoolRepository.save(school);
	}
	
	// get school by id REST API
	@GetMapping("/schools/{id}")
	public ResponseEntity<School> getSchoolById(@PathVariable int id) {
		School school = schoolRepository.findById(id)
				.orElseThrow(() -> new ResourceNotFoundException("School with id " + id + "does not exist"));
		return ResponseEntity.ok(school);
	}
	
	// update school REST API
	@PutMapping("/schools/{id}")
	public ResponseEntity<School> updateSchool(@PathVariable int id, @RequestBody School schoolDetails) {
		School school = schoolRepository.findById(id)
				.orElseThrow(() -> new ResourceNotFoundException("School with id " + id + "does not exist"));
		
		school.setName(schoolDetails.getName());
		school.setEmail(schoolDetails.getEmail());
		school.setPhone(schoolDetails.getPhone());
		school.setCountry(schoolDetails.getCountry());
		school.setLocation(schoolDetails.getLocation());
		school.setAdmissionWeb(schoolDetails.getAdmissionWeb());
		school.setTuitionUSD(schoolDetails.getTuitionUSD());
		school.setTuition(schoolDetails.getTuition());
		school.setWebsite(schoolDetails.getWebsite());
		school.setLogoURL(schoolDetails.getLogoURL());
		school.setImageURL(schoolDetails.getImageURL());
		school.setScore_ielts(schoolDetails.getScore_ielts());
		school.setScore_toefl(schoolDetails.getScore_toefl());
		school.setScore_sat(schoolDetails.getScore_sat());
		
		School updatedSchool = schoolRepository.save(school);
		return ResponseEntity.ok(updatedSchool);
	}
	
	// delete school REST API
	@DeleteMapping("/schools/{id}")
	public ResponseEntity<Map<String, Boolean>> deleteSchool(@PathVariable int id) {
		School school = schoolRepository.findById(id)
				.orElseThrow(() -> new ResourceNotFoundException("School with id " + id + "does not exist"));
		
		schoolRepository.delete(school);
		Map<String, Boolean> response = new HashMap<>();
		response.put("deleted", Boolean.TRUE);
		return ResponseEntity.ok(response);
	}
	
	
	
	
}
