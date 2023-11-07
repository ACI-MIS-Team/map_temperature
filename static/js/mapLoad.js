var baseurl = "http://maps.codemaven.net";
//mapbox load
BANGLA_STYLE = baseurl + "/geocode/banglastyle/";
ENGLISH_STYLE = baseurl + "/geocode/englsihstyle/";
mapboxgl.accessToken =
  "pk.eyJ1IjoidmxhZGltaXJtYWthcm92MTcxIiwiYSI6ImNreTJsdGw0djBhZmwyb24xZ21ianN4Z2wifQ.wNcF-6rCTVkX3oRvBLL4YA";
var map = new mapboxgl.Map({
  container: "map", // container ID
  style: ENGLISH_STYLE, // style URL
  center: [90.3510153, 23.7645784], // starting position [lng, lat]
  zoom: 7, // starting zoom
  attributionControl: false,
});
// Define some sample point coordinates with popup content
var points = [
  {
    type: "Feature",
    properties: {
      title: "Dinajpur",
      description: "Dinajpur Weather Station",
    },
    geometry: {
      type: "Point",
      coordinates: [88.6346, 25.629], // Dinajpur
    },
  },
  {
    type: "Feature",
    properties: {
      title: "Rangpur",
      description: "Rangpur Weather Station",
    },
    geometry: {
      type: "Point",
      coordinates: [89.2752, 25.7439], // Rangpur
    },
  },
  {
    type: "Feature",
    properties: {
      title: "Bogra",
      description: "Bogra Weather Station",
    },
    geometry: {
      type: "Point",
      coordinates: [89.378, 24.8485], // Bogra
    },
  },
  {
    type: "Feature",
    properties: {
      title: "Mymensingh",
      description: "Mymensingh Weather Station",
    },
    geometry: {
      type: "Point",
      coordinates: [90.4075, 24.7465], // Mymensingh
    },
  },
  {
    type: "Feature",
    properties: {
      title: "Sylhet",
      description: "Sylhet Weather Station",
    },
    geometry: {
      type: "Point",
      coordinates: [91.8725, 24.8949], // Sylhet
    },
  },
  {
    type: "Feature",
    properties: {
      title: "Srimongal",
      description: "Srimongal Weather Station",
    },
    geometry: {
      type: "Point",
      coordinates: [91.7296, 24.3144], // Srimongal
    },
  },
  {
    type: "Feature",
    properties: {
      title: "Ishurdi",
      description: "Ishurdi Weather Station",
    },
    geometry: {
      type: "Point",
      coordinates: [89.9845, 24.1495], // Ishurdi
    },
  },
  {
    type: "Feature",
    properties: {
      title: "Dhaka",
      description: "Dhaka Weather Station",
    },
    geometry: {
      type: "Point",
      coordinates: [90.4125, 23.8103], // Dhaka
    },
  },
  {
    type: "Feature",
    properties: {
      title: "Faridpur",
      description: "Faridpur Weather Station",
    },
    geometry: {
      type: "Point",
      coordinates: [89.8394, 23.6061], // Faridpur
    },
  },
  {
    type: "Feature",
    properties: {
      title: "Comilla",
      description: "Comilla Weather Station",
    },
    geometry: {
      type: "Point",
      coordinates: [91.1782, 23.4682], // Comilla
    },
  },
  {
    type: "Feature",
    properties: {
      title: "Jessore",
      description: "Jessore Weather Station",
    },
    geometry: {
      type: "Point",
      coordinates: [89.2107, 23.1695], // Jessore
    },
  },
  {
    type: "Feature",
    properties: {
      title: "Khulna",
      description: "Khulna Weather Station",
    },
    geometry: {
      type: "Point",
      coordinates: [89.5687, 22.8158], // Khulna
    },
  },
  {
    type: "Feature",
    properties: {
      title: "Mymensingh",
      description: "Mymensingh Weather Station",
    },
    geometry: {
      type: "Point",
      coordinates: [90.4075, 24.7465], // Mymensingh
    },
  },
  {
    type: "Feature",
    properties: {
      title: "Rangamati",
      description: "Rangamati Weather Station",
    },
    geometry: {
      type: "Point",
      coordinates: [92.1902, 22.6284], // Rangamati
    },
  },
  {
    type: "Feature",
    properties: {
      title: "Chittagong",
      description: "Chittagong Weather Station",
    },
    geometry: {
      type: "Point",
      coordinates: [91.8, 22.3667], // Chittagong
    },
  },
  {
    type: "Feature",
    properties: {
      title: "Cox's Bazar",
      description: "Cox's Bazar Weather Station",
    },
    geometry: {
      type: "Point",
      coordinates: [92.0058, 21.4272], // Cox's Bazar
    },
  },
];

// Add a source for your points
map.on("load", function () {
  map.addSource("points", {
    type: "geojson",
    data: {
      type: "FeatureCollection",
      features: points,
    },
  });

  map.addLayer({
    id: "points",
    type: "circle",
    source: "points",
    paint: {
      "circle-radius": 10, // Increase the circle size
      "circle-color": "#FF5733", // Customize the color (e.g., orange)
      "circle-opacity": 0.7, // Adjust the opacity
      "circle-stroke-width": 2, // Add a border
      "circle-stroke-color": "#FF5733", // Border color matching the circle color
    },
  });
  // Add a hover popup
  var popup = new mapboxgl.Popup({
    closeButton: false,
    closeOnClick: false,
  });

  map.on("mouseenter", "points", function (e) {
    map.getCanvas().style.cursor = "pointer";
    var coordinates = e.features[0].geometry.coordinates.slice();
    var title = e.features[0].properties.title;
    var description = e.features[0].properties.description;

    popup
      .setLngLat(coordinates)
      .setHTML("<h3>" + title + "</h3><p>" + description + "</p>")
      .addTo(map);
  });

  map.on("mouseleave", "points", function () {
    map.getCanvas().style.cursor = "";
    popup.remove();
  });
});
