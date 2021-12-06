document.addEventListener('DOMContentLoaded', function () {
  var modeSwitch = document.querySelector('.mode-switch');

  modeSwitch.addEventListener('click', function () {
    document.documentElement.classList.toggle('dark');
  });
});
function openFinder(elem){

    var slides = document.getElementsByClassName("card-text big cardText-js");


    for (var i = 0; i < slides.length; i++) {
       city_to_find = String(document.getElementById("find_city").value).replace(/\s/g, '').toLowerCase();
       city=String(slides.item(i).getAttribute('value')).replace(/\s/g, '').toLowerCase();

       if (city == city_to_find){
            slides.item(i).parentElement.parentElement.style.visibility = 'visible';
       }else if (city_to_find == "todas" || city_to_find == "" ){
            slides.item(i).parentElement.parentElement.style.visibility = 'visible';
       }else {
            slides.item(i).parentElement.parentElement.style.visibility = 'hidden';
       }
    }

}
function openModal(elem){
    elemento = elem.id.replaceAll(`'`, `"`);
    var elemento = JSON.parse(elemento)

    ascensor = ""
    format_date = elemento["valuation_date"].slice(0, -9)

    if (elemento["elevator"] == "1"){
        ascensor = "tiene ascensor"

    }else{
        ascensor = "no tiene ascensor"
    }

    description = "Piso situado en " +elemento["city"]+ " con código postal " +elemento["cp"]+
                   " y con latitud " +elemento["latitude"]+ " y longitud " +elemento["longitude"]+
                   ". El piso se construyó en elaño " +elemento["year_const"]+
                   ". Consta de una superficie de " +elemento["total_area"]+ " m2 con un valor de "+elemento["price_m2"]+
                   "€ por metro cuadrado. La vivienda " +ascensor+" y su fecha de evaluación es " +
                   format_date+ ". La última reforma corresponde al año "+elemento["year_renovation"] +"."



  let modal= document.querySelector('#modal-window');
  modal.classList.add("showModal");
    document.getElementById('id_total_price').innerHTML =elemento["total_price"] +"€";
    document.getElementById('id_street').innerHTML =elemento["address"];
    document.getElementById('id_city').innerHTML =elemento["city"];
    document.getElementById('id_total_area').innerHTML =elemento["total_area"] +" m2";
    document.getElementById('id_elevator').innerHTML =ascensor;
    document.getElementById('id_description').innerHTML =description;
    document.getElementById('id_img').src =elemento["img_url"];


}


function closeM(){
    let m= document.querySelector('#modal-window');
  m.classList.remove("showModal");
}

document.getElementsByClassName('.mode-switch').onclick = function() {
  document.body.classList.toggle('dark');
}

const cardItems = document.querySelectorAll('.main-card');
const modalHeader = document.querySelector('.modalHeader-js');
const modalCardPrice = document.querySelector('.amount');

cardItems.forEach((cardItem) => {
  cardItem.addEventListener('click', function () {
    const cardHeader = cardItem.querySelector('.cardText-js');
    const cardPrice = cardItem.querySelector('.card-price');

    modalHeader.innerText = cardHeader.innerText;
    modalCardPrice.innerText = cardPrice.innerText;
  });
});

window.onkeydown = function (event) {
  if(event.keyCode == 27) {
    closeM();
  }
}

