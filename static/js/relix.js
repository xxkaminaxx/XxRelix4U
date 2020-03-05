	$(".show-btn").click(function(){
  $(this).siblings(".artifact-description").toggle();
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
