

/*******************
 * Named Functions *
 *******************/
console.log(`calling increment before it was defined: ${increment(5)}`)

function logWithNoReturn(){
    console.log('in a function that takes no arguments and has no return')
}
var result = logWithNoReturn()
console.log(`printing the result of a function call with no return statement: ${result}`)
function increment(x){
    return x + 1
}

console.log(`calling increment after was defined: ${increment(5)}`)


const incrementFunctionInAConstant = increment

console.log(`printing a the increment function: ${incrementFunctionInAConstant}`)
console.log(`calling the increment function through a constant and printing the result: ${incrementFunctionInAConstant(2)}`)

const squaredConstant = function square(x){
    return x * x
}


/***********************
 * Anonymous Functions *
 ***********************/

// using the function keyword
console.log(`function keyword style anonymous function: ${function(){ return 5}}`)
console.log(`calling an anonymous function that returns 5: ${(function(){ return 5})()}`)
 
console.log(function(x){ return x + 5})
console.log((function(x){ return x + 5})(10))


// arrow function 
console.log(`arrow function that takes no parameters: ${() => 5}`)
console.log(`calling an arrow function that takes no parameters: ${(() => 5)()}`)

console.log(`arrow function takes one parameter ${x => x + 5}`)
console.log(`calling arrow function takes one parameter: ${(x => x + 5)(10)}`)


console.log(`arrow function that takes two parameters: ${(x, y) => x + y}`)
console.log(`calling an arrow function that takes two parameters: ${((x, y) => x + y)(2,3)}`)
const add = (x, y) => x + y 
console.log(`the constant add containing an arrow function: ${add}`)
console.log(`calling the function in the constant add with the arguments 5 and 6: ${add (5,6)}`) 

console.log(`arrow function with curly braces: ${() => {let x = 5; return x;}}`)
const anonFuncNoParams = () => {
  let x = 5
  console.log(`printing a local variable from an anonymous function ${x}`)
  return x
}

const anonFuncOneParam = x => {
 console.log(`printing a parameter from an anonymous function ${x}`) 
 return x
}

const anonFuncTwoParams = (x, y) => {
  return x + y
}

console.log(`anonFuncNoParams ${anonFuncNoParams()}`)
console.log(`anonFuncOneParam ${anonFuncOneParam(19)}`)
console.log(`anonFuncTwoParams ${anonFuncTwoParams(5, 6)}`)

