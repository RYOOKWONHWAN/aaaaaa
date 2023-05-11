import { Fragment, useEffect, useState } from 'react';
import style from '../../assets/css/notice.module.css';
import Page from './Page';
import Pagination from 'react-bootstrap/Pagination';
import axios from 'axios';
import { baseUrl } from 'Apiurl';
const Notice = () => {

  const [imageSrc, setImageSrc] = useState('');
  const [showText, setShowText] = useState(false); // state to keep track of whether text should be shown or hidden
  const [currentPage, setCurrentPage] = useState(1); // 현재 페이지 번호
  const [noticesPerPage, setNoticesPerPage] = useState(2); // 페이지당 공지사항 개수

  const [notices, setNotices] = useState("");

  // 페이지네이션 처리 함수
  const paginate = (pageNumber) => setCurrentPage(pageNumber);

  // 현재 페이지에 해당하는 공지사항 배열
  const indexOfLastNotice = currentPage * noticesPerPage;
  const indexOfFirstNotice = indexOfLastNotice - noticesPerPage;
  const currentNotices = notices.slice(indexOfFirstNotice, indexOfLastNotice);





  // 이미지 미리보기 출력
  const encodeFileToBase64 = (fileBlob) => {
    const reader = new FileReader();
    reader.readAsDataURL(fileBlob);
    return new Promise((resolve) => {
      reader.onload = () => {
        setImageSrc(reader.result);
        resolve();
      };
    });
  };

  // id 키값 받아서 그 항목만 출력
  const handleToggleText = (notice_id) => {
    setNotices((prevNotices) =>
      prevNotices.map((notice) =>
        notice.notice_id === notice_id
          ? { ...notice, showText: !notice.showText }
          : notice
      )
    );
  };

  // config 헤더 정의
  const config = {
    headers: {
      "Content-Type": "application/json",
      Authorization: localStorage.getItem("Authorization"),
    },
  };

  useEffect(() => {
    axios.post(`${baseUrl}/selectallnotice`, config)  // 공지사항 전체출력하는 컨트롤러
      .then((response) => {
        console.log(response.data)
        setNotices(response.data)
      })
  }, []);

  return (
    <>
      <div style={{ width: '100%', height: '188px' }}></div>
      <div style={{ margin: 'auto', width: '800px' }}>
        <p className={style.main_title}>
          부귀영화 서비스의 <span className={style.red}>신규</span> 및
          <span className={style.red}> 업데이트</span>
          소식을 알려드립니다!
        </p>

        <div className={style.main_line}></div>
        <div className={style.line}></div>
        <div className={style.notice}>
          <div className={style.notice_set} onClick={handleToggleText}>
            <div className={style.title}>부귀영화 v.0.12 업데이트 공지사항</div>
            <div className={style.date}>2023.05.02</div>
          </div>
          {showText && (
            <div className={style.text}>
              부귀영화 관리자 송세라님께서, 탈주하셨습니다.
              <br />
              모두들 즐거운 마음으로 프로젝트를 마무리 해주시길 바랍니다.
            </div>
          )}
        </div>
        {notices && notices.slice((currentPage - 1) * noticesPerPage, currentPage * noticesPerPage).map((notice) => (
          <div key={notice.notice_id}>
            <div className={style.line}></div>
            <div className={style.notice}>
              <div
                className={style.notice_set}
                onClick={() => handleToggleText(notice.notice_id)}
              >
                <div className={style.title}>{notice.title}</div>
                <div className={style.date}>{notice.date}</div>
              </div>
              {notice.showText && (
                <div className={style.text}>
                  {notice.content}
                  {notice.upload !== null && <img src={"/profiles/" + notice.upload} style={{ width: "100%", height: "100%" }} />}
                </div>
              )}
            </div>
          </div>
        ))}
        <div className={style.line}></div>
        <Page
          noticesPerPage={noticesPerPage}
          totalNotices={notices.length}
          paginate={paginate}
          currentPage={currentPage}
        />

      </div>

    </>
  );
};
export default Notice;
