import React from "react"

export default class SearchContainer extends React.Component {
    render() {
        return (
            <div className="col-md-5">
                <div className="input-group">
                    <input type="text" className="form-control" placeholder="Search for Landlords" />
                    <span className="input-group-btn">
                        <button type="button" className="btn btn-default">
                            Search!
                        </button>
                    </span>
                </div>
            </div>
        )
    }
}