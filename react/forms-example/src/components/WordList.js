import Word from "./Word.js";

function WordList({ words }) {
    console.assert(
        words.length !== undefined,
        "words prop in WordList is not an array"
    );
    return (
        <ul>
            {words.map((word) => (
                <Word key={word.text} 
                      text={word.text} 
                      origin={word.origin} />
            ))}
        </ul>
    );
}
export default WordList;
