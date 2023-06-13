
let toggle = true

const form = document.getElementById('formId')
const header = document.querySelector('h1')

form.addEventListener('submit', (e) =>{
    e.preventDefault()
    const p = document.createElement('p')
    p.innerText = e.target.name.value
    const greeting = document.querySelector('#greeting') 
    p.addEventListener('click', (e)=>{
        if(toggle){
            e.target.style.color = 'red'
            toggle = false
        }else{
            e.target.style.color = 'blue'
            toggle = true
        }
    })
    greeting.appendChild(p)
})

