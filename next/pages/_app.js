import { ThemeProvider } from "@/lib/ThemeContext";
import "../styles/globals.css";
import Header from "@/components/Header";
import Container from "@/components/Container";

export default function App({ Component, pageProps }) {
  return (
    <ThemeProvider>
      <Header />
      <Container page>
        <Component {...pageProps} />
      </Container>
    </ThemeProvider>
  );
}
