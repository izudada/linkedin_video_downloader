let loader = document.getElementById('video_loader');
let submitButton = document.getElementById('submit');
let heading1 = document.getElementsByTagName("h1")[0];


// function to stop spinner after 10secs 
function stopSpinner (){
    // add hidden class from spinner
    loader.classList.add('hidden');
 }

// add event listener on submit button
submitButton.addEventListener('click', () => {

    // reduce the margin of the heading tag when spinner appears
    heading1.style.marginTop = "40vh";
    // remove hidden class from spinner
    loader.classList.remove('hidden');

})

// spinner timeout
const myTimeout = setTimeout(stopSpinner, 8000);