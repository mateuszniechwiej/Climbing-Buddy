// Add focus in modal on message field
const myModal = document.getElementById('message_climber');
const message = document.getElementById('message');

myModal.addEventListener('shown.mdb.modal', () => {
    message.focus();
});