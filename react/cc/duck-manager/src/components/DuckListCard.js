function DuckListCard({ duck, handleImgClick }) {
    return (
        <img
            src={duck.img_url}
            alt={duck.name}
            onClick={() => handleImgClick(duck)}
        />
    );
}

export default DuckListCard;
