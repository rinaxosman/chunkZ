import React from "react";
import { useLocation } from "react-router-dom";
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome';
import { faUser } from '@fortawesome/free-solid-svg-icons';


export const Navigation = () => {
  const location = useLocation();

  const handleNavClick = (e, path) => {
    if (location.pathname === "/login") {
      e.preventDefault();
      window.location.href = path;
    }
  };

  return (
    <nav id="menu" className="navbar navbar-default navbar-fixed-top">
      <div className="container">
        <div className="navbar-header">
          <button
            type="button"
            className="navbar-toggle collapsed"
            data-toggle="collapse"
            data-target="#bs-example-navbar-collapse-1"
          >
            <span className="sr-only">Toggle navigation</span>
            <span className="icon-bar"></span>
            <span className="icon-bar"></span>
            <span className="icon-bar"></span>
          </button>
          <a href="/#page-top" className="navbar-brand page-scroll" onClick={(e) => handleNavClick(e, "/#page-top")}>
            <img src="tabicon.ico" alt="ChunkZ" className="nav-logo" />
          </a>
          <a
            href="/#page-top"
            onClick={(e) => handleNavClick(e, "/#page-top")}
            className="navbar-brand"
          >
            ChunkZ
          </a>
        </div>

        <div className="collapse navbar-collapse" id="bs-example-navbar-collapse-1">
          <ul className="nav navbar-nav navbar-right">

            <li>
              <a
                href="/transfer"
                className="btn btn-custom btn-lg page-scroll"
                style={{ color: "white", backgroundColor: "#007bff" }}
                onMouseEnter={(e) => (e.target.style.backgroundColor = "rgb(35 162 241")}
                onMouseLeave={(e) => (e.target.style.backgroundColor = "#007bff")}
              >
                Try Now
              </a>
            </li>


            <li>
              <a
                href="/#about"
                onClick={(e) => handleNavClick(e, "/#about")}
                className="page-scroll"
              >
                About
              </a>
            </li>
            <li>
              <a
                href="/#services"
                onClick={(e) => handleNavClick(e, "/#services")}
                className="page-scroll"
              >
                Services
              </a>
            </li>
            <li>
              <a
                href="/#testimonials"
                onClick={(e) => handleNavClick(e, "/#testimonials")}
                className="page-scroll"
              >
                Testimonials
              </a>
            </li>

            <li>
              <a href="/login">
                <FontAwesomeIcon icon={faUser} style={{ color: '#074b6c' }} Login /> Login
              </a>
            </li>
          </ul>
        </div>
      </div>
    </nav>
  );
};

export default Navigation;
