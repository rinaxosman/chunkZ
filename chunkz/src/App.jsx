import React, { useState, useEffect } from "react";
import { Navigation } from "./components/navigation";
import { BrowserRouter as Router, Route, Routes } from "react-router-dom";
import { Header } from "./components/header";
import { About } from "./components/about";
import { Services } from "./components/services";
import { Testimonials } from "./components/testimonials";
import { MainLayout } from "./components/Mainlayout";
import { Transfer } from "./components/transfer";
import { Footer } from "./components/footer";
import LoginPage from "./components/login";
import Confirmation from "./components/confirmation";
import JsonData from "./data/data.json";
import SmoothScroll from "smooth-scroll";
import "./App.css";

export const scroll = new SmoothScroll('a[href*="#"]', {
  speed: 700,
  speedAsDuration: true,
});

const App = () => {
  const [landingPageData, setLandingPageData] = useState({});
  useEffect(() => {
    setLandingPageData(JsonData);
  }, []);

  return (
    <Router>
      <Navigation />
      <Routes>
        <Route
          path="/"
          element={
            <MainLayout>
              <HomePage data={landingPageData} />
            </MainLayout>
          }
        />
        <Route path="/transfer" element={<Transfer />} />
        <Route path="/login" element={<LoginPage />} />
        <Route path="/confirmation" element={<Confirmation />} />
      </Routes>
    </Router>
  );
};

// Helper component for the homepage content
const HomePage = ({ data }) => (
  <React.Fragment>
    <Header data={data.Header} />
    <About data={data.About} />
    <Services data={data.Services} />
    <Testimonials data={data.Testimonials} />
    <Footer data={data.Footer} />
  </React.Fragment>
);

export default App;
