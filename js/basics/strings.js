

//Declaring
const testString = "words words"

//Interpolation
console.log("Combining strings with the plus operator " + "second part of the string")
console.log("Combining strings with other types using the plus operator: " + 1)

console.log(`Printing an interlopation string with some javascript code inside: ${5 + 5}`)
//Accessing characters
console.log(`the first character of a string: ${testString[0]}`)
console.log(`the length of a string: ${testString.length}`)
//Iterating
for(let character of testString){
    console.log(`printing characters of testString: ${character}` )
}
let arrayOfLetters = Array.from(testString)
console.log(`split string to an array ${arrayOfLetters}`)

let reconstructedString = arrayOfLetters.join('')
console.log(`join array of letters to a string ${reconstructedString}`)