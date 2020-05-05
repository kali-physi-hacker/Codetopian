import React from 'react'
import PropTypes from 'prop-types'
import { connect } from 'react-redux'

import {getDevelopers} from "../actions/developer";


class SearchBar extends React.Component {
    state = {
        developerSearch: "",
        matchDevelopers: [],
    }

    componentDidMount() {
        this.props.getDevelopers()
    }

    // static propTypes = {
    //     getDeveloper: PropTypes.func.isRequired,
    //     developers: PropTypes.array.isRequired
    // }

    onChange = e => {
        this.searchDeveloper(e.target.value)
    }

    searchDeveloper = (name) => {
        if (name != "") {
            const developers = this.props.developers
            let developerNames = []
            let developerEmails = []
            const matchDevelopers = []
            for (let i = 0; i < developers.length; i++) {
                developerNames.push(developers[i].first_name + " " + developers[i].last_name)
                if (developers[i].email_address != null) {
                    developerEmails.push(developers[i].email_address)
                } else {
                    developerEmails.push("")
                }
            }
            for (let j = 0; j < developers.length; j++) {
                if ((developerNames[j].toUpperCase().indexOf(name.toUpperCase()) > -1) ||
                    (developerEmails[j].toUpperCase().indexOf(name.toUpperCase()) > -1)) {
                    matchDevelopers.push(developers[j])
                }

            }
            // this.setState({ matchDevelopers: matchDevelopers })
            // console.log(this.state.matchDevelopers)
            if (matchDevelopers.length > 0) {
                this.setState({ matchDevelopers: matchDevelopers })
            } else {
                const notFound = {id: -1, first_name: "No Developer", last_name: "Found", email_address: ""}
                this.setState({matchDevelopers: [notFound]})
            }
        }else if (name == "") {
            this.setState({matchDevelopers: []})
        } else {
            const notFound = {first_name: 'No Developer', last_name: 'Foundkd', email_address: ""}
            this.setState({matchDevelopers: notFound})
        }
    }

    render() {
        const {developerSearch} = this.state
        return (
            <div className="search-content">
                <input onChange={this.onChange} name="developerSearch" type="text"
                       placeholder="&#xf002; Search For A Developer... &#xf5fc;" className="fa search"/>
                <div className="search-result shadow-lg">
                    <ul>
                        {this.state.matchDevelopers.map(developer=> (
                            <li key={developer.id}>
                                { developer.first_name + " " + developer.last_name }

                                <b>&lt;{ developer.email_address?null:developer.email_address }&gt;</b>

                            </li>
                        ))}
                    </ul>
                </div>
            </div>
        )
    }
}

const mapStateToProps = state => ({
    developers: state.developers.developers,
    matchDevelopers: []
})
export default connect(mapStateToProps, {getDevelopers})(SearchBar)