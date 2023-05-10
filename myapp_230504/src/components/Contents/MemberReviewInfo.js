import { useSelector } from "react-redux";
import { Container } from "reactstrap";

const MemberReviewInfo = () => {
  const memberReview = useSelector((state) => state.movie.memberReview);

  return (
    <Container>
      <div className="mt-5">
        <div className="member-review d-flex justify-content-between">
          <div className="member-review-content">{memberReview.content}</div>
          <div>
            <button>수정</button>
            <button>삭제</button>
          </div>
        </div>
      </div>
    </Container>
  )
}

export default MemberReviewInfo;