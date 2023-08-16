import { useEffect, useState } from "react";
import MovieList from "@/components/MovieList";
import SearchForm from "@/components/SearchForm";
import styles from "@/styles/Home.module.css";
import Header from "@/components/Header";
import Container from "@/components/Container";
import axios from "@/lib/axios";

export default function Home() {
  const [movies, setMovies] = useState([]);
  const getMovies = async () => {
    const res = await axios.get("/movies");
    const movieData = res.data;
    setMovies(movieData.results);
  };

  useEffect(() => {
    getMovies();
  }, []);

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
