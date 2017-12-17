function animate() {
  $(".card").hide();

  $(".card").first().slideDown("slow", function next() {
    $(this).parent().next().next().children().first().slideDown("slow", next);
  });
}

$(window).bind("load", function() {
  animate();
});