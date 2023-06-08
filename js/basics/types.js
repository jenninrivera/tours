

//Booleans
let trueValue = true
let falseValue = false

console.log(`the type of trueValue ${trueValue}`)
//Numbers
let pi = 3.14
let three = 3

console.log(`type of the variable pi: ${pi}`)
console.log(`type of the variable three: ${three}`)

//Arrays

let array = [1,2,3] 


//Strings
let doubleQuotedString = "string"
let singleQuotedString = 'string' 

console.log(`type of the variable doubleQuotedString: ${doubleQuotedString}`)
//Objects

let obj = {
    text: "word",
    1: 2,
    nestedObject: {
        text: "different word"
    }
}

console.log(`Accessing the text field of obj with dot notation: ${obj.key}`)
console.log(`Accessing the text field of obj with bracket notation: ${obj.key}`)

console.log(`Accessing the nestedObject field from obj: ${obj.nestedObject}`)
console.log(`Accessing the text field field from nestedObject: ${obj.nestedObject.text}`)
//Array of Objects

let obj1 = { number: 1}
let obj2 = { number: 2}
let obj3 = { number: 3}
let arrayOfObj = [obj1, obj2, obj3]

console.log(`getting obj1 out of arrayOfObj: ${arrayOfObj[0]}`)
console.log(`getting obj1's number field: ${arrayOfObj[0].number}`)