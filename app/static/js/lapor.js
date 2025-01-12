// Inisialisasi peta dengan Leaflet
var map = L.map('map').setView([-6.200000, 106.816666], 13); // Default: Jakarta

L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
    attribution: '© OpenStreetMap contributors'
}).addTo(map);

var marker;

// Tambahkan event untuk klik pada peta
map.on('click', function (e) {
    var latlng = e.latlng;
    var coords = latlng.lat.toFixed(6) + ',' + latlng.lng.toFixed(6);

    if (marker) {
        marker.setLatLng(latlng);
    } else {
        marker = L.marker(latlng).addTo(map);
    }

    document.getElementById('maps').value = coords;
});

// Fungsi untuk mencari alamat dengan Nominatim (OpenStreetMap API)
function geocodeAddress(address) {
    var url = `https://nominatim.openstreetmap.org/search?format=json&q=${encodeURIComponent(address)}`;

    fetch(url)
        .then(response => response.json())
        .then(data => {
            if (data.length > 0) {
                var lat = parseFloat(data[0].lat);
                var lon = parseFloat(data[0].lon);

                // Set peta dan marker ke lokasi hasil geocoding
                map.setView([lat, lon], 13);

                if (marker) {
                    marker.setLatLng([lat, lon]);
                } else {
                    marker = L.marker([lat, lon]).addTo(map);
                }

                document.getElementById('maps').value = `${lat.toFixed(6)},${lon.toFixed(6)}`;
            } else {
                alert("Lokasi tidak ditemukan, coba lagi dengan alamat yang lebih spesifik.");
            }
        })
        .catch(err => console.error(err));
}

// Event listener untuk input alamat
document.getElementById('alamat').addEventListener('input', function () {
    var address = this.value;

    if (address.length > 3) { // Mulai mencari jika input lebih dari 3 karakter
        geocodeAddress(address);
    }
});