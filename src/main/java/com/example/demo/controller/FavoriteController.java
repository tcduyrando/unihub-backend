package com.example.demo.controller;

import java.util.HashMap;
import java.util.List;
import java.util.Map;

import org.hibernate.SQLQuery;

//import org.hibernate.query.Query;

//import org.hibernate.Query;

//import javax.persistence.Query;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.data.jpa.repository.Query;
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
import com.example.demo.model.Favorite;
import com.example.demo.repository.FavoriteRepository;

@RestController
@RequestMapping("api/v1/")
public class FavoriteController {
	
	@Autowired
	private FavoriteRepository favoriteRepository;
	
	// get all favorites REST API
	@GetMapping("/favorites")
	public List<Favorite> getAllFavorites() {
		return favoriteRepository.findAll();
	}
	
	// create favorite REST API
	@PostMapping("/favorites")
	public Favorite createFavorite(@RequestBody Favorite favorite) {
		return favoriteRepository.save(favorite);
	}
	
	// get favorite by id REST API
	@GetMapping("/favorites/{id}")
	public ResponseEntity<Favorite> getFavoriteById(@PathVariable int id) {
		Favorite favorite = favoriteRepository.findById(id)
				.orElseThrow(() -> new ResourceNotFoundException("Favorite with id " + id + "does not exist"));
		return ResponseEntity.ok(favorite);
	}
	
	// get favorite by user id REST API
	@GetMapping("/favorites/user/{userId}")
	public ResponseEntity<List<Favorite>> getFavoriteByUser(@PathVariable int userId) {
		List<Favorite> favorite = favoriteRepository.findByUserId(userId);
		return ResponseEntity.ok(favorite);
	}

	
	// update favorite REST API
	@PutMapping("/favorites/{id}")
	public ResponseEntity<Favorite> updateFavorite(@PathVariable int id, @RequestBody Favorite favoriteDetails) {
		Favorite favorite = favoriteRepository.findById(id)
				.orElseThrow(() -> new ResourceNotFoundException("Favorite with id " + id + "does not exist"));
		
		favorite.setUser(favoriteDetails.getUser());
		favorite.setSchool(favoriteDetails.getSchool());
		
		Favorite updatedFavorite = favoriteRepository.save(favorite);
		return ResponseEntity.ok(updatedFavorite);
	}
	
	// delete favorite REST API
	@DeleteMapping("/favorites/{id}")
	public ResponseEntity<Map<String, Boolean>> deleteFavorite(@PathVariable int id) {
		Favorite favorite = favoriteRepository.findById(id)
				.orElseThrow(() -> new ResourceNotFoundException("Favorite with id " + id + "does not exist"));
		
		favoriteRepository.delete(favorite);
		Map<String, Boolean> response = new HashMap<>();
		response.put("deleted", Boolean.TRUE);
		return ResponseEntity.ok(response);
	}

}
