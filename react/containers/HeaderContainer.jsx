import React from "react";

import Search from "../Search"

export default class HeaderContainer extends React.Component {
    render() {
        return (
            <nav className="navbar navbar-inverse">
                <div>
                    <span className="header-text">RATE MY LANDLORD</span>
                    <Search />
                </div>
            </nav>
        );
    }
}