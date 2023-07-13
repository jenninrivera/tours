import React from "react";
import DuckListCard from "./DuckListCard";
function DuckList({ ducks, handleImgClick }) {
    return (
        <div className="duck-nav">
            {/* display the duck card components here */}
            {ducks.map((duck) => (
                <DuckListCard
                    key={duck.img_url + duck.id}
                    duck={duck}
                    handleImgClick={handleImgClick}
                />
            ))}
        </div>
    );
}

export default DuckList;
