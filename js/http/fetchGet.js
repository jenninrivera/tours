


fetch("http://localhost:3000/langs")
    .then(response => { 
        console.log("response object:")
        console.log(response)
    })

fetch("http://localhost:3000/langs")
    .then(response => {
        console.log("JSON promise:")
        console.log(response.json())
    })

fetch("http://localhost:3000/langs")
    .then(response => 5)
    .then(randomName => console.log(randomName))

fetch("http://localhost:3000/langs")
.then(response => response.json())
.then(langs => langs.forEach(lang => console.log(lang)))
.catch(error => console.log(`printing the error: ${error}`))

console.log("This runs before the fetch")

fetch("https://www.dnd5eapi.co/api/spells/silence")
.then(response => response.json())
.then(json => console.log(json))
