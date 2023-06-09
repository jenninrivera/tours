

console.log(`true AND true: ${true && true}`)
console.log(`true AND false: ${true && false}`)

console.log(`true AND true AND true AND false: ${true && true && true && false}`)

console.log(`true OR true: ${true || true}`)
console.log(`true OR false: ${true || false}`)

console.log(`true OR false OR false OR false: ${true || false || false || false }`)


console.log(`NOT true: ${!true}`)
console.log(`NOT false: ${!false}`)

console.log(`NOT NOT true: ${!!true}`)
console.log(`NOT NOT false: ${!!false}`)

console.log(`Multiple logical expressions should be grouped by parentheses for clarity: ${(true && false) || (false || (true && false )}`)