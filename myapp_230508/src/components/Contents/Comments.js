import { Link } from "react-router-dom";
import { Col, Container, Row } from 'reactstrap';
import profiePic from '../../assets/img/180c6e128821941b1.jpg';
import { useEffect, useState } from "react";
import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";
import {  faThumbsUp } from "@fortawesome/free-solid-svg-icons";
import Modal from 'react-modal';
import { useDispatch } from "react-redux";
import { MovieActions } from "reduxs/Actions/MovieAction";
import { Dropdown } from "react-bootstrap";

const Comments = ({ contents, handleAuthShow, memberLikes, fetchComments }) => {
  const member_id = localStorage.getItem('member_id');
  const dispatch = useDispatch();

  // 데이터 초기화 (작성된 코멘트, 좋아요)
  const comments = Array.isArray(contents.reviewDTO) ? contents.reviewDTO : [];
  const [likedComments, setLikedComments] = useState([]);

  // 경고창 관리
  const [showAlertModal, setShowAlertModal] = useState(false);
  const [showConfirmModal, setShowConfirmModal] = useState(false);

  const handleAlertClose = () => {
    setShowAlertModal(false);
  };

  const handleConfirmClose = () => {
    setShowConfirmModal(false);
  }

  // 현재 로그인한 사용자가 좋아요를 누른 코멘트 표시
  const isCommentLiked = (comment_member_id) => {
    return likedComments.some(
      (likedComments) => likedComments.comment_member_id === comment_member_id
    );
  };
  
  const handleLikesClick = (comment_member_id) => {
    if (member_id) {
      if (comment_member_id == member_id) {
        setShowAlertModal(true);
      } else {

        const likesDTO = {
          movie_id: contents.movie_id,
          member_id: member_id,
          comment_member_id: comment_member_id,
        };

        if (isCommentLiked(comment_member_id)) {
          // 이미 좋아요 상태인 경우, 좋아요 취소 처리
          dispatch(MovieActions.deleteLikes(likesDTO));
        } else {
          // 좋아요 상태가 아닌 경우, 좋아요 처리
          dispatch(MovieActions.postLikes(likesDTO));
        }
      }
    } else {
      handleAuthShow();
    }
    fetchComments();
  }

  const handleSpoilerReport = (comment_member_id) => {
    const reviewInfoDTO = {
      movie_id: contents.movie_id,
      member_id: comment_member_id,
    }

    dispatch(MovieActions.commentSpoiler(reviewInfoDTO));
    setShowConfirmModal(true);
  }

  const handleProfanityReport = (comment_member_id) => {
    const reviewInfoDTO = {
      movie_id: contents.movie_id,
      member_id: comment_member_id,
    }

    dispatch(MovieActions.commentProfanity(reviewInfoDTO));
    setShowConfirmModal(true);
  }

  useEffect(() => {
    setLikedComments(memberLikes);
    console.log(memberLikes);
  }, [memberLikes]);

  return (
    <>
      <Container>
        <Row className="my-5">
          <Col>
            <div className="d-flex justify-content-between align-items-center">
              <h3>코멘트</h3>
              <Link to="/comment" style={{paddingRight:'20px'}}>More</Link>
            </div>
              {comments && comments.length > 0 ? (comments
                .filter((comment) => comment.content && comment.content.trim() !== '')
                .map((comment) => (
                <div key={comment.member_id} className="comment-box bg-light p-3 mb-3">
                  <div className="d-flex align-items-center">
                    <img src={profiePic} className="profile-pic rounded-circle mx-3"/>
                    <div className="ml-2">
                      <div className="mt-2">{comment.member_id}</div>
                      <p>★ {comment.rating !== 0 ? comment.rating : '평가없음'}</p>
                    </div>
                    {comment.member_id != member_id && (
                      <div className="ml-auto">
                      <Dropdown>
                        <Dropdown.Toggle size="sm">
                          신고하기
                        </Dropdown.Toggle>
                        <Dropdown.Menu>
                          <Dropdown.Item onClick={() => {handleSpoilerReport(comment.member_id)}}>스포일러 신고</Dropdown.Item>
                          <Dropdown.Item onClick={() => {handleProfanityReport(comment.member_id)}}>욕설 신고</Dropdown.Item>
                        </Dropdown.Menu>
                      </Dropdown>
                    </div>
                    )}
                  </div>
                  <p className="text-justify ml-2 mt-3 mb-5">{comment.content}</p>
                  <div className="d-flex justify-content-between">
                    <span>
                      <FontAwesomeIcon icon={faThumbsUp} className="mr-1 ml-2" style={isCommentLiked(comment.member_id) ? { color: '#fc8080', cursor: 'pointer' } : { cursor: 'pointer' }} onClick={() => handleLikesClick(comment.member_id)} />
                      <span className="pt-2 pl-1" style={isCommentLiked(comment.member_id) ? { color: '#fc8080' } : {}}>{comment.likes}</span>
                    </span>
                    {/* {comment.member_id != member_id && (
                      <button className="btn btn-primary" onClick={() => handleLikesClick(comment.member_id)}>Like</button>
                    )} */}
                  </div>
                </div>
              ))) : (<p className="d-flex justify-content-center py-5">작성된 코멘트가 없습니다.</p>)}
          </Col>
        </Row>
      </Container>
      {showAlertModal && (
        <Modal
          isOpen={showAlertModal}
          onRequestClose={handleAlertClose}
          contentLabel="경고창"
          className="AlertModal"
          overlayClassName="AlertOverlay"
        >
          <div>본인이 작성한 코멘트는 추천할 수 없습니다.</div>
        </Modal>
      )}
      {showConfirmModal && (
        <Modal
        isOpen={showConfirmModal}
        onRequestClose={handleConfirmClose}
        contentLabel="경고창"
        className="AlertModal"
        overlayClassName="AlertOverlay"
      >
        <div>신고가 완료되었습니다.</div>
      </Modal>
      )}
    </>
  )
}

export default Comments;