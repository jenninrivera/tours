

const addedLang = {
    "name":"Prolog",
    "creator":"Colmerauer et al.",
    "year": 1972,
    "users":0
}
const postRequestParameters = {
    method:"POST",
    headers:{'Content-Type':'application/json'},
    body:JSON.stringify(addedLang)
}
fetch("http://localhost:3000/langs",postRequestParameters)
    .then(response => response.json())
    .then(json => console.log(`response from the post ${JSON.stringify(json)}`))
    .catch(error => console.log(`error from post: ${error}`))



const modification = {
    users:999999
}

const patchRequestParameters = {
    method:"PATCH",
    headers:{'Content-Type':'application/json'},
    body:JSON.stringify(modification)
}


fetch("http://localhost:3000/langs/1",patchRequestParameters)



fetch(`http://localhost:3000/langs/fillInANumber`,{method: 'DELETE'})


