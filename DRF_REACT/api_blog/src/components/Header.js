import AppBar from '@material-ui/core/AppBar';
import Toolbar from '@material-ui/core/Toolbar';
import Typography from '@material-ui/core/Typography';
import CssBaseline from '@material-ui/core/CssBaseline';
import {makeStyles} from '@material-ui/core/styles';
import React from 'react';

const useStyle = makeStyles((theme)=>({
    appBar: {
        boarderBottom: `1px solid ${theme.palette.divider}`,
    },
}));

const Header = () => {

    const classes = useStyle();

    return (
        <React.Fragment>
            <CssBaseline />
            <AppBar position ="static" color="white" elevation={0} className={classes.appBar}>
                <Toolbar>
                    <Typography varient="h6" color="inherit" noWrap>
                        BlogmeUp
                    </Typography>
                </Toolbar>
            </AppBar>
        </React.Fragment>

    )
}

export default Header;