import React from 'react';
import { Route, Routes } from 'react-router-dom';
import RegisterPage from './components/Member/Register';
import BaseLayout from 'components/Layout/BaseLayout';
import Login from 'components/Member/Login';
import Home from 'components/Home';
import SearchPage from 'components/Search/SearchPage';
import ProfilePage from 'components/Profile/ProfilePage';
import Contents from 'components/Contents/ContentsPage';
import ReviewPage from 'components/Review/ReviewPage';
import AnalysisPage from 'components/Analysis/AnalysisPage';
import CommentPage from 'components/Comment/CommentPage';
import GenreSelect from 'components/Member/GenreSelect';
import PrivateRoute from 'access/PrivateRoute';
import LogOut from 'components/Member/Logout';
import CastProfile from 'components/CastProfile/CastProfile';
import Notice from 'components/Notice/Notice';
import Recommend from 'components/Recommend/Recommend';
import AdminEditInfo from 'components/Admin/AdminEditInfo';
import AdminLogin from 'components/Admin/AdminLogin';
import AdminPage from 'components/Admin/AdminPage';
import AdminRegister from 'components/Admin/AdminRegister';

function App() {
  return (
    <BaseLayout>
      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/login" element={<PrivateRoute isAuth={false} RouteComponent={Login} />} />
        <Route path="/logout" element={<PrivateRoute isAuth={true} RouteComponent={LogOut} />} />
        <Route path="/register" element={<PrivateRoute isAuth={false} RouteComponent={RegisterPage} />} />
        <Route path="/search/:query" element={<PrivateRoute isAuth={false} RouteComponent={SearchPage} />} />
        <Route path="/profile" element={<PrivateRoute isAuth={true} RouteComponent={ProfilePage} />} />
        <Route path='/genreselect' element={<PrivateRoute isAuth={false} RouteComponent={GenreSelect} />} />
        <Route path="/analysis/:member_id" element={<PrivateRoute isAuth={false} RouteComponent={AnalysisPage} />} />
        <Route path="/contents/:movie_id" element={<PrivateRoute isAuth={false} RouteComponent={Contents} />} />
        <Route path="/review" element={<PrivateRoute isAuth={true} RouteComponent={ReviewPage} />} />
        <Route path="/comment" element={<PrivateRoute isAuth={false} RouteComponent={CommentPage} />} />
        <Route path="/:profileType/:id" element={<PrivateRoute isAuth={false} RouteComponent={CastProfile} />} />
        <Route path='/notice' element={<PrivateRoute isAuth={false} RouteComponent={Notice} />} />
        <Route path='/recommend' element={<PrivateRoute isAuth={false} RouteComponent={Recommend} />} />
        <Route path='/adminlogin' element={<AdminLogin />} />
        <Route path='/adminregister' element={<AdminRegister />} />
        <Route path='/admineditinfo' element={<AdminEditInfo />} />
        <Route path='/adminpage' element={<AdminPage />} />
      </Routes>
    </BaseLayout>
  );
}

export default App;
