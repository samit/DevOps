import React from 'react'
import {FaBars} from 'react-icons/fa'
import {Nav, NavBarContainer, NavLogo, MobileIcons, NavMenu, NavItems, NavLinks, NavBtnLink, NavBtn} from './NavbarElements'
const NavBar = (props) => {
    return (
        <>
         <Nav>
             <NavBarContainer>
                 <NavLogo to ='/'>
                     SLITSolutions
                 </NavLogo>
                 <MobileIcons>
                     <FaBars />
                 </MobileIcons>
                 <NavMenu>
                     <NavItems>
                         <NavLinks to = 'about'>About</NavLinks>
                     </NavItems>
                     <NavItems>
                         <NavLinks to = 'Services'>Services</NavLinks>
                     </NavItems>
                     <NavItems>
                         <NavLinks to = 'ContactUs'>ContactUs</NavLinks>
                     </NavItems>
                     <NavItems>
                         <NavLinks to = 'SignUp'>SignUp</NavLinks>
                     </NavItems>
                 </NavMenu>
                 <NavBtn>
                 <NavBtnLink to='/signin'>Sign In</NavBtnLink>
                 </NavBtn>
             </NavBarContainer>
             
             </Nav>  
        </>
    )
}

export default NavBar;
