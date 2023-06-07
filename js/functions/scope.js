

var x = 5
var y = 0
function f(x){
    console.log(`the value of the globally scoped variable y inside a function: ${y}`)
    x = 6
    console.log(`the value of the parameter x: ${x}`)
    if(x == 6){
        console.log(`the value of the globally scoped variable y inside a block: ${y}`)
        var x = 7
        console.log(`the value of the block scoped variable x: ${x}`)
    }
    console.log(`the value of the function scoped variable x: ${x}`)
    y = 1
}

console.log(`the value of the globally scoped variable x: ${x}`)
console.log(`the value of the globally scoped variable y before the function call: ${y}`)
f(x)
console.log(`the value of the globally scoped variable y: ${y}`)
console.log(`the value of the function scoped variable x: ${x}`)