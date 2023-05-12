package com.example.list.dao;

import java.util.List;
import java.util.Map;

import org.apache.ibatis.annotations.Mapper;
import org.springframework.stereotype.Repository;

import com.example.actor.dto.ActorDTO;
import com.example.director.dto.DirectorDTO;
import com.example.genre.dto.GenreDTO;
import com.example.list.dto.ContentsDTO;
import com.example.list.dto.ImagesDTO;
import com.example.list.dto.ListDTO;
import com.example.member.dto.MemberDTO;
import com.example.review.dto.CommentsDTO;
import com.example.review.dto.LikesDTO;
import com.example.review.dto.RatingDTO;
import com.example.review.dto.ReviewDTO;
import com.example.review.dto.ReviewInfoDTO;
import com.example.wish.dto.WishDTO;

@Mapper
@Repository
public interface ListDAO {
	public List<ListDTO> getTopRatedMovies();
	public List<ListDTO> getTopRatedClassic();
	
	//검색 영역
	public List<ListDTO> searchMovies(String query);
	public List<ActorDTO> searchActors(String query);
	public List<DirectorDTO> searchDirectors(String query);
	
	// 배우/감독 정보
	public ActorDTO selectByActorId(String actor_id);
	public DirectorDTO selectByDirId(String dir_id);
	
	//출연 영화
	public List<ListDTO> castMovies(String actor_id);
	
	//감독 영화
	public List<ListDTO> dirMovies(String dir_id);
	
	//전체선택(자동완성 기능)
	public List<String> selectAll();
	
	// 영화 상세 페이지
	public ContentsDTO getMovieById(int movie_id);
	public List<GenreDTO> getGenresByMovieId(int movie_id);
	public List<DirectorDTO> getDirectorsByMovieId(int movie_id);
	public List<ActorDTO> getActorsByMovieId(int movie_id);
	public List<ImagesDTO> getImagesByMovieId(int movie_id);
	public List<ReviewDTO> getReviewsByMovieId(int movie_id);
	public List<ListDTO> getSimilarMovies(int movie_id);
	
	// review > comment, rating
	public void postComment(CommentsDTO comment);
	public void updateComment(CommentsDTO comment);
	public void deleteComment(Map<String, Object> map);
	public void postRating(RatingDTO rating);
	public void updateRating(RatingDTO rating);
	public void deleteRating(Map<String, Object> map);
	public ReviewDTO findReviewById(Map<String, Object> map);
	
	// wish
	public WishDTO findWishById(Map<String, Object> map);
	public void postWish(WishDTO wish);
	public void deleteWish(Map<String, Object> map);
	
	// likes
	public List<LikesDTO> findLikesById(Map<String, Object> map);
	public void postLikes(LikesDTO likes);
	public void incrementLikesById(CommentsDTO comment);
	public void incrementLikesCountById(int member_id);
	
	public void deleteLikes(LikesDTO likes);
	public void decrementLikesById(CommentsDTO comment);
	public void decrementLikesCountById(int member_id);
	
	public void updateGradeById(MemberDTO member);
	public MemberDTO findMemberById(int member_id);
	
	// 신고
	public void commentSpoilerReport(ReviewInfoDTO review);
	public void commentProfanityReport(ReviewInfoDTO review);
	public List<CommentsDTO> checkReported(Map<String, Object> map);
	
	
}
