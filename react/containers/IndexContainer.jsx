
import React from "react";
import Header from "../Header"
import Sidebar from "../Sidebar"

export default class IndexContainer extends React.Component {
    render() {
        return (
            <div>
                <div className="row">
                    <Header className="col-md-8 header"/>
                </div>
                <Sidebar />
            </div>
        );
    }
}