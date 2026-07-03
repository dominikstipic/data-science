import geocoder

def process():
    g = geocoder.ip('me')
    latitude  =  g.latlng[0]
    longitude =  g.latlng[1]
    return latitude, longitude

