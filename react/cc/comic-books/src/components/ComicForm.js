function ComicForm({ updateFormData, addComic }) {
    return (
        <form className="comic-form" onSubmit={addComic}>
            <h2>Add A New Issue</h2>

            <label htmlFor="image_url">Image URL: </label>
            <input name="image_url" onChange={updateFormData} />

            <label htmlFor="title">Title: </label>
            <input name="title" onChange={updateFormData} />

            <label htmlFor="issue">Issue Number: </label>
            <input name="issue" type="number" onChange={updateFormData} />

            <input type="submit" value="Add Issue" />
        </form>
    );
}

export default ComicForm;
