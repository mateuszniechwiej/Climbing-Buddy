
function sendMail(acceptForm) {
  emailjs
    .send("gmail", "climbing_buddy", {
      user: acceptForm.name.value,
      user_email: acceptForm.email.value,
      other_user: acceptForm.creator.value,
      other_email: acceptForm.receiver.value,
      message: acceptForm.message.value,
    })
    .then(
      function () {
        document.querySelector('.response').innerHTML = "Your message was sent!";
      },
      function () {
        document.querySelector('.response').innerHtml = "There was an error to send your message. Try again later..."
      }
    );
  return false;
}
