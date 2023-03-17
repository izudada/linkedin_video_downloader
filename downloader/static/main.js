let loader = document.getElementById('video_loader');
let downloadButton = document.getElementById('download');
let action = document.getElementById("action-text");
let anchorTag = document.getElementById("download-anchor");
let urlInput = document.getElementById("url");


$('#url').on('keyup input', function() {
    let url = document.getElementById("url").value;
    if (url.length > 0){
        loader.classList.remove('hidden');
        action.classList.remove("hidden");
        $.ajax({
            type: 'POST',
            url : `/`,
            data: {"url": url},
            success: function(response){
                anchorTag.setAttribute("href", `/download/${response.fileName}`);
                loader.classList.add('hidden');
                action.classList.add("hidden");
                downloadButton.classList.remove('hidden');
            },
            error: function(error) {
                console.log(error)
            }
        })
    }
});
