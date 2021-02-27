const main = document.querySelector('.main')
const head_section = document.querySelector('.head')
const toggleTheme = document.querySelector('.toggle')
const DOMBody = document.querySelector('.DOMBody')
const theme = document.querySelectorAll('.theme')


const getTheme = localStorage.getItem('currentTheme')

if(getTheme == null) {
    changeTheme('dark')
} else {
    changeTheme(getTheme)
}

theme.forEach(elemet => {
    elemet.addEventListener('click', e => {
        let mode = elemet.dataset.mode
        changeTheme(mode)
    })
});


// Function to set theme
function changeTheme(mode){
    if (mode == 'light') {
        DOMBody.classList.add('theme-toggle')
    } else if(mode == 'dark') {
        DOMBody.classList.remove('theme-toggle')
    }

    // Saving theme to local storage
    localStorage.setItem('currentTheme', mode)
}

