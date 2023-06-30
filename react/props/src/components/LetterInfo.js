
function LetterInfo({symbol, isVowel}){
    console.assert(typeof(isVowel) === 'boolean', "isVowel prop in LetterInfo is wrong type")
    console.assert(symbol.lowerCase != null, 'symbol prop in LetterInfo has no property lowerCase')
    return (
        <div>
            <h3>Upper Case: {symbol.upperCase}</h3>
            <h3>Lower Case: {symbol.lowerCase}</h3>
            <h3>{symbol.isVowel ? "Vowel" : "Consonant" }</h3>
        </div>
    )
}
export default LetterInfo