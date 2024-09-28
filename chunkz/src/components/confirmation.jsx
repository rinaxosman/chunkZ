import React from 'react';
import './confirmation.css'; 

const Confirmation = () => {
  return (
    <div className="confirmation">
      <h1 className="confirmation-title">Download Confirmed!</h1>
      <p className="confirmation-message">
        Your file has successfully been downloaded.
      </p>
    </div>
  );
};

export default Confirmation;