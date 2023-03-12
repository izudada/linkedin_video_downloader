let loader = document.getElementById('video_loader');
let submitButton = document.getElementById('submit');
let heading1 = document.getElementsByTagName("h1")[0];
let action = document.getElementById("action-text");


function inputListener() {
    let url = document.getElementById("url").value;
    heading1.style.marginTop = "28vh";
    loader.classList.remove('hidden');
    action.classList.remove("hidden");
    $.ajax({
        type: 'POST',
        url : `/`,
        data: {"url": url},
        success: function(response){
            console.log(response)
            loader.classList.add('hidden');
            action.classList.add("hidden");
            submitButton.classList.remove('hidden');
        },
        error: function(error) {
            console.log(error)
        }
    })
}