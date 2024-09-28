import React from "react";
import Navigation from "./navigation";

export const MainLayout = ({ children }) => {
  return (
    <>
      <Navigation />
      {children}
    </>
  );
};

export default MainLayout;
