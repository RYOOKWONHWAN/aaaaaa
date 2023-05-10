//사용자가 별점 평가를 남길 수 있는 영화 리스트 페이지
import React, { useEffect, useState } from 'react';
import { Button, Modal } from 'reactstrap';
import '../../assets/css/modal.css';
import ReviewModal from './MovieDetailModal';
import axios from 'axios';
import yourImage from '../../assets/img/180c6e128821941b1.jpg';
import { baseUrl } from 'Apiurl';
import { DropdownButton, Dropdown } from 'react-bootstrap';

const ReviewPage = () => {
  const config = {
    headers: {
      "Content-Type": "application/json",
      Authorization: localStorage.getItem("Authorization"),
    },
  };
  const [selectedOption, setSelectedOption] = useState('랜덤영화');
  const [movies, setMovies] = useState([]);
  const [show, setShow] = useState(false);
  const [selectedMovie, setSelectedMovie] = useState(null);

  const handleClose = () => {
    setShow(false);
    setSelectedMovie(null);
  }

  const handleShow = (movie) => {
    setSelectedMovie(movie);
    setShow(true);
  }

  useEffect(() => {
    axios.get('http://localhost:8090/review')
      .then(response => {
        console.log("review")
        setMovies(response.data);
      })
      .catch(error => {
        console.log(error);
      });
  }, []);


  const handleOptionClick = (eventKey) => {
    console.log(eventKey)
    setSelectedOption(eventKey);
    axios
      .post("http://localhost:8090/printmovie", eventKey, config)
      .then((response) => {
        // 영화 목록을 받아와서 처리하는 코드 작성
        console.log("printmovie")
        console.log(response.data)
        setMovies(response.data);
      })
      .catch((error) => {
        console.error(error);
      });
  }

  console.log(movies);

  return (
    <div className="container d-flex justify-content-center align-items-center" style={{ marginTop: '150px', width: '40%' }}>
      <div className="container">
        <header className="my-4">
          <div className="row">
            <div className="col mb-3">
              <h2 className="text-center mb-3">1</h2>
              <p className="text-center">작품을 평가해보세요. 당신의 취향에 딱 맞는 작품을 추천해드릴게요.</p>
            </div>
          </div>
          <DropdownButton id="dropdown-basic-button" title={selectedOption} onSelect={handleOptionClick}>
            <Dropdown.Item eventKey='랜덤영화'>랜덤영화</Dropdown.Item>
            <Dropdown.Item eventKey='드라마'>드라마</Dropdown.Item>
            <Dropdown.Item eventKey='코미디'>코미디</Dropdown.Item>
            <Dropdown.Item eventKey='범죄'>범죄</Dropdown.Item>
            <Dropdown.Item eventKey='로맨스'>로맨스</Dropdown.Item>
            <Dropdown.Item eventKey='액션'>액션</Dropdown.Item>
            <Dropdown.Item eventKey='스릴러'>스릴러</Dropdown.Item>
            <Dropdown.Item eventKey='다큐멘터리'>다큐멘터리</Dropdown.Item>
            <Dropdown.Item eventKey='모험'>모험</Dropdown.Item>
            <Dropdown.Item eventKey='SF'>SF</Dropdown.Item>
            <Dropdown.Item eventKey='애니메이션'>애니메이션</Dropdown.Item>
            <Dropdown.Item eventKey='가족'>가족</Dropdown.Item>
            <Dropdown.Item eventKey='미스터리'>미스터리</Dropdown.Item>
            <Dropdown.Item eventKey='공포'>공포</Dropdown.Item>
            <Dropdown.Item eventKey='판타지'>판타지</Dropdown.Item>
            <Dropdown.Item eventKey='전쟁'>전쟁</Dropdown.Item>
            <Dropdown.Item eventKey='음악'>음악</Dropdown.Item>
            <Dropdown.Item eventKey='서부'>서부</Dropdown.Item>
            <Dropdown.Item eventKey='역사'>역사</Dropdown.Item>
            <Dropdown.Item eventKey='TV 영화'>TV 영화</Dropdown.Item>
          </DropdownButton>
        </header>

        <div className="row" >
          <div className="col">
            <ul className='pl-0'>
              <li className="list-group-item">
                {movies.map((movie) => (
                  <div key={movie.movie_id} className="row align-items-center">
                    <div className="col-3">
                      {movie.poster_path
                        ? <img src={`https://image.tmdb.org/t/p/w200/${movie.poster_path}`} alt="movie" className="img-fluid" />
                        : <img src={yourImage} alt="movie" className="img-fluid" />
                      }
                    </div>
                    <div className="col-9">
                      <h3 className="mb-0">{movie.title}</h3>
                      <div className='mb-3'>{movie.release_date} ・ {movie.country}</div>
                      <Button color="secondary" onClick={() => handleShow(movie)}>
                        자세히 보기
                      </Button>
                      <ReviewModal show={show} handleClose={handleClose} movie={selectedMovie} />
                    </div>
                  </div>
                ))}
              </li>
            </ul>
          </div>
        </div>
      </div>
    </div >
  )
}


export default ReviewPage;
