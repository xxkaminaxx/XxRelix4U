$(document).ready(function() {
    // hides or shows description
    $("#show-btn").click(function(){
        $("#artifact-description").toggle(500);
    });

    window.onscroll = function() {scrollFunction();};

function scrollFunction() {
  if (document.body.scrollTop > 500 || document.documentElement.scrollTop >500) {
    document.getElementById("TopBtn").style.display = "block";
  } else {
    document.getElementById("TopBtn").style.display = "none";
  }
}

// When the user clicks on the button, scroll to the top of the document
function topFunction() {
  document.body.scrollTop = 0; // For Safari
  document.documentElement.scrollTop = 0; // For Chrome, Firefox, IE and Opera
}

// Taken from MS1  

});