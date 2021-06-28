//location autocomplate for Uk and Ireland

let autocomplete;
let autocomplete2;
let autocomplete3;
let autocomplete4;
let autocomplete5;
function initAutocomplete() {
    autocomplete = new google.maps.places.Autocomplete(
        document.getElementById("autocomplete"),
        {
            componentRestrictions: { country: ["UK", "IE"] },
            fields: ["place_id", "name", "geometry"],
        }
        );
    autocomplete2 = new google.maps.places.Autocomplete(
        document.getElementById("autocomplete2"),
        {
            componentRestrictions: { country: ["UK", "IE"] },
            fields: ["place_id", "name", "geometry"],
        }
    );
    autocomplete3 = new google.maps.places.Autocomplete(
        document.getElementById("autocomplete3"),
        {
            componentRestrictions: { country: ["UK", "IE"] },
            fields: ["place_id", "name", "geometry"],
        }
    );
    autocomplete4 = new google.maps.places.Autocomplete(
        document.getElementById("autocomplete4"),
        {
            componentRestrictions: { country: ["UK", "IE"] },
            fields: ["place_id", "name", "geometry"],
        }
    );
    autocomplete5 = new google.maps.places.Autocomplete(
        document.getElementById("autocomplete5"),
        {
            componentRestrictions: { country: ["UK", "IE"] },
            fields: ["place_id", "name", "geometry"],
        }
    );
    autocomplete.addListener("place_changed", onPlaceChanged);
    autocomplete2.addListener("place_changed", onPlaceChanged);
    autocomplete3.addListener("place_changed", onPlaceChanged);
    autocomplete4.addListener("place_changed", onPlaceChanged);
    autocomplete5.addListener("place_changed", onPlaceChanged);
}

function onPlaceChanged() {
  var location = autocomplete.getPlace();

  if (!location.geometry) {
    document.getElementById("autocomplete").placeholder = "Enter location";
  }
}