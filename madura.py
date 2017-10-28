import folium


m = folium.Map(
    location=[-7.0796837, 113.2876241],
    zoom_start=10,
    )
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
m.save('index.html')
