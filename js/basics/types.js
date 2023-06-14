

//Booleans
let trueValue = true
let falseValue = false

console.log(`the type of trueValue ${typeof trueValue}`)
//Numbers
let pi = 3.14
let three = 3

console.log(`type of the variable pi: ${typeof pi}`)
console.log(`type of the variable three: ${typeof three}`)



//Strings
let doubleQuotedString = "string"
let singleQuotedString = 'string' 

console.log(`type of the variable doubleQuotedString: ${doubleQuotedString}`)
//Objects
//--Arrays
let numbers = [1,2,3]
console.log(`The type of an array is: ${typeof numbers}`)
console.log(`The first element of an array: ${numbers[0]}`)
console.log(`The length of an array: ${numbers.length}`)

//--JSON
let obj = {
    text: "word",
    array: [1,2,3],
    nestedObject: {
        text: "different word"
    }
}
console.log(`The type of an object is: ${typeof obj}`)
console.log(`Accessing the text field of obj with dot notation: ${obj.text}`)
console.log(`Accessing the text field of obj with bracket notation: ${obj['text']}`)

console.log(`Accessing the nestedObject field from obj: ${obj.nestedObject}`)
console.log(`Accessing the text field field from nestedObject: ${obj.nestedObject.text}`)
//Array of Objects

let obj1 = { number: 1}
let obj2 = { number: 2}
let obj3 = { number: 3}
let arrayOfObj = [obj1, obj2, obj3]

console.log(`getting obj1 out of arrayOfObj: ${arrayOfObj[0]}`)
console.log(`getting obj1's number field: ${arrayOfObj[0].number}`)
