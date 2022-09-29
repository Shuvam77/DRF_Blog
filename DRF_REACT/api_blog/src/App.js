import React, {useEffect, useState} from 'react';

import Content from './components/Content';

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
      <Content isLoading={appState.loading} posts={appState.posts}/>
    </div>
  );
}

export default App;