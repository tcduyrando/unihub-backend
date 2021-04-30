package com.example.demo.model;

import java.util.ArrayList;
import java.util.List;

import javax.persistence.CascadeType;
import javax.persistence.Column;
import javax.persistence.Entity;
import javax.persistence.GeneratedValue;
import javax.persistence.GenerationType;
import javax.persistence.Id;
import javax.persistence.JoinColumn;
import javax.persistence.OneToMany;
import javax.persistence.Table;

@Entity
@Table(name = "schools")

public class School {
	
	@Id
	@GeneratedValue(strategy = GenerationType.IDENTITY)
	private int id;
	
	@Column(name = "name")
	private String name;
	
	@Column(name = "email")
	private String email;
	
	@Column(name = "phone")
	private String phone;
	
	@Column(name = "country")
	private String country;
	
	@Column(name = "location")
	private String location;
	
	@Column(name = "admissionWeb")
	private String admissionWeb;
	
	@Column(name = "tuitionUSD")
	private int tuitionUSD;
	
	@Column(name = "tuition")
	private String tuition;
	
	@Column(name = "website")
	private String website;
	
	@Column(name = "logoURL")
	private String logoURL;
	
	@Column(name = "imageURL")
	private String imageURL;
	
	@Column(name = "score_ielts")
	private float score_ielts;
	
	@Column(name = "score_toefl")
	private int score_toefl;
	
	@Column(name = "score_sat")
	private int score_sat;
	
	public School() {
		
	}
	public School(String name, String email, String phone, String country, String location, String admissionWeb,
			int tuitionUSD, String tuition, String website, String logoURL, String imageURL, float score_ielts,
			int score_toefl, int score_sat) {
		super();
		this.name = name;
		this.email = email;
		this.phone = phone;
		this.country = country;
		this.location = location;
		this.admissionWeb = admissionWeb;
		this.tuitionUSD = tuitionUSD;
		this.tuition = tuition;
		this.website = website;
		this.logoURL = logoURL;
		this.imageURL = imageURL;
		this.score_ielts = score_ielts;
		this.score_toefl = score_toefl;
		this.score_sat = score_sat;
	}

	public int getId() {
		return id;
	}
	public void setId(int id) {
		this.id = id;
	}
	public String getName() {
		return name;
	}
	public void setName(String name) {
		this.name = name;
	}
	public String getEmail() {
		return email;
	}
	public void setEmail(String email) {
		this.email = email;
	}
	public String getPhone() {
		return phone;
	}
	public void setPhone(String phone) {
		this.phone = phone;
	}
	public String getCountry() {
		return country;
	}
	public void setCountry(String country) {
		this.country = country;
	}
	public String getLocation() {
		return location;
	}
	public void setLocation(String location) {
		this.location = location;
	}
	public String getAdmissionWeb() {
		return admissionWeb;
	}
	public void setAdmissionWeb(String admissionWeb) {
		this.admissionWeb = admissionWeb;
	}
	public int getTuitionUSD() {
		return tuitionUSD;
	}
	public void setTuitionUSD(int tuitionUSD) {
		this.tuitionUSD = tuitionUSD;
	}
	public String getTuition() {
		return tuition;
	}
	public void setTuition(String tuition) {
		this.tuition = tuition;
	}
	public String getWebsite() {
		return website;
	}
	public void setWebsite(String website) {
		this.website = website;
	}
	public String getLogoURL() {
		return logoURL;
	}
	public void setLogoURL(String logoURL) {
		this.logoURL = logoURL;
	}
	public String getImageURL() {
		return imageURL;
	}
	public void setImageURL(String imageURL) {
		this.imageURL = imageURL;
	}
	public float getScore_ielts() {
		return score_ielts;
	}
	public void setScore_ielts(float score_ielts) {
		this.score_ielts = score_ielts;
	}
	public int getScore_toefl() {
		return score_toefl;
	}
	public void setScore_toefl(int score_toefl) {
		this.score_toefl = score_toefl;
	}
	public int getScore_sat() {
		return score_sat;
	}
	public void setScore_sat(int score_sat) {
		this.score_sat = score_sat;
	}

}
