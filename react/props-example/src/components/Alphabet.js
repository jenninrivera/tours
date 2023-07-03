

function Alphabet({alphabet, word}){
    console.assert(typeof(alphabet) === 'string', 'alphabet prop in Alphabet.js should be a string')
    console.assert(typeof(word) === 'string', 'word prop in Alphabet.js should be a string')

    return (
        <div>
           <li>{alphabet}</li>
           <ul>
            <li>Example word: {word}</li>
            </ul> 
        </div>
    )
}
export default Alphabet