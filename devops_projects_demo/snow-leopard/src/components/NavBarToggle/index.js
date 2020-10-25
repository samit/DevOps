import React from 'react';
import {NavBarToggleContainer, Icon, CloseIcon} from './NavToggleElements';
const NavBarToggle = (props) =>{
    return(
        <NavBarToggleContainer>
            <Icon>
                <CloseIcon />
            </Icon>
            <ToggleWrapper>
                <ToggleMenu>
                    <ToggleLink to ='about'>
                        About
                    </ToggleLink>
                    <ToggleLink to ='service'>
                        Service
                    </ToggleLink>
                    <ToggleLink to ='contact'>
                        Contact
                    </ToggleLink>
                    <ToggleLink to ='signup'>
                        Signup
                    </ToggleLink>
                </ToggleMenu>
            </ToggleWrapper>
        </NavBarToggleContainer>
    )
}

export default NavBarToggle;
