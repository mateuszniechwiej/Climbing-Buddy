function sendMail() {
    emailjs.send("gmail", "climbing_buddy", {
        user: user, user_email: user_email, other_user: other_user, other_email: other_email
    })
    .then(function(response) {
        console.log('SUCCESS!', response.status, response.text);
     }, function(error) {
        console.log('FAILED...', error);
     });
    
}