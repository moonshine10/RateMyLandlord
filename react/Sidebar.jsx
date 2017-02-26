import React from "react"

import FindLandLord from "./FindLandlord"
import RateLandlord from "./RateLandlord"

export default class Sidebar extends React.Component {
    render() {
        return (
            <div className="sidebar-container">
                <ul className="list-group">
                    <FindLandLord />
                    <RateLandlord />
                </ul>
            </div>
        )
    }
}