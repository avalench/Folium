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
m.save('index.html')
