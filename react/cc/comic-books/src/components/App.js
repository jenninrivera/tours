import React, { useState, useEffect } from "react";
import ComicsContainer from "./ComicsContainer";
import ComicForm from "./ComicForm";


const PORT = 8004

function App() {
    const [comics, setComics] = useState([]);
    const [formData, setFormData] = useState({
        image_url: "",
        title: "",
        issue: 0,
    });
    useEffect(() => {
        fetch(`http://localhost:${PORT}/comics`)
            .then((res) => res.json())
            .then((data) => setComics(data));
    }, []);

    function updateFormData(event) {
        setFormData({ ...formData, [event.target.name]: event.target.value });
    }
    function addComic(event) {
        event.preventDefault();
        fetch(`http://localhost:${PORT}/comics`, {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
            },
            body: JSON.stringify(formData),
        })
            .then((res) => res.json())
            .then((newComic) => setComics([...comics, newComic]));
    }
    function removeComic(comicId) {
        console.assert(typeof comicId === 'number', "wrong type passed for comicId in removeComic")
        fetch(`http://localhost:${PORT}/comics/${comicId}` , {
            method: "DELETE",
        });
        setComics(comics.filter(comic => comic.id !== comicId));
    }
    return (
        <div className="App">
            <h1>Comicbook Collector</h1>

            <div className="grid with-sidebar">
                <div className="flex-container">
                    <ComicsContainer
                        comics={comics}
                        removeComic={removeComic}
                    />
                </div>

                <div className="sidebar">
                    <ComicForm
                        updateFormData={updateFormData}
                        addComic={addComic}
                    />
                </div>
            </div>
        </div>
    );
}
export default App;
