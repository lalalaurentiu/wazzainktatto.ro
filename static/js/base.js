const navbar_elements = document.getElementById("navbar");
const navbar_btn = document.querySelector("#navbar_btn");
const contact = document.getElementById("contact");
const contact_btn = document.getElementById("contact_btn");
const contactBtn = document.getElementById("contactBtn");
const cta_email = document.getElementById("cta-email");

function touch_menu(){
    if (navbar_elements.classList.contains("-translate-y-full")){
        navbar_elements.classList.replace("-translate-y-full", "translate-y-0");

    } else {
       navbar_elements.classList.replace("translate-y-0", "-translate-y-full");
    };
    
};

navbar_btn.addEventListener("click", touch_menu, false);
contact_btn.addEventListener("click", function (){
    contact.classList.remove("hidden");
    document.getElementById("id_email").value = cta_email.value;

}, false)
contactBtn.addEventListener("click", function (){contact.classList.add("hidden")})
