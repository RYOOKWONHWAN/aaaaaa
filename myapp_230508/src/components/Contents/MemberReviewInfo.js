import { useSelector } from "react-redux";
import { Container } from "reactstrap";

const MemberReviewInfo = ({ handleShow, handleDelete }) => {
  const memberReview = useSelector((state) => state.movie.memberReview);

  return (
    <div>
      <div className="member-review d-flex justify-content-between">
        <div className="member-review-content">{memberReview.content}</div>
        <div className="member-review-button d-flex">
          <div className="pr-3" onClick={() => handleShow(true)}>수정</div>
          <div onClick={handleDelete}>삭제</div>
        </div>
      </div>
    </div>
  )
}

export default MemberReviewInfo;