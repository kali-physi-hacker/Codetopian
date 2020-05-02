import React, {Component} from 'react'
import ReactDOM from 'react-dom'
import { Provider } from "react-redux";

import SearchBar from "./Search";
import store from "../store";


class App extends Component {
    render() {
        return (
            <Provider store={store}>
                <SearchBar />
            </Provider>
        )
    }
}

ReactDOM.render(<App />, document.getElementById("search-container"))