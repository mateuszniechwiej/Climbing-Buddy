// sending email to climb creators and passing the appropriate information by using email.js
document.getElementById('message_climber').onsubmit = event => {
    event.preventDefault();
    
    fields = {
        user: event.target.name.value,
        user_email: event.target.email.value,
        other_user: event.target.creator.value,
        other_email: event.target.receiver.value,
        message: event.target.message.value,
    };

    emailjs.send("gmail", "climbing_buddy", fields)
        .then(
            function () {
                document.querySelector('.response').innerHTML = "Your message was sent!";
            },
            function () {
                document.querySelector('.response').innerHtml = "There was an error to send your message. Try again later...";
            }
        )
        .catch(err => console.log(err));
    return false;

};
