

let numbers = [1,2,3,4,5]
let total = 0

let arrayIndex = 0
while(arrayIndex < numbers.length){
    total = total + numbers[arrayIndex]
    arrayIndex = arrayIndex + 1
}

console.log(`total after while loop: ${total}`)

total = 0
for(let i = 0; i < numbers.length; i++){
    total += numbers[i]
}
console.log(`total after for loop: ${total}`)

total = 0
for(let num of numbers){
    total += num
}

console.log(`total after for/of loop: ${total}`)