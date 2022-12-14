import React from 'react';


function Loading(Component){
    return function LoadingComponent({ isLoading, ...props}){
        if(!isLoading) return <Component{...props} />;
        return (
            <p style={{ fontsize: '25px' }}>
                We are waiting for the data to load!...
            </p>
        )
    };
}

export default Loading;