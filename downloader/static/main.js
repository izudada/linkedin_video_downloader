let loader = document.getElementById('video_loader');
let submitButton = document.getElementById('submit');
let heading1 = document.getElementsByTagName("h1")[0];

// add event listener on submit button
submitButton.addEventListener('click', () => {
    // reduce the margin of the heading tag when spinner appears
    heading1.style.marginTop = "40vh";
    // remove hidden class from spinner
    loader.classList.remove('hidden');
})
