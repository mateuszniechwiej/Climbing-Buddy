
// const form = document.getElementById('accept_climb');
// // to dispaly modal on page load as didn't work by calling it in a different way
// form.classList.add('show')
// form.style.display = 'block';


document.getElementById('submit_climb').onsubmit = event => {
    event.preventDefault()
    
        fields = {
            user: event.target.name.value,
            user_email: event.target.email.value,
            other_user: event.target.creator.value,
            other_email: event.target.receiver.value,
            message: event.target.message.value,
        }

        emailjs.send("gmail", "climbing_buddy", fields)
            .then(
                function () {
                    document.querySelector('.response').innerHTML = "Your message was sent!";
                },
                function() {
                    document.querySelector('.response').innerHtml = "There was an error to send your message. Try again later..."
                }
        )
         .catch(err => console.log(err))
    return false;

}


// function sendMail(acceptForm) {
//     acceptForm.preventDefault();
//     emailjs.send("gmail", "climbing_buddy", {
//         'user': acceptForm.name.value,
//         'user_email': acceptForm.email.value,
//         'other_user': acceptForm.creator.value,
//         'other_email': acceptForm.receiver.value,
//         'message': acceptForm.message.value,
//         })
//         .then(
//             function() {
//                 document.querySelector('.response').innerHTML = "Your message was sent!";
//             },
//             function() {
//                 document.querySelector('.response').innerHtml = "There was an error to send your message. Try again later..."
//             }
//         );
//     return false;
// }
