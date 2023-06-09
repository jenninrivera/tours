
//comparisons
console.log(`Is 5 greater than 6? ${5 > 6}`)
console.log(`Is 5 less than 6? ${5 < 6}`)
console.log(`Is 5 greater than or equal to 5? ${5 >= 5}`)
console.log(`Is 5 less than or equal to 5? ${5 <= 5}`)

console.log(`Is 5 equal to 5? ${5 === 5}`)
console.log(`Is 5 not equal to 5? ${5 !== 5}`)
console.log(`Is the string "test" equal to the string "test"? ${'test' === 'test'}`)

let x = 0
let condition = x === 0
if(condition === true){
    console.log("condition x==0 is true, so we are inside the if statement")   
}

condition = x !== 0 
if(condition){
    console.log("we will never reach the inside of this if statement because the condition is false")
}else{
    console.log("we will always reach the inside of this else statement since the if condition is false")
}



if(x === 1){
    console.log("We will not reach here because the condition is false")
}else if(x === 2){
    console.log("We will not reach here because the condition is false")
}else if(x === 0){
    console.log("This prints because the condition in the second else if is true")
}else{
    console.log("This else statement is not reached because one of the else if conditions was true")

}


switch(x){
    case 0:
        console.log("x == 0 from a switch statement")
        break
    case 1:
        console.log("this will NEVER execute")
        break
    case 2:
        console.log("this will NEVER execute")
        break;
}