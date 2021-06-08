// TODO: // "flapickr" date and time picker
flatpickr('.flatpickr', {
    enableTime: true,
    time_24hr: true,
    altInput: true,
    altFormat: 'd M Y H:i',
    dateFormat: 'Y-m-d H:i',
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
const Modals = document.querySelectorAll(".modal");
const acceptFocus = document.querySelector("#message");

Modals.forEach(modal => {
    modal.addEventListener("shown.mdb.modal", () => {
        acceptFocus.focus()
    })
});