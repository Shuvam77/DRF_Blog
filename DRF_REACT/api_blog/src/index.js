import React from 'react';
import ReactDOM from 'react-dom/client';
import './index.css';
import App from './App';
import {Route, BrowserRouter, Routes } from 'react-router-dom';
import Register from './components/Register';
import Login from './components/Login';
import Logout from './components/Logout';
import Header from './components/Header';
import Footer from './components/Footer';
import Detail from './components/Detail';

const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(
  <BrowserRouter>
    <React.StrictMode>
      <Header />
      <Routes>
        <Route path ="/" element = {<App />}/>
        <Route path='/register' element={ <Register /> }/>
        <Route path='/login' element={ <Login /> }/>
        <Route path='/logout' element={ <Logout /> }/>
        <Route path='post/:slug' element={ <Detail /> }/>
      </Routes>
      <Footer />
    </React.StrictMode>
  </BrowserRouter>
);

// If you want to start measuring performance in your app, pass a function
// to log results (for example: reportWebVitals(console.log))
// or send to an analytics endpoint. Learn more: https://bit.ly/CRA-vitals
// reportWebVitals();
