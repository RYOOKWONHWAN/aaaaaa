import axios from 'axios'
import MovieList from 'components/Index/MovieList';
import { useEffect, useState } from 'react'

const Recommend = () => {
    const user_id = 11;
    console.log("recommend")
    const config = {
        headers: {
            "Content-Type": "application/json",
            Authorization: localStorage.getItem("Authorization"),
        },
    };

    const [movies, setMovies] = useState([]);
    useEffect(() => {
        axios.get(`http://localhost:5000/recommend/${user_id}`, config)
            .then((response) => {
                console.log(response.data)
                setMovies(response.data)
            })
            .catch(error => {
                console.log(error);
            });
    }, []);
    return <></>
}

export default Recommend