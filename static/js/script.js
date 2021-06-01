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

// Modals script
const acceptModal = document.querySelector('#accept_climb')
const acceptFocus = document.querySelector('#message')
const deleteModal = document.querySelector('.delete') 

acceptModal.addEventListener('shown.mdb.modal', () => {
    acceptFocus.focus()
});

deleteModal.addEventListener('shown.mdb.modal', () => {

});

