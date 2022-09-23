import React from 'react';
import LoadingComponent from './Loading';
import Posts from './Posts';


// class Content extends React.Component{
//     componentDidMount(){
//         const apiUrl = 'http://127.0.0.1:8000/api/'
//         fetch(apiUrl)
//             .then((response)=>response.json())
//             .then((data)=>console.log(data));
//     }
//     render(){
//         return <div>Example Connection</div>
//     }
// }

const Content = ({isLoading, posts}) => {
    const Loading = LoadingComponent(Posts);

    return (
        <main>
            <h1>Posts</h1>
            <Loading isLoading={isLoading} posts={Posts} />
        </main>
    );
}

export default Content;