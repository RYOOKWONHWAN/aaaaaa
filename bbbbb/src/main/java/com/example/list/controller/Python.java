package com.example.list.controller;
import java.io.BufferedReader;
import java.io.ByteArrayOutputStream;
import java.io.IOException;
import java.io.InputStream;
import java.io.InputStreamReader;

public class Python {

	public static void main(String[] args) throws IOException, InterruptedException {
	    // 파이썬 파일 경로 설정
	    String pythonFilePath = "src/main/resources/request.py";

	    // 파이썬 실행 명령어 생성
	    ProcessBuilder processBuilder = new ProcessBuilder();
	    processBuilder.command("python", pythonFilePath);

	    // 파이썬 실행 및 결과값 받아오기
	    Process process = processBuilder.start();
	    process.waitFor(); // 파이썬 프로세스가 종료될 때까지 기다림
	    InputStream inputStream = process.getInputStream();
	    ByteArrayOutputStream resultStream = new ByteArrayOutputStream();
	    byte[] buffer = new byte[1024];
	    int length;
	    while ((length = inputStream.read(buffer)) != -1) {
	        resultStream.write(buffer, 0, length);
	    }
	    String output = resultStream.toString("UTF-8");

	    // 결과값 출력
	    System.out.println(output);
	}

}
