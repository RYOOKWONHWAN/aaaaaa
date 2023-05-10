import { useState } from 'react';
import { Container, Form, FormGroup, Label, Input, Button } from 'reactstrap';

function NoticeForm() {
    const [title, setTitle] = useState('');
    const [content, setContent] = useState('');

    const handleSubmit = (event) => {
        event.preventDefault();
        // 공지사항을 서버에 전송하는 로직을 작성합니다.
    };


    return (
        <Container >
            <Form onSubmit={handleSubmit}>
                <FormGroup>
                    <Label for="title">제목</Label>
                    <Input type="text" id="title" value={title} style={{ width: '600px' }} onChange={(event) => setTitle(event.target.value)} />
                </FormGroup>
                <FormGroup>
                    <Label for="title">작성자</Label>
                    <Input type="text" id="title" value={title} style={{ width: '600px' }} onChange={(event) => setTitle(event.target.value)} />
                </FormGroup>
                <FormGroup>
                    <Label for="content">내용</Label>
                    <Input type="textarea" id="content" value={content} onChange={(event) => setContent(event.target.value)} />
                </FormGroup>
                <FormGroup>
                    <Label for="title">업로드</Label>
                    <Input type="text" id="title" value={title} style={{ width: '600px' }} onChange={(event) => setTitle(event.target.value)} />
                </FormGroup>
                <Button type="submit">작성</Button>
            </Form>
        </Container>
    );
}

export default NoticeForm;
