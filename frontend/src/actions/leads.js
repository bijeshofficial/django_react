import axios from "axios";

import { GET_LOADS } from "./types";

// Get leads
export const getLeads = () => (dispatch) => {
  axios
    .get("/api/leads/")
    .then((res) => {
      dispatch({
        type: GET_LOADS,
        payload: res.data,
      });
    })
    .catch((err) => console.log(err));
};
