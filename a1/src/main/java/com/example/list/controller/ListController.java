package com.example.list.controller;

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
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.RestController;

import com.example.list.dto.ContentsDTO;
import com.example.list.service.ListService;
import com.example.review.dto.CommentsDTO;
import com.example.review.dto.LikesDTO;
import com.example.review.dto.RatingDTO;
import com.example.review.dto.ReviewDTO;
import com.example.review.dto.ReviewInfoDTO;
import com.example.wish.dto.WishDTO;

@CrossOrigin({"http://localhost:3000"})
@RestController
public class ListController {
	
	@Autowired
	private ListService listService;
	
	public ListController() {
		
	}
	
	// 메인 리스트
	// http://localhost:8090/
	@GetMapping("/")
	public Map<String, Object> listExecute() {
		Map<String, Object> map = new HashMap<>();
		map.put("topRatedList", listService.getTopRatedMoviesProcess());
		map.put("topRatedClassic", listService.getTopRatedClassicProcess());
		
		return map;
	}
	
	
	// 영화 상세정보
	@GetMapping("/contents/{movie_id}")
	public ContentsDTO contentsExecute(@PathVariable("movie_id") int movie_id) {
		return listService.getContentsProcess(movie_id);
	}
	
	
	
	// 코멘트, 별점 작성
	@PostMapping("/comment")
	public void postCommentExecute(@RequestBody CommentsDTO comment) {
		listService.postCommentProcess(comment);
	}
	
	@PutMapping("/comment")
	public void updateCommentExecute(@RequestBody CommentsDTO comment) {
		listService.updateCommentProcess(comment);
	}
	
	@DeleteMapping("/comment/{movie_id}/{member_id}")
	public void deleteCommentExecute(@PathVariable("movie_id") int movie_id, @PathVariable("member_id") int member_id) {
		listService.deleteCommentProcess(movie_id, member_id);
	}
	
	@PostMapping("/rating")
	public void postRatingExecute(@RequestBody RatingDTO rating) {
		listService.postRatingProcess(rating);
	}
	
	@PutMapping("/rating")
	public void updateRatingExecute(@RequestBody RatingDTO rating) {
		listService.updateRatingProcess(rating);
	}
	
	@DeleteMapping("/rating/{movie_id}/{member_id}")
	public void deleteRatingExecute(@PathVariable("movie_id") int movie_id, @PathVariable("member_id") int member_id) {
		listService.deleteRatingProcess(movie_id, member_id);
	}
	
	@GetMapping("/comment/{movie_id}/{member_id}")
	public ReviewDTO getCommentExecute(@PathVariable("movie_id") int movie_id, @PathVariable("member_id") int member_id) {
		System.out.println("리뷰썼냐" + movie_id);
		return listService.findReviewByIdProcess(movie_id, member_id);
	}
		
	

	// 보고싶어요
	@PostMapping("/wish")
	public void postWishExecute(@RequestBody WishDTO wish) {
		listService.postWishProcess(wish);
	}
	
	@DeleteMapping("/wish/{movie_id}/{member_id}")
	public void deleteWishExecute(@PathVariable("movie_id") int movie_id, @PathVariable("member_id") int member_id) {
		listService.deleteWishProcess(movie_id, member_id);
	}
	
	@GetMapping("/wish/{movie_id}/{member_id}")
	public WishDTO getWishExecute(@PathVariable("movie_id") int movie_id, @PathVariable("member_id") int member_id) {
		System.out.println("보고싶어요" + movie_id);
		return listService.findWishByIdProcess(movie_id, member_id);
	}
	
	
	
	// 코멘트 > 좋아요
	@GetMapping("/likes/{movie_id}/{member_id}")
	public List<LikesDTO> getLikesExecute(@PathVariable("movie_id") int movie_id, @PathVariable("member_id") int member_id) {
		System.out.println("멤버아이디" + member_id);
		System.out.println("좋아요" + listService.findLikesByIdProcess(movie_id, member_id));
		return listService.findLikesByIdProcess(movie_id, member_id);
	}
	
	@PostMapping("/likes")
	public void postLikesExecute(@RequestBody LikesDTO likes) {
		listService.postLikesProcess(likes);
	}
	
	@DeleteMapping("/likes")
	public void deleteLikesExecute(@RequestBody LikesDTO likes) {
		listService.deleteLikesProcess(likes);
	}
	
	
	
	// 신고
	@PutMapping("/spoiler")
	public void commentSpoilerReportExecute(@RequestBody ReviewInfoDTO review) {
		listService.commentSpoilerReport(review);
	}
	
	@PutMapping("/profanity")
	public void commentProfanityReportExecute(@RequestBody ReviewInfoDTO review) {
		listService.commentProfanityReport(review);
	}
	
	@GetMapping("/checkReported/{movie_id}/{member_id}")
	public ResponseEntity<Map<String, Boolean>> checkReportedExecute(@PathVariable("movie_id") int movie_id, @PathVariable("member_id") int member_id) {
		List<CommentsDTO> comment = listService.checkReported(movie_id, member_id);
		System.out.println(comment);
		boolean isReported = !comment.isEmpty();
		
		Map<String, Boolean> response = new HashMap<>();
		response.put("isReported", isReported);
		
		return ResponseEntity.ok(response);
	}
	
	
	
}
