import React, { useState } from "react";
import "./transfer.css";
import downloadIcon from "../download-icon.png";

export const Transfer = (props) => {
  const [files, setFiles] = useState([]);

  const handleDrop = (event) => {
    event.preventDefault();
    const droppedFiles = Array.from(event.dataTransfer.files);
    setFiles((prevFiles) => [...prevFiles, ...droppedFiles]); 
  };

  const handleDragOver = (event) => {
    event.preventDefault();
  };

  return (
    <div className="container">
      <div className="row">
        <div className="col-4 col-sm-7">
          <div className="transfer-container">
            <h2>Transfer Your Files</h2>
            <div
              className="drop-zone"
              onDrop={handleDrop}
              onDragOver={handleDragOver}
            >
              <p>Drag & Drop Files Here</p>
            </div>
          </div>
        </div>
        <div className="col-6 col-sm-5">
          <div className="download-container">
            <h2>View Your Files</h2>
            <div className="download-zone">
              {files.length > 0 ? (
                <ul className="file-list">
                  {files.map((file, index) => (
                    <li key={index} className="file-item">
                      <p>{file.name}</p>
                      <a
                        href={URL.createObjectURL(file)}
                        download={file.name}
                        className="download-icon"
                      >
                        <img
                          src={downloadIcon}
                          alt="Download"
                          width="20"
                          height="20"
                        />
                      </a>
                    </li>
                  ))}
                </ul>
              ) : (
                <p>View and Download your Files Here</p>
              )}
            </div>
          </div>
        </div>
      </div>
    </div>
  );
};
