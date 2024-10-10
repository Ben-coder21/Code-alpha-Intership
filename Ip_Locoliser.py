#to locolise the IP Address
import geocoder
g = geocoder.ip('me')
lat, lon = g.latlng
import folium

# Create a map centered at the geolocation
m = folium.Map(location=[lat, lon], zoom_start=13)

# Add a marker at the user's location
folium.Marker([lat, lon], popup="Your Location").add_to(m)

# Save the map as an HTML file
m.save('map.html')
import streamlit as st
import streamlit.components.v1 as components

st.title("Geolocation App")

# Fetch and display user's geolocation
st.write(f"Your location: Latitude {lat}, Longitude {lon}")

# Display the map in Streamlit
with open("map.html", "r") as f:
    html = f.read()
    components.html(html, height=600)
