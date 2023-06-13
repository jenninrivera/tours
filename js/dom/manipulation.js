

const ch1 = document.getElementById('1')

const section11 = document.getElementById('1.1')

const section11WithQuerySelector = ch1.querySelector('.section')


const allSections = document.querySelectorAll(".section")

const allSectionsInChapters = document.querySelectorAll('.chapter .section')

//chapter1.style.color = 'red'

const ch1Sections = ch1.querySelectorAll('.section')

ch1Sections.forEach(sec => sec.innerText = sec.innerText = sec.innerText.replace('.','-'))
ch1Sections.forEach(sec => sec.innerText.replace('.','-'))


ch1Sections.forEach(sec => sec.innerText = sec.innerText = sec.innerText.replaceAll('.','-'))


