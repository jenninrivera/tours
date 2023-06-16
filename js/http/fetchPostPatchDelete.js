

const addedLang = {
    "name": "Prolog",
    "creator": "Colmerauer et al.",
    "year": 1972,
    "users": 0
}
const postRequestParameters = {
    method: "POST",
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify(addedLang)
}
/*
fetch("http://localhost:3000/langs",postRequestParameters)
    .then(response => response.json())
    .then(json => console.log(`response from the post ${JSON.stringify(json)}`))
    .catch(error => console.log(`error from post: ${error}`))
*/

const form = document.getElementById('langForm')
form.addEventListener('submit', (e) => {
    e.preventDefault()
    const name = e.target.name.value
    const year = e.target.year.value
    const creator = e.target.creator.value
    const users = 0

    const newLangObject = {
        "name": name,
        "year": year,
        "creator": creator,
        "users": users
    }

    fetch('http://localhost:3000/langs', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(newLangObject)
    }).then(response => response.json())
        .then(jsonData => addLangToPage(jsonData))
        .catch(error => console.log(`post error: ${error}`))
})
function addLangToPage(lang) {
    const langDiv = document.createElement('div')
    langDiv.innerText = `$Language: ${lang.name} Year: ${lang.year}`
    const postedLangs = document.getElementById('posted-langs')
    postedLangs.appendChild(langDiv)
}

const modification = {
    users: 999999
}

const patchRequestParameters = {
    method: "PATCH",
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify(modification)
}


//fetch("http://localhost:3000/langs/1",patchRequestParameters)
//    .then(response => response.json())
//    .then(data => console.log(data))



//fetch(`http://localhost:3000/langs/fillInANumber`,{method: 'DELETE'})


