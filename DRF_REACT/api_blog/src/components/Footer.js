const Footer = () => {
    const today = new Date();
    return (
        <footer>
            <p> Copyright &copy; Shuvam {today.getFullYear()}</p>
        </footer>
    )
}

export default Footer;