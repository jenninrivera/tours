

let x = 5
let y = 0
function f(x){
    console.log(`the value of the globally scoped variable y inside a function: ${y}`)
    x = 6
    console.log(`the value of the parameter x: ${x}`)
    if(x === 6){
        console.log(`the value of the globally scoped variable y inside a block: ${y}`)
        let z = 7
        console.log(`the value of the block scoped variable z: ${z}`)
    }
    //console.log(`the value of the function scoped variable x: ${z}`)
    y = 1
}

console.log(`the value of the globally scoped variable x: ${x}`)
console.log(`the value of the globally scoped variable y before the function call: ${y}`)
f(x)
console.log(`the value of the globally scoped variable y: ${y}`)
console.log(`the value of the function scoped variable x: ${x}`)