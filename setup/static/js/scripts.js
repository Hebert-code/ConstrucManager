function button_onclick_menulateral(){
    let menulateral = document.querySelector(".menu-lateral");

    console.log("Entrou")

    if(menulateral.style.display === "none"){
        menulateral.style.display = "block";
    }else{
        menulateral.style.display = "none";
    }

}

function toggleMenu() {
    const menu = document.getElementById("menuLateral");
    const toggleButton = document.getElementById("toggleMenu");

    
    menu.classList.toggle("menu-hidden");

    if (menu.classList.contains("menu-hidden")) {
        toggleButton.innerHTML = "&#9776;"; 
    } else {
        toggleButton.innerHTML = "&#10006;"; // para fechar
    }
} 