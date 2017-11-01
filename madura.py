import folium


def normal(lat, long):
    osm = folium.Map(
        location=[lat, long],
        zoom_start=10,
        tiles='OpenStreetMap')
    return osm


def lingkaranMerah(lat, long):
    LM = folium.CircleMarker(
        radius=15,
        location=[lat, long],
        color='crimson',
        fill=True,)
    return LM


def lingkaranBiru(lat, long):
    LB = folium.CircleMarker(
        radius=15,
        location=[lat, long],
        color='blue',
        fill=True,)
    return LB


def lingkaranHijau(lat, long):
    LH = folium.CircleMarker(
        radius=15,
        location=[lat, long],
        color='green',
        fill=True,)
    return LH


m = normal(-7.0796837, 113.2876241)
folium.Marker(
    location=[-7.0095568, 113.8495442],
    popup='Sumenep',
    icon=folium.Icon(icon='info-sign')
).add_to(m)
folium.Marker(
    location=[-7.0461858, 113.5339472],
    popup='Bandungan',
    icon=folium.Icon(icon='info-sign')
).add_to(m)
folium.Marker(
    location=[-7.1227688, 113.3218422],
    popup='Omben',
    icon=folium.Icon(icon='info-sign')
).add_to(m)
folium.Marker(
    location=[-7.1557868, 113.4795329],
    popup='Pamekasan',
    icon=folium.Icon(icon='info-sign')
).add_to(m)
folium.Marker(
    location=[-7.1947317, 113.2480638],
    popup='Sampang',
    icon=folium.Icon(icon='info-sign')
).add_to(m)
folium.Marker(
    location=[-6.9431888, 113.5390432],
    popup='Waru',
    icon=folium.Icon(icon='info-sign')
).add_to(m)
folium.Marker(
    location=[-6.9547548, 112.8408472],
    popup='Aermata',
    icon=folium.Icon(icon='info-sign')
).add_to(m)
folium.Marker(
    location=[-7.0272375, 112.7634372],
    popup='Bangkalan',
    icon=folium.Icon(icon='info-sign')
).add_to(m)
folium.Marker(
    location=[-7.1035618, 113.8482472],
    popup='Saroka',
    icon=folium.Icon(icon='info-sign')
).add_to(m)
folium.Marker(
    location=[-6.9306748, 114.0534472],
    popup='Lombang',
    icon=folium.Icon(icon='info-sign')
).add_to(m)
folium.Marker(
    location=[-7.1636532, 113.5182242],
    popup='Galis',
    icon=folium.Icon(icon='info-sign')
).add_to(m)
folium.Marker(
    location=[-7.0969402, 113.6558853],
    popup='Prenduan',
    icon=folium.Icon(icon='info-sign')
).add_to(m)
folium.Marker(
    location=[-7.0449567, 113.6004068],
    popup='Guluk guluk',
    icon=folium.Icon(icon='info-sign')
).add_to(m)
folium.Marker(
    location=[-7.0995622, 113.7055589],
    popup='Bluto',
    icon=folium.Icon(icon='info-sign')
).add_to(m)
folium.Marker(
    location=[-7.1463927, 113.1281394],
    popup='Torjun',
    icon=folium.Icon(icon='info-sign')
).add_to(m)
folium.Marker(
    location=[-7.1218832, 113.0090748],
    popup='Blega',
    icon=folium.Icon(icon='info-sign')
).add_to(m)
folium.Marker(
    location=[-7.0262722, 113.4541552],
    popup='Batu Ampar',
    icon=folium.Icon(icon='info-sign')
).add_to(m)
folium.Marker(
    location=[-6.9901512, 113.5503519],
    popup='Montorna',
    icon=folium.Icon(icon='info-sign')
).add_to(m)
folium.Marker(
    location=[-6.9803754, 113.000816],
    popup='Kokop',
    icon=folium.Icon(icon='info-sign')
).add_to(m)
folium.Marker(
    location=[-7.0450812, 112.911726],
    popup='Konang',
    icon=folium.Icon(icon='info-sign')
).add_to(m)
folium.Marker(
    location=[-6.963261, 112.7580141],
    popup='Bukit Kapur Arosbaya',
    icon=folium.Icon(icon='info-sign')
).add_to(m)
folium.Marker(
    location=[-7.0034726, 112.7686571],
    popup='Bukit Jaddih',
    icon=folium.Icon(icon='info-sign')
).add_to(m)
folium.Marker(
    location=[-7.0480749, 112.7604445],
    popup='Taman Paseban Kota Bangkalan',
    icon=folium.Icon(icon='info-sign')
).add_to(m)
folium.Marker(
    location=[-7.045562, 112.7608522],
    popup='Kolam Renang Banyu Biru',
    icon=folium.Icon(icon='info-sign')
).add_to(m)
folium.Marker(
    location=[-7.045562, 112.7608522],
    popup='Nasi Bebek Sinjay',
    icon=folium.Icon(icon='info-sign')
).add_to(m)
folium.Marker(
    location=[-7.0392159, 112.7657553],
    popup='SPBU Pertamina PASTI PAS',
    icon=folium.Icon(icon='info-sign')
).add_to(m)
folium.Marker(
    location=[-7.0392159, 112.7657553],
    popup='Bebek Songkem Pak Salim',
    icon=folium.Icon(icon='info-sign')
).add_to(m)
folium.Marker(
    location=[-7.0392159, 112.7657553],
    popup='Khayangan Residence',
    icon=folium.Icon(icon='info-sign')
).add_to(m)
folium.Marker(
    location=[-7.0442843, 112.760541],
    popup='SMK Negeri 2 Bangkalan',
    icon=folium.Icon(icon='info-sign')
).add_to(m)
folium.Marker(
    location=[-7.0454249, 112.7566373],
    popup='Rumah Makan Mbah Muslimah',
    icon=folium.Icon(icon='info-sign')
).add_to(m)
folium.Marker(
    location=[-7.158283, 113.476421],
    popup='zoya pamekasan',
    icon=folium.Icon(icon='info-sign')
).add_to(m)
folium.Marker(
    location=[-7.158302, 113.476522],
    popup='masjid',
    icon=folium.Icon(icon='info-sign')
).add_to(m)
folium.Marker(
    location=[-7.158529, 113.476702],
    popup='atm bni',
    icon=folium.Icon(icon='info-sign')
).add_to(m)
folium.Marker(
    location=[-7.159141, 113.477762],
    popup='segara',
    icon=folium.Icon(icon='info-sign')
).add_to(m)
folium.Marker(
    location=[-7.160491, 113.481492],
    popup='masjid agung',
    icon=folium.Icon(icon='info-sign')
).add_to(m)
folium.Marker(
    location=[-7.155767, 113.483456],
    popup='mandilaras',
    icon=folium.Icon(icon='info-sign')
).add_to(m)
folium.Marker(
    location=[-7.157763, 113.487638],
    popup='jl. Stadion',
    icon=folium.Icon(icon='info-sign')
).add_to(m)
folium.Marker(
    location=[-7.160425, 113.486815],
    popup='telemoyo',
    icon=folium.Icon(icon='info-sign')
).add_to(m)
folium.Marker(
    location=[-7.160897, 113.485739],
    popup='jokotole',
    icon=folium.Icon(icon='info-sign')
).add_to(m)
folium.Marker(
    location=[-7.162484, 113.486246],
    popup='jingga',
    icon=folium.Icon(icon='info-sign')
).add_to(m)
folium.Marker(
    location=[-7.1727889, 113.4447051],
    popup='Edu Wisata Selamat Pagi Madura',
    icon=folium.Icon(icon='info-sign')
).add_to(m)
folium.Marker(
    location=[-7.0583209, 113.3288337],
    popup='KAR Cell Batuampar',
    icon=folium.Icon(icon='info-sign')
).add_to(m)
folium.Marker(
    location=[-7.203956, 113.4722567],
    popup='Gelora Ratu Pamellingan Stadium',
    icon=folium.Icon(icon='info-sign')
).add_to(m)
folium.Marker(
    location=[-7.203956, 113.4722567],
    popup='Terminal Ronggosukowati',
    icon=folium.Icon(icon='info-sign')
).add_to(m)
folium.Marker(
    location=[-7.183527, 113.4785846],
    popup='RSUD Dr.H. Slamet Martodirdjo',
    icon=folium.Icon(icon='info-sign')
).add_to(m)
folium.Marker(
    location=[-7.1700081, 113.4792069],
    popup='SMPN 1 Pamekasan',
    icon=folium.Icon(icon='info-sign')
).add_to(m)
folium.Marker(
    location=[-7.1673895, 113.4784559],
    popup='Pasar Sekar Putih Gurem',
    icon=folium.Icon(icon='info-sign')
).add_to(m)
folium.Marker(
    location=[-7.1592353, 113.4928325],
    popup='UPT Rumah Sakit Umum Mohammad Noer',
    icon=folium.Icon(icon='info-sign')
).add_to(m)
folium.Marker(
    location=[-7.1540617, 113.4959224],
    popup='Lapas Narkotika Kelas IIA Pamekasan',
    icon=folium.Icon(icon='info-sign')
).add_to(m)
folium.Marker(
    location=[-7.160236, 113.4842923],
    popup='Alun Alun Pamekasan',
    icon=folium.Icon(icon='info-sign')
).add_to(m)
folium.Marker(
    location=[-7.2371563, 113.5335884],
    popup='Pantai Jumiang',
    icon=folium.Icon(icon='info-sign')
).add_to(m)
folium.Marker(
    location=[-7.233311, 113.5493051],
    popup='Cafe Rampak Naong Jumiang',
    icon=folium.Icon(icon='info-sign')
).add_to(m)
folium.Marker(
    location=[-7.2337446, 113.5442443],
    popup='PT. Marinal Indoprima',
    icon=folium.Icon(icon='info-sign')
).add_to(m)
folium.Marker(
    location=[-7.2337446, 113.5442443],
    popup='Sunrise Point Cafe',
    icon=folium.Icon(icon='info-sign')
).add_to(m)
folium.Marker(
    location=[-7.2331388, 113.5264192],
    popup='Masjid Nurul Huda',
    icon=folium.Icon(icon='info-sign')
).add_to(m)
folium.Marker(
    location=[-7.2331388, 113.5264192],
    popup='Mushalla Nurud Dholam',
    icon=folium.Icon(icon='info-sign')
).add_to(m)
folium.Marker(
    location=[-7.2328382, 113.5281948],
    popup='TPQ Nurul Dholam',
    icon=folium.Icon(icon='info-sign')
).add_to(m)
folium.Marker(
    location=[-7.2321956, 113.5281704],
    popup='Majelis Taklim Al Hidayah',
    icon=folium.Icon(icon='info-sign')
).add_to(m)
folium.Marker(
    location=[-7.2362887, 113.5305008],
    popup='Teri Crispy - Sofyan Store',
    icon=folium.Icon(icon='info-sign')
).add_to(m)
folium.Marker(
    location=[-7.2374975, 113.5292921],
    popup='Pantai Padelegan',
    icon=folium.Icon(icon='info-sign')
).add_to(m)
folium.Marker(
    location=[-6.9011039, 112.9471094],
    popup='Pijet Setrum',
    icon=folium.Icon(color='red', icon='info-sign')
).add_to(m)
folium.Marker(
    location=[-6.8862571, 112.9828318, 17.54],
    popup='Taman mangrove 2',
    icon=folium.Icon(color='green', icon='info-sign')
).add_to(m)
folium.Marker(
    location=[-6.8882991, 112.9883212, 16.54],
    popup='Taman mangrove ',
    icon=folium.Icon(color='green', icon='info-sign')
).add_to(m)
folium.Marker(
    location=[-6.8906211, 113.0694814, 18.04],
    popup='Kantor Pos ',
    icon=folium.Icon(color='orange', icon='info-sign')
).add_to(m)
folium.Marker(
    location=[-6.9860248, 113.0267308, 16],
    popup='Night club Tramok kokop ',
    icon=folium.Icon(color='black', icon='info-sign')
).add_to(m)
folium.Marker(
    location=[-6.9962151, 113.0540483, 16],
    popup='Kantor Pos kokop ',
    icon=folium.Icon(color='orange', icon='info-sign')
).add_to(m)
folium.Marker(
    location=[-7.0103881, 112.9881211, 17],
    popup='Night club Aeng ',
    icon=folium.Icon(color='black', icon='info-sign')
).add_to(m)
folium.Marker(
    location=[-7.0936784, 112.7065992, 17.42],
    popup='Kantor Pos ',
    icon=folium.Icon(color='orange', icon='info-sign')
).add_to(m)
folium.Marker(
    location=[-6.9531759, 114.1001642, 15.25],
    popup='Lahan sorgum ',
    icon=folium.Icon(color='green', icon='info-sign')
).add_to(m)
folium.Marker(
    location=[-6.8701869, 113.9246468, 18.79],
    popup='Batu putih ',
    icon=folium.Icon(color='white', icon='info-sign')
).add_to(m)
folium.Marker(
    location=[-6.9762634, 114.1182389],
    popup='Wisata Pantai Lapa Laok',
    icon=folium.Icon(icon='info-sign')
).add_to(m)
folium.Marker(
    location=[-6.975132, 114.107352],
    popup='Masjid Ar Rafiqur Rahman',
    icon=folium.Icon(icon='info-sign')
).add_to(m)
folium.Marker(
    location=[-6.9728743, 114],
    popup='Pantai Dungkek',
    icon=folium.Icon(icon='info-sign')
).add_to(m)
folium.Marker(
    location=[-6.9618709, 114.0981994],
    popup='Masjid Nurul Islam',
    icon=folium.Icon(icon='info-sign')
).add_to(m)
folium.Marker(
    location=[-6.9698403, 114.0996264],
    popup='Masjid As Sholihin',
    icon=folium.Icon(icon='info-sign')
).add_to(m)
folium.Marker(
    location=[-6.9764643, 114.0947555],
    popup='Pelabuhan Dungkek',
    icon=folium.Icon(icon='info-sign')
).add_to(m)
folium.Marker(
    location=[-6.9764643, 114.0947555],
    popup='Kantor Pos Dungkek',
    icon=folium.Icon(icon='info-sign')
).add_to(m)
folium.Marker(
    location=[-6.9764643, 114.0947555],
    popup='KUA Dungkek Sumenep',
    icon=folium.Icon(icon='info-sign')
).add_to(m)
folium.Marker(
    location=[-6.9764643, 114.0947555],
    popup='Pasar Dungkek',
    icon=folium.Icon(icon='info-sign')
).add_to(m)
folium.Marker(
    location=[-6.9716201, 114.0948479],
    popup='Bukit Wisata Kalompek',
    icon=folium.Icon(icon='info-sign')
).add_to(m)
folium.Marker(
    location=[-6.9250794, 112.8989777],
    popup='Mangrove Labuhan',
    icon=folium.Icon(icon='info-sign')
).add_to(m)
folium.Marker(
    location=[-6.940416, 112.8620705],
    popup='Bukit Kapur Arosbaya',
    icon=folium.Icon(icon='info-sign')
).add_to(m)
folium.Marker(
    location=[-6.8943622, 112.993606],
    popup='Pertamina',
    icon=folium.Icon(icon='info-sign')
).add_to(m)
folium.Marker(
    location=[-6.8876956, 113.0196007],
    popup='Masjid Waleed Aqeeli Al Hasan',
    icon=folium.Icon(icon='info-sign')
).add_to(m)
folium.Marker(
    location=[-6.8863109, 113.022991],
    popup='SPBN AKR Banyu Sangka',
    icon=folium.Icon(icon='info-sign')
).add_to(m)
folium.Marker(
    location=[-6.8979208, 112.9564936],
    popup='Pt. Semen Gresik',
    icon=folium.Icon(icon='info-sign')
).add_to(m)
folium.Marker(
    location=[-6.8946402, 112.9285343],
    popup='Kantor Desa Larangan Glintong',
    icon=folium.Icon(icon='info-sign')
).add_to(m)
folium.Marker(
    location=[-6.8951518, 112.9041227],
    popup='Indomaret Klampis',
    icon=folium.Icon(icon='info-sign')
).add_to(m)
folium.Marker(
    location=[-6.8965365, 112.8832229],
    popup='Indomarco Adi Prima PT',
    icon=folium.Icon(icon='info-sign')
).add_to(m)
folium.Marker(
    location=[-6.9002431, 112.8742536],
    popup='Mrandung Village',
    icon=folium.Icon(icon='info-sign')
).add_to(m)
folium.Marker(
    location=[-6.893240, 113.284143],
    popup='Pasar Lebak',
    icon=folium.Icon(icon='info-sign')
).add_to(m)
folium.Marker(
    location=[-6.893371, 113.284916],
    popup='Spbu',
    icon=folium.Icon(icon='info-sign')
).add_to(m)
folium.Marker(
    location=[-6.892918, 113.286273],
    popup='Bakso Pak Sapri',
    icon=folium.Icon(icon='info-sign')
).add_to(m)
folium.Marker(
    location=[-6.918344, 113.164994],
    popup='Banjoeates',
    icon=folium.Icon(icon='info-sign')
).add_to(m)
folium.Marker(
    location=[-6.887144, 112.992846],
    popup='Mangrove Labuhan',
    icon=folium.Icon(icon='info-sign')
).add_to(m)
folium.Marker(
    location=[-6.912516, 113.035216],
    popup='Tagungguh',
    icon=folium.Icon(icon='info-sign')
).add_to(m)
folium.Marker(
    location=[-7.158380, 113.478389],
    popup='Gladak Anyar',
    icon=folium.Icon(icon='info-sign')
).add_to(m)
folium.Marker(
    location=[-7.221390, 113.531947],
    popup='Tanjung',
    icon=folium.Icon(icon='info-sign')
).add_to(m)
folium.Marker(
    location=[-7.169427, 113.430080],
    popup='Proppo',
    icon=folium.Icon(icon='info-sign')
).add_to(m)
folium.Marker(
    location=[-7.186633, 113.371867],
    popup='Rabasan',
    icon=folium.Icon(icon='info-sign')
).add_to(m)
folium.Marker(
    location=[-7.209429, 113.0336413, 16.79],
    popup='Kantor Pos Modung ',
    icon=folium.Icon(color='orange', icon='info-sign')
).add_to(m)
folium.Marker(
    location=[-7.2166668, 113.0579122, 15],
    popup='Laboean',
    icon=folium.Icon(icon='info-sign')
).add_to(m)
folium.Marker(
    location=[-6.8928552, 113.2576821, 12],
    popup='Air Terjun Toroan ',
    icon=folium.Icon(color='green', icon='info-sign')
).add_to(m)
folium.Marker(
    location=[-6.9086727, 113.4831474, 16.5],
    popup='Goa Blaban ',
    icon=folium.Icon(color='brown', icon='info-sign')
).add_to(m)
folium.Marker(
    location=[-6.8985224, 113.4843233, 17.5],
    popup='Kantor Pos Batumarmar ',
    icon=folium.Icon(color='orange', icon='info-sign')
).add_to(m)
folium.Marker(
    location=[-6.8986128, 113.4893759, 17.5],
    popup='Night Club Sp ',
    icon=folium.Icon(color='black', icon='info-sign')
).add_to(m)
folium.Marker(
    location=[-6.8969276, 113.4797962, 18.5],
    popup='Shisa Cafe Colozeum ',
    icon=folium.Icon(color='black', icon='info-sign')
).add_to(m)
folium.Marker(
    location=[-6.8957723, 113.4705835, 18],
    popup='Kantor Pos Sokobanah ',
    icon=folium.Icon(color='orange', icon='info-sign')
).add_to(m)
folium.Marker(
    location=[-6.8999998, 113.4079122, 15],
    popup='Sokobanah',
    icon=folium.Icon(icon='info-sign')
).add_to(m)
folium.Marker(
    location=[-6.9102138, 113.3161432, 15],
    popup='Kelapang',
    icon=folium.Icon(icon='info-sign')
).add_to(m)
folium.Marker(
    location=[-7.1041556, 113.8785575],
    popup='Tk. Katulistiwa',
    icon=folium.Icon(icon='info-sign')
).add_to(m)
folium.Marker(
    location=[-7.1171866, 113.8809178],
    popup='Warkop Bunda Rio',
    icon=folium.Icon(icon='info-sign')
).add_to(m)
folium.Marker(
    location=[-7.1253202, 113.8889859],
    popup='Pelabuhan Tanjung, Saronggi',
    icon=folium.Icon(icon='info-sign')
).add_to(m)
folium.Marker(
    location=[-7.1296638, 113.8890932],
    popup='Menara Suar Tanjung',
    icon=folium.Icon(icon='info-sign')
).add_to(m)
folium.Marker(
    location=[-7.1225877, 113.8925464],
    popup='Masjid Taufiqur Rahman',
    icon=folium.Icon(icon='info-sign')
).add_to(m)
folium.Marker(
    location=[-7.1241098, 113.890489],
    popup='Loket Transportasi Wisata Gili Labak',
    icon=folium.Icon(icon='info-sign')
).add_to(m)
folium.Marker(
    location=[-7.1241098, 113.890489],
    popup='SPBN AKR Saronggi Sumenep',
    icon=folium.Icon(icon='info-sign')
).add_to(m)
folium.Marker(
    location=[-7.1066376, 113.8661854],
    popup='SMPN 2 Sarongi',
    icon=folium.Icon(icon='info-sign')
).add_to(m)
folium.Marker(
    location=[-7.097404, 113.8597051],
    popup='Warung Kopi Bu Serli',
    icon=folium.Icon(icon='info-sign')
).add_to(m)
folium.Marker(
    location=[-7.0973614, 113.8597051],
    popup='Toko Hj. Jamila',
    icon=folium.Icon(icon='info-sign')
).add_to(m)
folium.Marker(
    location=[-7.2138232, 113.299243],
    popup='Pantai Wisata Camplong ,hotel, Dan Resto',
    icon=folium.Icon(icon='info-sign')
).add_to(m)
folium.Marker(
    location=[-7.2136529, 113.2729359],
    popup='Politeknik Negeri Madura',
    icon=folium.Icon(icon='info-sign')
).add_to(m)
folium.Marker(
    location=[-7.2006671, 113.2419725],
    popup='RSUD Sampang',
    icon=folium.Icon(icon='info-sign')
).add_to(m)
folium.Marker(
    location=[-7.196303, 113.2430883],
    popup='Pantai Nepa Sampang Madura',
    icon=folium.Icon(icon='info-sign')
).add_to(m)
folium.Marker(
    location=[-7.1939825, 113.2397838],
    popup='Kodim 0828 Sampang',
    icon=folium.Icon(icon='info-sign')
).add_to(m)
folium.Marker(
    location=[-7.2199006, 113.2050832],
    popup='PT Garam Persero',
    icon=folium.Icon(icon='info-sign')
).add_to(m)
folium.Marker(
    location=[-6.9887753, 112.7826459],
    popup='Agenpos Jaya Bersaudara',
    icon=folium.Icon(icon='info-sign')
).add_to(m)
folium.Marker(
    location=[-6.998402, 112.7753717],
    popup='TOKO LAUT BIRU',
    icon=folium.Icon(icon='info-sign')
).add_to(m)
folium.Marker(
    location=[-7.0052811, 112.7689988],
    popup='UKM Seni Nanggala Universitas Trunojoyo',
    icon=folium.Icon(icon='info-sign')
).add_to(m)
folium.Marker(
    location=[-7.0117342, 112.7628834],
    popup='Perum Citra Mutiara Bancaran',
    icon=folium.Icon(icon='info-sign')
).add_to(m)
folium.Marker(
    location=[-7.054003, 113.942728],
    popup='Biru laut express ',
    icon=folium.Icon(color='blue', icon='info-sign')
).add_to(m)
folium.Marker(
    location=[-7.056952, 113.942707],
    popup='Pelabuhan Kali Anget ',
    icon=folium.Icon(color='blue', icon='info-sign')
).add_to(m)
folium.Marker(
    location=[-7.052214, 113.947878],
    popup='Goa Batu Kurung ',
    icon=folium.Icon(color='yellow', icon='info-sign')
).add_to(m)
folium.Marker(
    location=[-7.044729, 113.947577],
    popup='Pelabuhan kaletek ',
    icon=folium.Icon(color='blue', icon='info-sign')
).add_to(m)
folium.Marker(
    location=[-7.024242, 113.890200],
    popup='Bandara Trunojoyo ',
    icon=folium.Icon(color='blue', icon='info-sign')
).add_to(m)
folium.Marker(
    location=[-7.007172, 113.856007],
    popup='Taman Kemala ',
    icon=folium.Icon(color='green', icon='info-sign')
).add_to(m)
folium.Marker(
    location=[-7.008237, 113.860245],
    popup='Taman Adipura kota Sumenep ',
    icon=folium.Icon(color='green', icon='info-sign')
).add_to(m)
folium.Marker(
    location=[-7.008493, 113.864161],
    popup='Taman Lake ',
    icon=folium.Icon(color='green', icon='info-sign')
).add_to(m)
folium.Marker(
    location=[-7.003296, 113.863710],
    popup='Kantor Pos Sumenep ',
    icon=folium.Icon(color='orange', icon='info-sign')
).add_to(m)
folium.Marker(
    location=[-6.995767, 113.871928],
    popup='Makam pangeran ketandur ',
    icon=folium.Icon(color='black', icon='info-sign')
).add_to(m)
folium.Marker(
    location=[-6.994261, 113.017124],
    popup='Kokop',
    icon=folium.Icon(color='black', icon='info-sign')
).add_to(m)
folium.Marker(
    location=[-7.142466, 113.060383],
    popup='Rosep',
    icon=folium.Icon(color='black', icon='info-sign')
).add_to(m)
folium.Marker(
    location=[-6.973122, 112.831043],
    popup='Balung',
    icon=folium.Icon(color='black', icon='info-sign')
).add_to(m)
folium.Marker(
    location=[-7.055579, 112.706631],
    popup='Socah',
    icon=folium.Icon(color='black', icon='info-sign')
).add_to(m)
folium.Marker(
    location=[-7.061707, 112.856320],
    popup='Tanah Merah',
    icon=folium.Icon(color='black', icon='info-sign')
).add_to(m)
folium.Marker(
    location=[-7.187750, 113.129605],
    popup='Disanah',
    icon=folium.Icon(color='black', icon='info-sign')
).add_to(m)
folium.Marker(
    location=[-7.152535, 113.222454],
    popup='Patapan',
    icon=folium.Icon(color='black', icon='info-sign')
).add_to(m)
folium.Marker(
    location=[-7.099726, 113.530758],
    popup='Bangkes',
    icon=folium.Icon(color='black', icon='info-sign')
).add_to(m)
folium.Marker(
    location=[-7.090863, 113.989995],
    popup='Talango',
    icon=folium.Icon(color='black', icon='info-sign')
).add_to(m)
folium.Marker(
    location=[-6.947061, 113.810094],
    popup='Dasuk',
    icon=folium.Icon(color='black', icon='info-sign')
).add_to(m)
folium.Marker(
    location=[-6.993473, 113.5148273],
    popup='Gunung Perkat(Jurkottok)',
    icon=folium.Icon(icon='info-sign')
).add_to(m)
folium.Marker(
    location=[-7.0080824, 113.5372675],
    popup='Kamboja. UD',
    icon=folium.Icon(icon='info-sign')
).add_to(m)
folium.Marker(
    location=[-7.0163539, 113.5537017],
    popup='Bank Rakyat Indonesia',
    icon=folium.Icon(icon='info-sign')
).add_to(m)
folium.Marker(
    location=[-7.021983, 113.55616],
    popup='Taman Pendidikan Al-Quran (TPQ) Al-Amannah',
    icon=folium.Icon(icon='info-sign')
).add_to(m)
folium.Marker(
    location=[-7.0261055, 113.5511061],
    popup='Koperasi Unit Desa Karya Bhakti',
    icon=folium.Icon(icon='info-sign')
).add_to(m)
folium.Marker(
    location=[-7.0311546, 113.5471132],
    popup='SPBU Pakong',
    icon=folium.Icon(icon='info-sign')
).add_to(m)
folium.Marker(
    location=[-7.0366458, 113.5460843],
    popup='Spbu Pertamina',
    icon=folium.Icon(icon='info-sign')
).add_to(m)
folium.Marker(
    location=[-7.0443005, 113.5455239],
    popup='KAMPOENG CANDI',
    icon=folium.Icon(icon='info-sign')
).add_to(m)
folium.Marker(
    location=[-7.0080824, 113.5372675],
    popup='Kopontren Pancoran',
    icon=folium.Icon(icon='info-sign')
).add_to(m)
folium.Marker(
    location=[-7.0952578, 113.5546416],
    popup='Mabrur. UD',
    icon=folium.Icon(icon='info-sign')
).add_to(m)
folium.Marker(
    location=[-6.913833, 113.920749],
    popup='Batuputih',
    icon=folium.Icon(color='black', icon='info-sign')
).add_to(m)
folium.Marker(
    location=[-7.027314, 113.438724],
    popup='Pasanggar',
    icon=folium.Icon(color='black', icon='info-sign')
).add_to(m)
folium.Marker(
    location=[-6.999600, 113.408902],
    popup='Poreh',
    icon=folium.Icon(color='black', icon='info-sign')
).add_to(m)
folium.Marker(
    location=[-6.943450, 113.400147],
    popup='Bira Timur',
    icon=folium.Icon(color='black', icon='info-sign')
).add_to(m)
folium.Marker(
    location=[-6.962700, 113.344529],
    popup='Pancor',
    icon=folium.Icon(color='black', icon='info-sign')
).add_to(m)
folium.Marker(
    location=[-7.058447, 113.139909],
    popup='Beringin',
    icon=folium.Icon(color='black', icon='info-sign')
).add_to(m)
folium.Marker(
    location=[-7.007671, 113.020433],
    popup='Lembung Gunong',
    icon=folium.Icon(color='black', icon='info-sign')
).add_to(m)
folium.Marker(
    location=[-7.148377, 113.010133],
    popup='Gigir',
    icon=folium.Icon(color='black', icon='info-sign')
).add_to(m)
folium.Marker(
    location=[-6.961838, 113.695802],
    popup='Rajun',
    icon=folium.Icon(color='black', icon='info-sign')
).add_to(m)
folium.Marker(
    location=[-7.059289, 113.710908],
    popup='Ganding',
    icon=folium.Icon(color='black', icon='info-sign')
).add_to(m)
lingkaranMerah(-7.163869, 112.781680).add_to(m)
lingkaranBiru(-7.174050, 112.727494).add_to(m)
lingkaranBiru(-7.175157, 112.721754).add_to(m)
lingkaranBiru(-7.044729, 113.947577).add_to(m)
lingkaranBiru(-6.9764643, 114.0947555).add_to(m)
lingkaranBiru(-7.1253202, 113.8889859).add_to(m)
lingkaranBiru(-7.056952, 113.942707).add_to(m)
lingkaranHijau(-7.0480749, 112.7604445).add_to(m)
lingkaranHijau(-6.8862571, 112.9828318).add_to(m)
lingkaranHijau(-6.8882991, 112.9883212).add_to(m)


m.save('index.html')
