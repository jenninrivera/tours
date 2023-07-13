import React from "react";

function DuckDisplay({ duck, handleLikeClick }) {
    return (
        <div className="duck-display">
            {/* show all the details for the featuredDuck state here */}

            <h2>{duck.name}</h2>

            <img src={duck.img_url} alt={duck.name} />

            <button onClick={handleLikeClick}>{duck.likes} likes</button>
        </div>
    );
}

export default DuckDisplay;
