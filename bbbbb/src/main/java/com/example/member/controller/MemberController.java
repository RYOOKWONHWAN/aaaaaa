package com.example.member.controller;

import java.util.ArrayList;
import java.util.List;
import java.util.Map;
import java.util.UUID;

import javax.servlet.http.HttpServletRequest;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.security.crypto.bcrypt.BCryptPasswordEncoder;
import org.springframework.web.bind.annotation.CrossOrigin;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.RestController;
import org.springframework.web.multipart.MultipartFile;

import com.example.member.dto.AuthInfo;
import com.example.member.dto.MemberDTO;
import com.example.member.dto.MemberGenreDTO;
import com.example.member.service.MemberService;
import com.example.common.file.FileUpload;
import com.example.list.dto.ListDTO;


@CrossOrigin("*")
@RestController
public class MemberController {
	
	@Autowired
	private MemberService memberService;
	
	@Autowired
	private BCryptPasswordEncoder encodePassword;
	
	// 회원가입 처리
	// @RequestBody첨부파일이 없는 경우 붙이고 있는 경우에는 붙이지 않는다. (json으로 내보내므로 필요)
	@PostMapping("/register")
	public String addMember(@RequestBody MemberDTO memberDTO) {
		System.out.println("요청");
		System.out.println(memberDTO.getEmail());
		System.out.println(memberDTO.getVisibility());
		
		if(memberDTO.getGender() == 0) {
			memberDTO.setGender(1);
		} //리액트에서 디폴트값으로 gender값을 0을 보냈을때 강제로 gender값을 1로 변경해서 db저장함
		
		memberDTO.setPassword(encodePassword.encode(memberDTO.getPassword()));

		AuthInfo authInfo = memberService.addMemberProcess(memberDTO);
		return null;
	}
	
	@PostMapping("/emailcheck")
	public int checkEmail(@RequestBody Map<String, String> requestBody) {		
		String a = requestBody.get("email");
		System.out.println("emailcheck실행");
		System.out.println(a);
		int count = memberService.idcheckprocess(a);
		System.out.println(count);
		
	    return count;
	}
	

	// 회원정보 가져오기
	@GetMapping("/member/editinfo/{email}")
	public MemberDTO getMember(@PathVariable("email") String email) {
		return memberService.updateMemberProcess(email);
	}

	// 회원정보 수정 처리
	@PostMapping("/profile/update")
	public void updateMember(@RequestBody MemberDTO memberDTO, HttpServletRequest request) {
//		UUID uuid = FileUpload.saveCopyFile(file, FileUpload.urlPath(request));
//		memberDTO.setProfile_path(uuid + "_" + file.getOriginalFilename());
		System.out.println(memberDTO.getPassword());
		memberDTO.setPassword(encodePassword.encode(memberDTO.getPassword()));
//		memberDTO.setNickname(memberDTO.getNickname());
//		System.out.println(memberDTO.getProfile_path());
		memberService.updateMemberProcess(memberDTO);
	}
	
	@PostMapping("/profile/imgUpdate")
	public void updateprofileImg(@RequestParam("file") MultipartFile file, @RequestParam("email") String email, HttpServletRequest request) {
		System.out.println("Hello World");
		UUID uuid = FileUpload.saveCopyFile(file, FileUpload.urlPath(request));
	    System.out.println(uuid);
	    System.out.println(email);
	    MemberDTO member = memberService.selectByEmailProcess(email);
	    member.setProfile_path(uuid + "_" + file.getOriginalFilename());
	    System.out.println(member.getProfile_path());
	    System.out.println(member.getEmail());
	    memberService.updateProfileImgProcess(member);
	};
	
	// 회원가입 > 장르선택
	@PostMapping("/genreselect")
	public String addMember(@RequestBody MemberGenreDTO memberGenreDTO) {
		int memberId = memberGenreDTO.getMemberId();
		List<Integer> selectedGenre = memberGenreDTO.getSelectedGenre();

		MemberGenreDTO dto = new MemberGenreDTO();

		for (int tagValue : selectedGenre) {
			dto.setMemberId(memberId);
			dto.setGenreId(tagValue);
			System.out.println(tagValue);
			System.out.println(memberId);
			memberService.insertMemGenreProcess(dto);
		}
		return null;
	}
	
	// 마이페이지 > 평가하기
	@GetMapping("/review")
	public List<ListDTO> printRandom() {
		System.out.println("요청 들어옴");
		List<ListDTO> aList= memberService.randomService();
		System.out.println(aList.size());
		return aList; 
	}
	
	
	
}
