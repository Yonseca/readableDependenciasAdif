import geopandas as gpd
import requests
import geojson
# from pyproj import CRS
# from owslib.wfs import WebFeatureService

url = "https://ideadif.adif.es/gservices/Tramificacion/wfs?request=GetCapabilities"
params = dict(
    service="WFS",
    version="2.0.0",
    request="GetCapabilities",
    outputFormat="json",
)

r = requests.get(url, params=params)

# Create GeoDataFrame from geojson and set coordinate reference system
data = gpd.GeoDataFrame.from_features(geojson.loads(r.content), crs="EPSG:3067")