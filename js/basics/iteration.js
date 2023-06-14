

const numbers = [1,2,3,4,5]

let arrayIndex = 0
let total = 0
//while loop
while(arrayIndex < numbers.length){
    total = total + numbers[arrayIndex]
    arrayIndex = arrayIndex + 1
}

console.log(`total after while loop: ${total}`)

//for loop
total = 0
for(let i = 0; i < numbers.length; i++){
    total += numbers[i]
}
console.log(`total after for loop: ${total}`)

//for/of loop
total = 0
for(let num of numbers){
    total += num
}
console.log(`total after for/of loop: ${total}`)

total = 0
for(let num of numbers){
    if(num % 2 === 1) {
        total += num;
    }
}

console.log(`total of only odd numbers: ${total}`)

let letters = ['a','b','c','d']
for(let num of numbers){
    for(let letter of letters){
        console.log(`number ${num}\nletter ${letter}\n `)
    }


}
numbers.forEach(num => {
    letters.forEach(letter => {
        console.log(`number ${num}\nletter ${letter}\n `)

    })
})