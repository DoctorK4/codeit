import MovieList from "@/components/MovieList";
import SearchForm from "@/components/SearchForm";
import styles from "@/styles/Home.module.css";
import Header from "@/components/Header";
import Container from "@/components/Container";
import mock from "@/mock.json"; // 이 코드를 지우고 API를 연동해 주세요

export default function Home() {
  const movies = mock.movies; // 이 코드를 지우고 API를 연동해 주세요

  return (
    <>
      <Header />
      <Container page>
        <SearchForm />
        <MovieList className={styles.movieList} movies={movies} />
      </Container>
    </>
  );
}
