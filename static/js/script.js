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
const acceptModal = document.getElementById('accept_climb')
const acceptfocus = document.getElementById('message')
const deleteModal = document.getElementByClassName('delete')
const deletefocus = document.getElementById('')

const deleteModal = document.getElementsByClassName('delete') 

acceptModal.addEventListener('shown.mdb.modal', () => {
    myInput.focus()
});

deleteModal.addEventListener('shown.mdb.modal')
    