
fetch('http://localhost:3000/ducks')
    .then(response => response.json())
    .then(duckList => duckList.forEach(duck => addDuckToNav(duck)))
    .catch(error => console.log(`Error with GET request to /ducks: ${error}`))

function addDuckToNav(duck) {
    const duckNav = document.querySelector('#duck-nav')
    const duckImgElement = document.createElement('img')
    const duckImgURL = duck.img_url

    duckImgElement.src = duckImgURL
    duckNav.appendChild(duckImgElement)

    duckImgElement.addEventListener('click', () => {
        const duckDisplayImg = document.querySelector('#duck-display-image')
        const duckDisplayName = document.querySelector('#duck-display-name')
        const duckDisplayLikesButton = document.querySelector('#duck-display-likes')

        duckDisplayImg.src = duck.img_url
        duckDisplayName.innerText = duck.name
        duckDisplayLikesButton.innerText = duck.likes + " Likes"

        duckDisplayLikesButton.addEventListener('click', () => {
            duck.likes++
            duckDisplayLikesButton.innerText = duck.likes + " Likes"
        })
    })
}
const newDuckForm = document.querySelector('#new-duck-form')
newDuckForm.addEventListener('submit', (e) => {
    e.preventDefault()
    const duckName = e.target['duck-name-input'].value
    const duckImgURL = e.target['duck-image-input'].value
    const newDuckObject = {
        name: duckName,
        img_url: duckImgURL,
        likes: 0
    }
    addDuckToNav(newDuckObject)

})