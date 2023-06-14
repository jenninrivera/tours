

const ch1 = document.getElementById('1')

const section11 = document.getElementById('1.1')

const section11WithQuerySelector = ch1.querySelector('.section')


const allSections = document.querySelectorAll(".section")
const firstH1 = document.querySelector('h1')

const allSectionsInChapters = document.querySelectorAll('.chapter .section')


const ch1Sections = ch1.querySelectorAll('.section')


//ch1.style.color = 'red'

ch1Sections.forEach(sec => sec.innerText.replace('.','-'))

//ch1Sections.forEach(sec => sec.innerText = sec.innerText.replace('.','-'))

const img = document.createElement('img')
img.src = "https://i.imgur.com/2BhRYY6.jpeg"
firstH1.appendChild(img)
img.remove()



