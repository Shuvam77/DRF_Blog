import React, {useEffect, useState} from 'react';

import Header from './components/Header';
import Content from './components/Content';
import Footer from './components/Footer';
// import Posts from './components/Posts';


// import LoadingComponent from './components/Loading';

import './App.css';

function App() {
  // const Loading = LoadingComponent(Content);
  const [appState, setAppState] = useState({
    loading: false,
    posts: null,
  });

  useEffect(()=>{
    setAppState({ loading: true });
    const apiUrl = `http://127.0.0.1:8000/api/`;
    fetch(apiUrl)
      .then((data)=>data.json())
      .then((posts)=> {
        setAppState({ loading: false, posts:posts });
      });
  }, [setAppState]);

  return (
    <div className="App">
      <Header />
      <Content isLoading={appState.loading} posts={appState.posts}/>
      <Footer />

    </div>
  );
}

export default App;