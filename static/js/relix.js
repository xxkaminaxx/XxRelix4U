$(document).ready(function() {
    document.getElementById("h3").addEventListener("mouseover",  function() {
       showDescription();
    });
  document.getElementById("h3").addEventListener("mouseleave",  function() {
       hideDescription();
    });





    function showDescription() {
      $("#artifact-description").style.display = "flex";
}

  function hideDescription() {
    $("#artifact-description").style.display = "none";
}  



    });