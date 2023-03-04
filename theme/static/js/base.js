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

// navbar_btn.addEventListener("click", touch_menu, false);
contact_btn.addEventListener("click", function (){
    contact.classList.remove("hidden");
    document.getElementById("id_email").value = cta_email.value;

}, false)
contactBtn.addEventListener("click", function (){contact.classList.add("hidden")})

var year = document.getElementById("year").innerHTML = new Date().getFullYear();

const observer  = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
        if (entry.isIntersecting) {
            entry.target.classList.replace("opacity-0", "opacity-100");
        }
    });
});

const elements = document.querySelectorAll(".animate");
elements.forEach(element => {
    observer.observe(element);
});


const textAnimation = document.querySelectorAll(".text-animation");
const textAnimationRight = document.querySelectorAll(".text-animation-right");

animation(textAnimation, "text-animation", "text-animation-active");

setTimeout(() => {
    animation(textAnimationRight, "text-animation-right", "text-animation-right-active");
}, 30000);

const observerBackground  = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
        if (entry.isIntersecting) {
            entry.target.scrollIntoView({behavior: "smooth", block: "start", inline: "nearest",});
        }
    });
});

const elementsBackground = document.querySelectorAll(".background");
elementsBackground.forEach(element => {
    observerBackground.observe(element);
});


