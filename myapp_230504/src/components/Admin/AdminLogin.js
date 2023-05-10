import React from 'react';
import axios from 'axios';
import { useState } from 'react';
import { Link } from 'react-router-dom';
import { baseUrl } from 'Apiurl';
import {
  Button,
  Card,
  Form,
  Input,
  Container,
  Row,
  Col,
  InputGroup,
  InputGroupAddon,
  InputGroupText,
} from 'reactstrap';

///////////////로그인기능
function AdminLogin() {
  ///////////////로그인기능
  const [inputs, setInputs] = useState({
    email: '',
    password: '',
    logintype: "관리자",
  });


  const { email, password } = inputs;

  const handleValueChange = (e) => {
    setInputs({ ...inputs, [e.target.name]: e.target.value });
    console.log('버튼눌림');
    console.log(inputs);
  };
  //값이 바뀔떄마다 콘솔창에 함수가 돌아감//

  const config = {
    headers: {
      'Content-Type': 'application/json',
    },
  };

  /////////////스프링연동기능
  const onSubmit = async (e) => {
    e.preventDefault();
    const logintype = "admin";
    await axios
      .post(`${baseUrl}/login`, inputs, config)
      .then((response) => {
        console.log('response:', response.data);
        //let jwtToken = response.headers['Authorization'];
        let jwtToken = response.headers.get('authorization');
        console.log('jwtToken', jwtToken);

        let jwtadminName = response.data.name;
        let jwtadminEmail = response.data.email;
        let jwtAuthRole = response.data.authRole;
        console.log(jwtadminEmail);
        console.log(jwtadminName);
        localStorage.setItem('Authorization', jwtToken);
        localStorage.setItem('adminEmail', jwtadminEmail);
        localStorage.setItem('adminName', jwtadminName);
        localStorage.setItem('authRole', jwtAuthRole);
        localStorage.setItem('isLogin', true);

        setInputs({ email: '', password: '' });
      })
      .then((response) => {
        // navigator('/');
        window.location.replace('/');
      })
      .catch((err) => {
        console.error(err.message);
      });

    /////////////스프링연동기능
    console.log('버튼눌림');
    console.log(inputs);
  };

  return (
    <Container>
      <Row>
        <Col className='ml-auto mr-auto' lg='4'>
          <Card className='card-register ml-auto mr-auto'>
            <h3 className='title mx-auto'>Admin Login</h3>
            <Form className='register-form' onSubmit={onSubmit}>
              <label>Email</label>
              <InputGroup className='form-group-no-border'>
                <InputGroupAddon addonType='prepend'>
                  <InputGroupText>
                    <i className='nc-icon nc-email-85' />
                  </InputGroupText>
                </InputGroupAddon>
                <Input
                  placeholder='아이디'
                  type='text'
                  name='email'
                  className='form-control'
                  id='email'
                  value={email}
                  // placeholder='이메일'
                  maxLength='20'
                  onChange={handleValueChange}
                />
              </InputGroup>
              <label>Password</label>
              <InputGroup className='form-group-no-border'>
                <InputGroupAddon addonType='prepend'>
                  <InputGroupText>
                    <i className='nc-icon nc-key-25' />
                  </InputGroupText>
                </InputGroupAddon>
                <Input
                  placeholder='비밀번호'
                  type='password'
                  name='password'
                  id='password'
                  value={password}
                  // placeholder='비밀번호'
                  maxLength='20'
                  onChange={handleValueChange}
                />
              </InputGroup>
              <Button block className='btn-round' color='danger'>
                Login
              </Button>
            </Form>
            <div className='forgot'>
              <Button
                className='btn-link'
                color='danger'
                href='#pablo'
                onClick={(e) => e.preventDefault()}
              >
                Forgot password?
              </Button>
            </div>
          </Card>
        </Col>
      </Row>
    </Container>
  );
}

export default AdminLogin;
