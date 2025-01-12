document.addEventListener("DOMContentLoaded", function () {


    const icPg = document.querySelectorAll('.imgPG img');
    const jb = document.getElementById('Jumbroton');
    const images = [
        "url('/static/img/in.jpg')",
        "url('/static/img/en.jpg')",
        "url('/static/img/un.jpg')"
    ];
    indicators = document.querySelectorAll('.ila');
    currentIndex = 0;

    function updateJumbotron(index) {
        if (jb) {
            jb.style.backgroundImage = `linear - gradient(rgba(0, 0, 0, 0.5), rgba(0, 0, 0, 0.5)), ${images[index]}`;
        }

        indicators.forEach((indicator, i) => {
            if (i === index) {
                indicator.classList.add('ila-active');
                indicator.classList.remove('ila');
            } else {
                indicator.classList.remove('ila-active');
                indicator.classList.add('ila');
            }
        });
    }

    updateJumbotron(currentIndex);

    const prevBtn = document.getElementById('prevBtn');
    prevBtn.addEventListener('click', function () {
        currentIndex = (currentIndex === 0) ? images.length - 1 : currentIndex - 1;
        updateJumbotron(currentIndex);
    });

    const nextBtn = document.getElementById('nextBtn');
    nextBtn.addEventListener('click', function () {
        currentIndex = (currentIndex === images.length - 1) ? 0 : currentIndex + 1;
        updateJumbotron(currentIndex);
    });

    icPg.forEach(img => {
        img.addEventListener('click', function () {
            const parentDiv = this.parentElement;
            const bgIg = parentDiv.getAttribute('datajm');
            if (jb && bgIg) {
                jb.style.backgroundImage = `linear-gradient(rgba(0, 0, 0, 0.5), rgba(0, 0, 0, 0.5)), url(${bgIg.replace("url('", "").replace("')", "")})`;
            }
        });
    });

    const dialogBackground = document.getElementById('dialogBackground');
    const openDialogButton = document.getElementById('openDialog');
    const closeDialogButton = document.getElementById('closeDialog');

    openDialogButton.addEventListener('click', function () {
        dialogBackground.style.display = 'flex';
    });

    closeDialogButton.addEventListener('click', function () {
        dialogBackground.style.display = 'none';
    });

    dialogBackground.addEventListener('click', function (e) {
        if (e.target === dialogBackground) {
            dialogBackground.style.display = 'none';
        }
    });
});
var planes = [
    {
        name: "Balai KSDA Aceh",
        lat: 5.528882347086243,
        lng: 95.29385578465542,
        description: "Fokus utama BKSDA Aceh meliputi konservasi satwa liar, seperti gajah, harimau, dan badak Sumatera, perlindungan hutan, penegakan hukum lingkungan, serta pengelolaan kawasan konservasi.",
        image: "/static/gambarBalai/Aceh.png"
    },
    {
        name: "Balai KSDA Sumatra Utara",
        lat: 3.5443164640814775,
        lng: 98.6982041,
        description: "BKSDA ini memiliki peran penting dalam perlindungan habitat, konservasi satwa liar seperti orangutan, gajah, dan harimau Sumatera, serta pengelolaan kawasan konservasi.",
        image: "/static/gambarBalai/Sumatra Utara.png"
    },
    {
        name: "Balai KSDA Alam Riau",
        lat: 0.46352253940349153,
        lng: 101.41554538465542,
        description: "BKSDA Riau berfokus pada perlindungan habitat satwa liar, seperti harimau Sumatera dan gajah Sumatera, yang menjadi ikon konservasi di daerah ini. Selain itu, BKSDA Riau berperan dalam mengelola kawasan konservasi, menangani konflik manusia dan satwa liar, serta menyelamatkan dan merehabilitasi satwa yang terancam punah.",
        image: "/static/gambarBalai/Riau.png"
    },
    {
        name: "Balai KSDA Sumatra Barat",
        lat: -0.9163861746322387,
        lng: 100.36001857910635,
        description: "BKSDA ini berperan dalam perlindungan kawasan konservasi seperti cagar alam, suaka margasatwa, dan taman wisata alam, serta konservasi satwa liar, termasuk harimau Sumatera dan berbagai jenis burung endemik.",
        image: "/static/gambarBalai/Sumatra Barat.png"
    },
    {
        name: "Balai KSDA Bengkulu dan Lampung",
        lat: -3.796567523674085,
        lng: 102.27000216609987,
        description: "BKSDA ini berfokus pada perlindungan habitat penting bagi satwa liar seperti gajah Sumatera dan harimau Sumatera, serta pengelolaan kawasan konservasi seperti cagar alam dan suaka margasatwa.",
        image: "/static/gambarBalai/Bengkulu&Lampung.png"
    },
    {
        name: "Balai KSDA Jambi",
        lat: -1.6105049960239133,
        lng: 103.57737238139795,
        description: "BKSDA Jambi berfokus pada mitigasi konflik manusia dan satwa liar, penyelamatan satwa yang terancam punah, serta rehabilitasi satwa sebelum dikembalikan ke habitat aslinya.",
        image: "/static/gambarBalai/Jambi.png"
    },
    {
        name: "Balai KSDA Sumatera Selatan",
        lat: -2.948137238288411,
        lng: 104.7313534336868,
        description: "BKSDA Sumatera Selatan fokus pada perlindungan dan pengelolaan kawasan konservasi, termasuk suaka margasatwa, cagar alam, dan taman nasional yang menjadi habitat penting bagi satwa liar seperti gajah Sumatera, harimau Sumatera, serta berbagai spesies lainnya.",
        image: "/static/gambarBalai/Sumatera Selatan.png"
    },
    {
        name: "Balai KSDA DKI Jakarta",
        lat: -6.193012161347539,
        lng: 106.84918073666586,
        description: "Meskipun Jakarta bukanlah daerah yang memiliki banyak hutan atau kawasan konservasi alam, BKSDA DKI Jakarta tetap berperan penting dalam perlindungan satwa liar, khususnya yang berada di kawasan urban atau yang terancam punah, seperti burung endemik dan satwa-satwa yang sering ditemukan dalam konflik dengan manusia.",
        image: "/static/gambarBalai/jakarta.png"
    },
    {
        name: "Balai Besar KSDA Jawa Barat",
        lat: -6.9531873933311,
        lng: 107.68658499434686,
        description: "BKSDA Jawa Barat fokus pada perlindungan kawasan konservasi, seperti Taman Nasional Gunung Gede Pangrango, Cagar Alam Ujung Kulon, dan suaka margasatwa, yang menjadi habitat bagi berbagai spesies flora dan fauna, termasuk satwa langka seperti harimau Jawa, jalak bali, serta berbagai jenis burung dan primata.",
        image: "/static/gambarBalai/jawa barat.png"
    },
    {
        name: "Balai KSDA Jawa Tengah",
        lat: -6.999160893002019,
        lng: 110.38729609434742,
        description: "BKSDA Jawa Tengah berfokus pada pengelolaan kawasan konservasi seperti Taman Nasional Gunung Merapi, Taman Nasional Ujung Kulon, dan suaka margasatwa, yang menjadi habitat bagi berbagai satwa liar, termasuk beberapa spesies yang terancam punah seperti harimau Jawa dan berbagai jenis burung endemik.",
        image: "/static/gambarBalai/jawa tengah.png"
    },
    {
        name: "Balai Besar KSDA Jawa Timur",
        lat: -7.38290831284943,
        lng: 112.75748349435219,
        description: "BKSDA Jawa Timur mengelola kawasan konservasi yang meliputi Taman Nasional Bromo Tengger Semeru, Taman Nasional Baluran, dan Suaka Margasatwa Meru Betiri, yang menjadi habitat penting bagi berbagai spesies satwa liar seperti harimau jawa, banteng, macan tutul, dan berbagai jenis burung.",
        image: "/static/gambarBalai/jawa timur.png"
    },
    {
        name: "Balai KSDA DI Yogyakarta",
        lat: -7.703972076251901,
        lng: 110.34830810114421,
        description: "BKSDA Yogyakarta berfokus pada perlindungan dan pengelolaan kawasan konservasi seperti Taman Nasional Gunung Merapi, yang merupakan rumah bagi berbagai spesies flora dan fauna, termasuk satwa langka dan terancam punah seperti burung elang Jawa.",
        image: "/static/gambarBalai/yogyakarta.png"
    },
    {
        name: "Balai KSDA Banten",
        lat: -6.128405711871256,
        lng: 106.15091959259985,
        description: "BKSDA Banten mengelola kawasan konservasi seperti Taman Nasional Ujung Kulon, yang terkenal sebagai habitat utama untuk badak Jawa yang sangat terancam punah, serta berbagai jenis satwa liar lainnya.",
        image: "/static/gambarBalai/banten.png"
    },
    {
        name: "Balai KSDA Bali",
        lat: -8.710426953546436,
        lng: 115.22458507534466,
        description: "BKSDA Bali mengelola kawasan konservasi seperti Taman Nasional Bali Barat, yang menjadi habitat bagi satwa langka seperti banteng, rusa, dan berbagai spesies burung endemik, serta memberikan perlindungan terhadap satwa liar yang terancam punah.",
        image: "/static/gambarBalai/bali.png"
    },
    {
        name: "Balai KSDA Nusa Tenggara Barat",
        lat: -8.5906835708011,
        lng: 116.09482279897405,
        description: "BKSDA NTB mengelola berbagai kawasan konservasi penting seperti Taman Nasional Gunung Rinjani, yang merupakan salah satu destinasi alam utama di Indonesia, serta kawasan konservasi lainnya yang menjadi habitat bagi flora dan fauna khas daerah ini, seperti rusa, monyet ekor panjang, dan berbagai spesies burung.",
        image: "/static/gambarBalai/NTB.png"
    },
    {
        name: "Balai KSDA Nusa Tenggara Timur",
        lat: -10.157496872632466,
        lng: 123.61978870242542,
        description: "BKSDA NTT mengelola kawasan konservasi penting seperti Taman Nasional Komodo, yang terkenal dengan populasi komodo, spesies kadal raksasa yang terancam punah, serta kawasan lainnya yang menjadi habitat bagi berbagai satwa langka dan spesies endemik.",
        image: "/static/gambarBalai/ntt.png"
    },
    {
        name: "Balai KSDA Kalimantan Barat",
        lat: -0.06274547376899858,
        lng: 109.35509628311833,
        description: "BKSDA Kalimantan Barat berfokus pada pengelolaan kawasan konservasi seperti Taman Nasional Danau Sentarum dan Taman Nasional Betung Kerihun, yang menjadi habitat bagi berbagai satwa liar, termasuk orangutan Kalimantan, beruang madu, dan berbagai spesies burung endemik.",
        image: "/static/gambarBalai/kalbar.png"
    },
    {
        name: "Balai KSDA Kalimantan Tengah",
        lat: -2.2094376757677487,
        lng: 113.9145721385571,
        description: "BKSDA Kalimantan Tengah mengelola beberapa kawasan konservasi penting, seperti Taman Nasional Tanjung Puting, yang terkenal dengan populasi orangutan Kalimantan, serta suaka margasatwa dan cagar alam lainnya yang menjadi habitat bagi berbagai spesies satwa langka seperti bekantan, macan dahan, dan berbagai jenis burung.",
        image: "/static/gambarBalai/kalteng.png"
    },
    {
        name: "Balai KSDA Kalimantan Selatan",
        lat: -3.444894370177536,
        lng: 114.85280270334447,
        description: "BKSDA Kalimantan Selatan mengelola kawasan konservasi penting seperti Taman Nasional Bukit Duabelas, serta suaka margasatwa dan cagar alam lainnya yang menjadi habitat bagi beragam satwa liar, termasuk spesies langka seperti orangutan Kalimantan, bekantan, dan harimau sumatera.",
        image: "/static/gambarBalai/kalsel.png"
    },
    {
        name: "Balai KSDA Kalimantan Timur",
        lat: -0.5079280036352027,
        lng: 117.10829573739454,
        description: "BKSDA Kalimantan Timur mengelola beberapa kawasan konservasi penting, seperti Taman Nasional Kutai, yang merupakan habitat bagi satwa langka seperti orangutan Kalimantan, gajah, dan harimau sumatera, serta suaka margasatwa dan cagar alam lainnya.",
        image: "/static/gambarBalai/kaltim.png"
    },
    {
        name: "Balai KSDA Kalimantan Utara",
        lat: 3.323109675060913,
        lng: 117.58242597896977,
        description: "BKSDA Kalimantan Utara mengelola kawasan konservasi yang kaya akan biodiversitas, termasuk hutan tropis dan lahan basah yang menjadi habitat bagi berbagai satwa liar, seperti orangutan Kalimantan, bekantan, serta berbagai spesies burung dan mamalia lainnya.",
        image: "/static/gambarBalai/kalimantanutara.png"
    },
    {
        name: "Balai KSDA Sulawesi Utara",
        lat: 1.4541395985321903,
        lng: 124.8551645943066,
        description: "BKSDA Sulawesi Utara mengelola beberapa kawasan konservasi yang penting, termasuk Taman Nasional Bunaken, yang terkenal dengan kekayaan bawah lautnya, serta kawasan konservasi lainnya yang menjadi habitat bagi berbagai satwa langka seperti tarsius, anoa, dan beragam spesies endemik Sulawesi.",
        image: "/static/gambarBalai/sulut.png"
    },
    {
        name: "Balai KSDA Gorontalo",
        lat: 0.6290808296819494,
        lng: 122.95132006574897,
        description: "lembaga di bawah Kementerian Lingkungan Hidup dan Kehutanan Republik Indonesia yang bertanggung jawab untuk melestarikan sumber daya alam hayati dan ekosistem di wilayah Gorontalo. BKSDA Gorontalo mengelola berbagai kawasan konservasi penting, seperti Suaka Margasatwa Nantu-Boliyohuto, yang merupakan habitat bagi babirusa, anoa, dan berbagai satwa endemik Sulawesi.",
        image: "/static/gambarBalai/gorontalo.png"
    },
    {
        name: "Balai KSDA Sulawesi Tengah",
        lat: -0.9166198242129566,
        lng: 119.89127631453809,
        description: "BKSDA Sulawesi Tengah mengelola beberapa kawasan konservasi penting, seperti Taman Nasional Lore Lindu, yang merupakan habitat bagi berbagai spesies endemik Sulawesi seperti anoa, babirusa, tarsius, dan maleo, serta kawasan konservasi lainnya yang kaya akan keanekaragaman hayati.",
        image: "/static/gambarBalai/sulteng.png"
    },
    {
        name: "Balai KSDA Sulawesi Selatan",
        lat: -5.1412466180793555,
        lng: 119.47549549840402,
        description: "BKSDA Sulawesi Selatan mengelola beberapa kawasan konservasi penting, seperti Suaka Margasatwa Karaenta, yang menjadi habitat bagi satwa khas Sulawesi seperti tarsius, anoa, dan kuskus. Lembaga ini juga melindungi berbagai kawasan hutan konservasi yang memiliki keanekaragaman hayati tinggi.",
        image: "/static/gambarBalai/sulsel.png"
    },
    {
        name: "Balai KSDA Sulawesi Tenggara",
        lat: -3.969663403016351,
        lng: 122.51500882472882,
        description: "BKSDA Sulawesi Tenggara mengelola berbagai kawasan konservasi penting, seperti Suaka Margasatwa Lambusango di Pulau Buton, yang merupakan habitat bagi anoa, babirusa, kuskus, dan berbagai spesies burung endemik Sulawesi.",
        image: "/static/gambarBalai/sulawesi tenggara.png"
    },
    {
        name: "Balai KSDA Maluku",
        lat: -3.6788931035831216,
        lng: 128.19723026454335,
        description: "BKSDA Maluku mengelola berbagai kawasan konservasi penting, seperti Suaka Margasatwa Pulau Seram dan Cagar Alam Manusela, yang menjadi habitat bagi satwa endemik seperti burung kakatua Maluku, nuri seram, dan kuskus beruang.",
        image: "/static/gambarBalai/maluku.png"
    },
    {
        name: "Balai KSDA Maluku Utara",
        lat: 0.8263057593026426,
        lng: 127.38375270030068,
        description: "BKSDA Maluku Utara mengelola berbagai kawasan konservasi penting, seperti Suaka Margasatwa Aketajawe-Lolobata, yang menjadi habitat bagi burung bidadari Halmahera, nuri ternate, kuskus beruang, dan berbagai flora serta fauna endemik lainnya.",
        image: "/static/gambarBalai/maluku utara.png"
    },
    {
        name: "Balai KSDA Papua",
        lat: -2.600383215148931,
        lng: 140.6763957851028,
        description: "BKSDA Papua mengelola berbagai kawasan konservasi penting, seperti Suaka Margasatwa Lorentz dan Cagar Alam Cyclops, yang menjadi habitat bagi keanekaragaman hayati luar biasa, termasuk burung cendrawasih, kasuari, kanguru pohon, dan spesies endemik lainnya.",
        image: "/static/gambarBalai/papua.png"
    },
    {
        name: "Balai KSDA Papua Barat",
        lat: -0.9310465952300399,
        lng: 131.3332838476773,
        description: "BKSDA Papua Barat mengelola berbagai kawasan konservasi penting, seperti Suaka Margasatwa Tambrauw dan kawasan konservasi Raja Ampat, yang terkenal dengan keanekaragaman hayati lautnya serta menjadi habitat bagi spesies endemik daratan seperti burung cendrawasih, kasuari, dan walabi.",
        image: "/static/gambarBalai/papuabarat.png"
    },
];

var map = L.map('map').setView([-3.0060, 115.6155], 4);
mapLink = '<a href="http://openstreetmap.org">OpenStreetMap</a>';
L.tileLayer(
    'http://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
    attribution: '&copy; ' + mapLink + ' Contributors',
    maxZoom: 18,
}).addTo(map);

for (var i = 0; i < planes.length; i++) {
    (function (i) {
        var marker = new L.marker([planes[i].lat, planes[i].lng])
            .bindPopup(
                "<img src='" + planes[i].image + "' class='popup-image'><br>" + // Add image
                "<b>" + planes[i].name + "</b><br>" +
                planes[i].description + "<br>" +
                "<button class='close-btn' onclick='zoomOut()'>Close</button>", // Add close button
                { className: 'custom-popup' }
            )
            .addTo(map);

        marker.on('click', function () {
            // Smooth zoom ke lokasi saat marker diklik
            map.flyTo([planes[i].lat, planes[i].lng], 12, {
                animate: true,  // Menambahkan animasi
                duration: 1.5   // Durasi animasi zoom
            });
            marker.openPopup(); // Buka popup setelah zoom
        });
    })(i);
};

// Function untuk melakukan zoom out kembali dengan animasi smooth
function zoomOut() {
    map.flyTo([-3.0060, 115.6155], 4, {  // Kembali ke zoom level awal dengan animasi
        animate: true,
        duration: 1.5  // Durasi animasi zoom
    });
    map.closePopup(); // Tutup semua popup
};

function toggleDropdown(id) {
    var dropdown = document.getElementById(id);
    var card = dropdown.parentElement;

    // Tutup semua dropdown lainnya
    document.querySelectorAll('.dropdown-content').forEach(function (content) {
        if (content !== dropdown) {
            content.style.display = 'none';
            content.parentElement.classList.remove('active');
        }
    });

    // Toggle untuk dropdown yang diklik
    card.classList.toggle('active');
    dropdown.style.display = card.classList.contains('active') ? 'block' : 'none';

};

