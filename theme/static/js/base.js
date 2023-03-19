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

let navbar = document.getElementById("navbar");
let logo = document.getElementById("logo");
let logoBtn = document.getElementById("logo-btn");
let navSide = document.querySelectorAll(".nav-side");

let path = window.location.pathname;
if (path != "/"){
    navbar.classList.replace("absolute", "sticky");
}

let navState = {
    active:function(){
        logo.classList.add("rollingOut");
        logo.classList.remove("rollingIn");
        navbar.classList.remove("bg-black");
        navbar.classList.replace("fixed", "absolute");
        navbar.classList.replace("absolute", "fixed");
        navSide.forEach(function(item){
            item.classList.add("hidden");
        });
    },
    inactive:function(){
        logo.classList.remove("rollingOut");
        logo.classList.add("rollingIn");
        setTimeout(function(){
            navbar.classList.add("bg-black");
            navSide.forEach(function(item){
                item.classList.remove("hidden");
            }, 3000);
        });
    }
}

let state = false;

function showNav(){
    navState.inactive();
    setTimeout(function(){
        logoBtn.setAttribute("href", "/");
    }, 500);
    state = false;
}


window.addEventListener("scroll", function(){
    let st = window.pageYOffset 
    
    if (st > 0 && state == false){
        console.log("active");
        state = true;
        navState.active();
        logoBtn.removeAttribute("href");
        logoBtn.addEventListener("click", showNav, false);
        logoBtn.addEventListener("touchstart", showNav, false);
    } else if (st == 0 && state == true) {
        console.log("inactive");
        navState.inactive();
        logoBtn.setAttribute("href", "/");
        state = false;
    }
}, false);


