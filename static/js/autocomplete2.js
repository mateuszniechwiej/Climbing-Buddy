let autocomplete2;
function initAutocomplete() {
    autocomplete2 = new google.maps.places.Autocomplete(
        document.getElementById("autocomplete2"),
        {
            componentRestrictions: { country: ["UK", "IE"] },
            fields: ["place_id", "name", "geometry"],
        });
    autocomplete2.addListener("place_changed", onPlaceChanged);
}

function onPlaceChanged() {
    var location = autocomplete2.getPlace();
  
    if (!location.geometry) {
      document.getElementById("autocomplete2").placeholder = "Enter location";
    }
  }