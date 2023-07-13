import React from "react";

function DuckForm({
    name,
    url,
    onDuckFormSubmit,
    handleNameChange,
    handleUrlChange,
}) {
    return (
        <form id="new-duck-form" onSubmit={onDuckFormSubmit}>
            <label htmlFor="duck-name-input">New Duck Name:</label>
            <input
                type="text"
                name="duck-name-input"
                value={name}
                onChange={handleNameChange}
            />

            <label htmlFor="duck-image-input">New Duck Image URL:</label>
            <input
                type="text"
                name="duck-image-input"
                value={url}
                onChange={handleUrlChange}
            />

            <input type="submit" value="Create Duck" />
        </form>
    );
}

export default DuckForm;
