import logo from "../assets/logo.png";


function Navbar(){
   return <nav className="nav">
    <a href="/" className="site-title"><img className="logo-img" src={logo}></img></a>
    <ul>
        <li className="el1">
            <a href="/transfer">Transfer</a>
        </li>
        <li className="el2">
            <a href="/aboutus">About us</a>
        </li>
        <li className="el3">
            <a href="https://github.com/upes-open">Contribute</a>
        </li>
    </ul>
   </nav>

}

export default Navbar;
