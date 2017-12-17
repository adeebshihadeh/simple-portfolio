function animate() {
  $(".card").hide();

  $(".jumbotron").fadeIn("slow");

  $(".card").first().slideDown("slow", function next() {
    $(this).parent().next().next().children().first().slideDown("slow", next);
  });
}

$(window).bind("load", function() {
  animate();
});