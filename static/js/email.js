const response = document.querySelector('.response')

function sendMail(acceptForm) {
  emailjs
    .send("gmail", "climbing_buddy", {
      user: user,
      user_email: user_email,
      other_user: other_user,
      other_email: other_email,
      message: acceptForm.message.value,
    })
    .then(
      function () {
        response.innerHTML = "Your message was sent!";
      },
      function () {
        response.innerHtml = "There was an error to send your message. Try again later..."
      }
    );
  return false;
}
