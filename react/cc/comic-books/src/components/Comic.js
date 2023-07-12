import React, {useState} from "react"
function Comic({comic, removeComic }) {

    const [showImage, setShowImage] = useState(true)
    if(showImage){
        return ( <div className="comic-item" onClick={() => setShowImage(!showImage)}>
                 <img src={comic.image_url} alt={comic.title} />
                 </div>)
    }else{
        return ( <div className="comic-item" onClick={() => setShowImage(!showImage)}>
                 <h3>{comic.title}</h3>
                 <h4>{comic.issue}</h4>
                 <button onClick={() => removeComic(comic.id)}>Remove</button>
                 </div>
               )

    }
}

export default Comic
