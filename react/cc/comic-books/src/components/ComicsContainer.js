import Comic from "./Comic";

function ComicsContainer({ comics, removeComic }) {
    return (
        <div className="flex-container">
            {comics.map((comic) => {
                return (
                    <Comic
                        key={comic.id}
                        comic={comic}
                        removeComic={removeComic}
                    />
                );
            })}
        </div>
    );
}

export default ComicsContainer;
