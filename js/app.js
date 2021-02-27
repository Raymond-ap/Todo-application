const main = document.querySelector('.main')
const head_section = document.querySelector('.head')
const toggleTheme = document.querySelector('.toggle')
const DOMBody = document.querySelector('.DOMBody')



toggleTheme.addEventListener('click', () => {
    toggleTheme.classList.toggle('mode')
    DOMBody.classList.toggle('theme-toggle')
    window.localStorage.toggle = 'theme-toggle'
})

if (window.location.toggle == 'theme-toggle') {
    
} else {
    
}