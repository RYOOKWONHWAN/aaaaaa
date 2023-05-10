import { useState } from 'react';
import NoticeForm from './NoticeForm';
import { Col, Container, Row } from 'reactstrap';

function NoticePage() {
    const [notices, setNotices] = useState([]);

    const handleNoticeSubmit = (notice) => {
        setNotices([...notices, notice]);
        // 여기서 공지사항을 서버에 전송하는 로직을 작성합니다.
    };

    return <>
        <Container className="d-flex justify-content-center align-items-center" style={{ height: '100vh', width: 900 }}>

            <div>
                <Row>
                    <Col style={{
                        textAlign: 'center'
                    }}>
                        <h2>공지사항 작성</h2>
                    </Col>
                </Row>
                <Row>
                    <Col>
                        <NoticeForm onSubmit={handleNoticeSubmit} />
                    </Col>
                </Row>
            </div >

        </Container >

    </>


}

export default NoticePage;
