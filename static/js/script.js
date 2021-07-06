//  "flatpickr" date picker
flatpickr('.flatpickr', {
    minDate: "today",
    enableTime: false,
    altInput: true,
    altFormat: 'd M Y',
    dateFormat: 'Y-m-d',
    wrap: true
});

// Dipsplaying different images depending on event type
const outdoor = document.querySelectorAll(".outdoor");
outdoor.forEach((image) => {
  image.src = "../static/images/outdoorOpt.jpg";
});

const indoor = document.querySelectorAll(".indoor");
indoor.forEach((image) => {
  image.src = "../static/images/indoorOpt.jpg";
});

// Modals script
const myModal = document.getElementById("accept_climb");
const modal = new mdb.Modal(myModal)
modal.show()

// Modals.forEach(modal => {
//     modal.addEventListener("shown.mdb.modal", () => {
//         acceptFocus.focus()
//     })
// });

// Pagination 

