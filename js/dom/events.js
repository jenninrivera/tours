
let toggle = true

const form = document.getElementById('formId')


form.addEventListener('submit', (e) => {
    e.preventDefault()
    console.log(e)
    const p = document.createElement('p')
    p.innerText = e.target.formName.value
    const greeting = document.querySelector('#greeting') 
    p.addEventListener('click', (e)=>{
        if(toggle){
            e.target.innerText === 'test' ? e.target.style.color = 'red' 
                                          : e.target.style.color = 'magenta'
            
            toggle = false
        }else{
            e.target.style.color = 'blue'
            toggle = true
        }
    })
    greeting.appendChild(p)
})
const header = document.querySelector('h2')

header.addEventListener('click', () => {
    toggle ? document.body.style.background = 'lightblue' 
           :  document.body.style.background = 'yellow'
    toggle = !toggle 
})
