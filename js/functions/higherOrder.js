


const numbers = [1,2,3,4,5]


//forEach

numbers.forEach(num => console.log(num))

//map
function increment(x){
    return x + 1
}
console.log(`passing a named function to map ${numbers.map(increment)}`)

console.log(`passing an anonymous function to map ${numbers.map(num => num + 1)}`)

//filter

const odds = numbers.filter(num => {
    if(num % 2 == 1){
        return true
    }else{
        return false
    }
})


console.log(`odd numbers in numbers array: ${odds}`)
console.log(`odd numbers in numbers array: ${numbers.filter(num => num % 2 == 1)}`)

//reduce

//from https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/reduce
let initialValue = 0
let total = numbers.reduce((accumulator, currentValue) => accumulator + currentValue, initialValue)