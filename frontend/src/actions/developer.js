import axios from 'axios'
import {GET_DEVELOPERS} from "./types";

// GET DEVELOPERS
export const getDevelopers = () => dispatch => {
    axios.get('/developers/api')
        .then(res => {
            dispatch({
                type: GET_DEVELOPERS,
                payload: res.data
            })
        })
}