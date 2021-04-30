package com.example.demo.repository;

import java.util.List;

import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;

import com.example.demo.model.Favorite;

@Repository
public interface FavoriteRepository extends JpaRepository<Favorite, Integer> {
	
//	public List<Favorite> findByUser_Id(int id);

}
