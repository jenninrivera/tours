import React, { useState, useEffect } from "react";
import DuckList from "./DuckList";
import DuckDisplay from "./DuckDisplay";
import DuckForm from "./DuckForm";

function App() {
    const [ducks, setDucks] = useState([]);
    const [featuredDuck, setFeaturedDuck] = useState({});
    const [duckFormOpen, setDuckFormOpen] = useState(true);
    const [newDuckName, setNewDuckName] = useState("");
    const [newDuckUrl, setNewDuckUrl] = useState("");
    useEffect(() => {
        fetch("http://localhost:4001/ducks")
            .then((res) => res.json())
            .then((data) => {
                setDucks(data);
                setFeaturedDuck(data[0]);
            });
    }, []);
    function handleImgClick(duck) {
        console.log(duck);
        setFeaturedDuck(duck);
    }
    function handleLikeClick() {
        setDucks(
            ducks.map((duck) => {
                if (duck.id === featuredDuck.id) {
                    duck.likes = featuredDuck.likes + 1;
                }
                return duck;
            })
        );
        fetch("http://localhost:4001/ducks/" + featuredDuck.id, {
            method: "PATCH",
            headers: {
                "Content-Type": "application/json",
            },
            body: JSON.stringify({ likes: featuredDuck.likes }),
        });
    }
    function onDuckFormSubmit(event) {
        let newDuck = { name: newDuckName, img_url: newDuckUrl, likes: 0 };
        event.preventDefault();
        fetch("http://localhost:4001/ducks", {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
            },
            body: JSON.stringify(newDuck),
        })
            .then((res) => res.json())
            .then((data) => setDucks([...ducks, data]));
    }

    return (
        <div className="App">
            <h1>Duck Manager 2023 - React Edition</h1>

            <DuckList ducks={ducks} handleImgClick={handleImgClick} />

            <DuckDisplay
                duck={featuredDuck}
                handleLikeClick={handleLikeClick}
            />

            <button onClick={() => setDuckFormOpen(!duckFormOpen)}>
                {duckFormOpen ? "Close" : "Open"} Duck Form
            </button>

            {/* Conditionally display the duck form on the line below depending on whether the duckFormOpen state is true or false... */}
            {duckFormOpen ? (
                <DuckForm
                    onDuckFormSubmit={onDuckFormSubmit}
                    handleNameChange={(event) =>
                        setNewDuckName(event.target.value)
                    }
                    handleUrlChange={(event) =>
                        setNewDuckUrl(event.target.value)
                    }
                />
            ) : null}
        </div>
    );
}


export default App;
