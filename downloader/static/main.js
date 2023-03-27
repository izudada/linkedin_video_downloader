let loader = document.getElementById('video_loader');
let downloadButton = document.getElementById('download');
let action = document.getElementById("action-text");
let anchorTag = document.getElementById("download-anchor");
let urlInput = document.getElementById("url");
let footer = document.getElementsByTagName('footer')[0];
let web_date = document.getElementById("date");

const validateLinkedInPost = (url) => {
    /*
        A function that validates a linkedin post
    */
    var pattern = /\/posts\/([a-zA-Z0-9\-]+)/;
    var match = url.match(pattern);
    if (match && match[1]) {
        var postId = match[1];
        // You can now check if the postId is valid using the LinkedIn API or any other method
        return true;
    } else {
        return false;
    }
      
};


$('#url').on('keyup input', function() {
    let url = document.getElementById("url").value;
    if (validateLinkedInPost(url)) {
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
    } else {
        $('.flash').remove();
        $("main").prepend(`
            <div class="flash">
                <div class="danger">Invalid url. Please paste a valid LinkedIn url</div>
            </div>
        `);
        $('.flash').fadeOut(7000);
        $('#url').val('');
    }
});


const d = new Date().getFullYear();
web_date.innerHTML = "&copy; " + d ;
footer.classList.add('footer_class');
