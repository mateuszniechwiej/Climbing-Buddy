

// Dipsplaying different images depending on event type
const outdoor = document.querySelectorAll(".outdoor");
outdoor.forEach((image) => {
  image.src = "../static/images/outdoorOpt.jpg";
});

const indoor = document.querySelectorAll(".indoor");
indoor.forEach((image) => {
  image.src = "../static/images/indoorOpt.jpg";
});

