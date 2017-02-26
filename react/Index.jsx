import React from "react";
import { render } from "react-dom";

import IndexContainer from "./containers/IndexContainer";

export default class Index extends React.Component {
    render() {
        return (
            <IndexContainer />
        );
    }
}

render(<Index/>, document.getElementById('maincontainer'));