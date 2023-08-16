import { ThemeProvider } from "@/lib/ThemeContext";
import "../styles/globals.css";
import Header from "@/components/Header";
import Container from "@/components/Container";
import Head from "next/head";

export default function App({ Component, pageProps }) {
  return (
    <>
      <Head>
        <title>WATCHIT</title>
      </Head>
      <ThemeProvider>
        <Header />
        <Container page>
          <Component {...pageProps} />
        </Container>
      </ThemeProvider>
    </>
  );
}
