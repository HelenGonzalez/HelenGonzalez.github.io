$(document).ready(function(){
  var card_array = ["fish", "fish", "turtle", "turtle", "pig", "pig", "dog", "dog", "cat", "cat", "snake", "snake", "bird", "bird", "goat", "goat", "hamster", "hamster", "dragon", "dragon"]

  for(i in card_array){
    $('#card_holder').append('<div class="card"><p>'+card_array[i]+'</p></div>');
  }
});
var card1="none"
//making the cards appear
$('.card')on ('click',function()){
  $mycard=(this). find('p');
  $mycard.css('opacity',1);
  card1=$mycard.html();
});
