const btnCloseModal = document.querySelectorAll(".close-modal");
const modalTransaction = document.querySelector(".transaction-modal");
const modalCategory = document.querySelector(".category-modal");
const overlay = document.querySelector(".overlay");

const openModalTransaction = function () {
  window.scrollTo(0,0);
  modalTransaction.classList.remove("hidden");
  overlay.classList.remove("hidden");
};

const openModalCategory = function () {
  window.scrollTo(0,0);
  modalCategory.classList.remove("hidden");
  overlay.classList.remove("hidden");
};

const closeModal = function () {
  modalCategory.classList.add("hidden");
  modalTransaction.classList.add("hidden");
  overlay.classList.add("hidden");
  document.body.style.overflow = 'visible';
};

btnCloseModal.forEach((btn)=>{
  btn.addEventListener("click", closeModal);
})

overlay.addEventListener("click", closeModal);

const openTransactionModal = () => openModalTransaction();
const openCategoryModal = () => openModalCategory();

document.addEventListener("DOMContentLoaded", function () {
  var splide = new Splide(".splide");
  splide.mount();
});
