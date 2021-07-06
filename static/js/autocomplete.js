let autocomplete;
function initAutocomplete() {
    autocomplete = new google.maps.places.Autocomplete(
        document.getElementById("autocomplete"),
        {
            componentRestrictions: { country: ["UK", "IE"] },
            fields: ["place_id", "name", "geometry"],
        });
    autocomplete.addListener("place_changed", onPlaceChanged);
}

function onPlaceChanged() {
    var location = autocomplete.getPlace();
  
    if (!location.geometry) {
      document.getElementById("autocomplete").placeholder = "Enter location";
    }
  }