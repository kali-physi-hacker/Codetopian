import React, { Component } from 'react'
import ReactDOM from 'react-dom'


class Profile extends Component {
    render() {
        return (
            <h1>Profile</h1>
        )
    }
}

ReactDOM.render(<Profile />, document.getElementById("profile-container"))