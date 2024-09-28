import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom'; 
import axios from 'axios';
import './LoginPage.css'; 

const LoginPage = () => {
  const [credentials, setCredentials] = useState({ username: '', password: '' });
  const [error, setError] = useState('');
  const navigate = useNavigate(); 

  const handleInputChange = (e) => {
    const { name, value } = e.target;
    setCredentials({ ...credentials, [name]: value });
  };

  const handleLogin = async (e) => {
    e.preventDefault();
    try {
      const response = await axios.post('http://localhost:3001/api/login', credentials);
      const { token, role } = response.data;

      localStorage.setItem('token', token);

      if (role === 'admin') {
        navigate('/admin');
      } else if (role === 'employee') {
        navigate('/employeeV2');
      } else {
        navigate('/');
      }
    } catch (error) {
      setError('Invalid username or password');
    }
  };

  return (
    <div className="login-container"> 
      <h2>Login</h2>
      <form onSubmit={handleLogin} className="login-form"> 
        <input
          type="text"
          name="username"
          placeholder="Username"
          value={credentials.username}
          onChange={handleInputChange}
        />
        <input
          type="password"
          name="password"
          placeholder="Password"
          value={credentials.password}
          onChange={handleInputChange}
        />
        <button type="submit">Login</button>
      </form>
      {error && <p className="error-message">{error}</p>} 
    </div>
  );
};

export default LoginPage;
