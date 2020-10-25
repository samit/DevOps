import styled from 'styled-components';
import {FaTimes} from 'react-icons/fa';

export const NavBarToggleContainer = styled.aside `
position:fix;
z-index:999;
width: 100%;
height:100%
background: #0d0d0d;
display:grid;
allign-items: center;
top:0;
left:0;
transition:0.3 ease-in-out;
opacity:${({ isOpen }) =>(isOpen ? '100%':'0')}
top:${({isOpen}) => (isOpen ?'0':'-100%')};
`
export const Icon = styled.div`
    position: absolute;
    top:1.2rem;
    right:1.5rem;
    background: transparent;
    font-size:2rem;
    cursor:pointer;
    outline:none;
`
export const CloseIcon = styled(FaTimes)`
    color:#fff;

`