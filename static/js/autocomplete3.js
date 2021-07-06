let autocomplete3;
function initAutocomplete() {
    autocomplete3 = new google.maps.places.Autocomplete(
        document.getElementById("autocomplete3"),
        {
            componentRestrictions: { country: ["UK", "IE"] },
            fields: ["place_id", "name", "geometry"],
        });
    autocomplete3.addListener("place_changed", onPlaceChanged);
}

function onPlaceChanged() {
    var location = autocomplete3.getPlace();
  
    if (!location.geometry) {
      document.getElementById("autocomplete3").placeholder = "Enter location";
    }
  }