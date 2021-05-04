package com.example.demo.repository;

import java.util.List;

import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;

import com.example.demo.model.Favorite;
import com.example.demo.model.User;

@Repository
public interface FavoriteRepository extends JpaRepository<Favorite, Integer> {
	
	public List<Favorite> findByUser(User user);
	public List<Favorite> findByUserId(int id);

}
