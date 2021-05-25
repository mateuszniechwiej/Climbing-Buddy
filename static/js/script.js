// TODO: // "flapickr" date and time picker 
// flatpickr('.flatpickr', {
//     enableTime: true,
//     time_24hr: true,
//     altInput: true,
//     altFormat: 'd M Y H:i',
//     dateFormat: 'Y-m-d H:i',

// });

// Dipsplaying different images depending on event type
const outdoor = document.querySelectorAll('.outdoor')
outdoor.forEach((image) => {
    image.src = "../static/images/outdoor.jpg"
});

const indoor = document.querySelectorAll('.indoor')
indoor.forEach((image) => {
    image.src = "../static/images/indoor.jpg"
});

// Modal script
const myModal = document.getElementById('myModal')
const myInput = document.getElementById('myInput')

myModal.addEventListener('shown.mdb.modal', () => {
  myInput.focus()
})