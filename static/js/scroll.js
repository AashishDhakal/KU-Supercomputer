fixNav = (e) => {
  let navbar = document.getElementById("navbar");
  let logo = document.getElementById("scrollLogo");
  if (window.scrollY) {
    navbar.classList.add("scroll");
    logo.classList.add("scroll-logo");
  } else {
    navbar.classList.remove("scroll");
    logo.classList.remove("scroll-logo");
  }
};

window.addEventListener("scroll", fixNav);
