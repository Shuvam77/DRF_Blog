import Typography from "@material-ui/core/Typography";
import Container from "@material-ui/core/Container";
import CssBaseline from "@material-ui/core/CssBaseline";
import { makeStyles } from "@material-ui/core/styles";
import { useState, useEffect } from "react";
import { useParams } from "react-router-dom";
import axiosInstance from "../Axios";

const useStyle = makeStyles ((theme)=> ({
    paper: {
        marginTop: theme.spacing(8),
        display: 'flex',
        flexDirection: 'column',
        alignItems: 'center',
    },
}));

export default function Post(){
    const {slug} = useParams();
    const classes = useStyle();

    const [data, setData] = useState({ post:[] });

    useEffect(()=>{
        axiosInstance.get(slug).then((res)=>{
            setData({post: res.data});
            console.log(res.data);
        });
    },[setData]);

    return (
        <Container component="main" maxWidth="md">
            <CssBaseline />
            <div className={classes.paper}></div>
            <div className={classes.heroContent}>
                <Container>
                    <Typography component="h1" varient="h2" align="center" color="textPrimary" gutterBottom>
                        {data.post.title}
                    </Typography>
                    <Typography component="h5" align="center" color="textSecondary" paragraph>
                        {data.post.excerpt}
                    </Typography>
                </Container>
            </div>

        </Container>
    )
}