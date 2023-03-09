let slides = document.querySelectorAll(".Slides");
let interactionBtn = [
  document.querySelector(".prev"),
  document.querySelector(".next"),
  document.querySelector(".close"),
];
let slideIndex = 1;

function plusSlides(n) {
  showSlides((slideIndex += n));
}

function currentSlide(n) {
  showSlides((slideIndex = n));
}

function showSlides(n) {
  let i;
  if (n > slides.length) {
    slideIndex = 1;
  }
  if (n < 1) {
    slideIndex = slides.length;
  }

  for (i = 0; i < slides.length; i++) {
    if (slides[i].classList.contains("active-slide")) {
      slides[i].classList.remove("active-slide");
    }
    slides[i].style.display = "none";
  }

  slides[slideIndex - 1].classList.add("active-slide");
  slides[slideIndex - 1].style.display = "block";
  slides[slideIndex - 1].scrollIntoView({ block: "end" });
  interactionBtn.forEach((element) => {
    element.classList.remove("hidden");
  });
}

document.querySelector(".close").addEventListener("click", () => {
  interactionBtn.forEach((element) => {
    element.classList.add("hidden");
  });
  slides.forEach((element) => {
    element.classList.remove("active-slide");
    element.removeAttribute("style");
  });
  slides[slideIndex - 1].scrollIntoView({ block: "end" });
});

slides.forEach((element, index) => {
  element.addEventListener("click", () => {
    currentSlide(index + 1);
    element.removeAttribute("style");
  });
});
