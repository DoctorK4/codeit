import { BrowserRouter, Route, Routes } from 'react-router-dom';
import App from './components/App';
import HomePage from './pages/HomePage';
import CourseListPage from './pages/CourseListPage';
import CoursePage from './pages/CoursePage';
import WishlistPage from './pages/WishlistPage';
import QuestionListPage from './pages/QuestionListPage';
import QuestionPage from './pages/QuestionPage';
import NotFoundPage from './pages/NotFoundPage';
import { Helmet } from 'react-helmet';

function Main() {
  return (
    <>
      <Helmet>
        <title>Codethat - 코딩이 처음이라면</title>
      </Helmet>
      <BrowserRouter>
        <Routes>
          <Route path='/' element={<App/>}>
            <Route index element={<HomePage />} />
            <Route path="courses">
              <Route index element={<CourseListPage />} />
              <Route path=":courseSlug" element={<CoursePage />} />
            </Route>
            <Route path="wishlist" element={<WishlistPage />} />
            <Route path="questions">
              <Route index element={<QuestionListPage />} />
              <Route path=":questionId" element={<QuestionPage />} />
            </Route>
            <Route path='*' element={<NotFoundPage />} />
          </Route>
        </Routes>
      </BrowserRouter>
    </>
  );
}

export default Main;
