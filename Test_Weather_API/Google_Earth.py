import pySimple
import ee
from google.auth.transport.requests import AuthorizedSession
from google.oauth2 import service_account
PROJECT = 'my-weather-api-378402'
SERVICE_ACCOUNT='bealeja@my-weather-api-378402.iam.gserviceaccount.com'
KEY = "./key.json"
credentials = service_account.Credentials.from_service_account_file(KEY)
scoped_credentials = credentials.with_scopes(
    ['https://www.googleapis.com/auth/cloud-platform'])

session = AuthorizedSession(scoped_credentials)

url = 'https://earthengine.googleapis.com/v1beta/projects/earthengine-public/assets/LANDSAT'

response = session.get(url)

from pprint import pprint
import json
pprint(json.loads(response.content))
ee_creds = ee.ServiceAccountCredentials(SERVICE_ACCOUNT, KEY)
ee.Initialize(ee_creds)

coords = [
  -121.58626826832939,
  38.059141484827485,
]
region = ee.Geometry.Point(coords)

collection = ee.ImageCollection('COPERNICUS/S2')
collection = collection.filterBounds(region)
collection = collection.filterDate('2020-04-01', '2020-09-01')
image = collection.median()


serialized = ee.serializer.encode(image)


# Make a projection to discover the scale in degrees.
proj = ee.Projection('EPSG:4326').atScale(10).getInfo()

# Get scales out of the transform.
scale_x = proj['transform'][0]
scale_y = -proj['transform'][4]

url = 'https://earthengine.googleapis.com/v1beta/projects/{}/image:computePixels'
url = url.format(PROJECT)

response = session.post(
  url=url,
  data=json.dumps({
    'expression': serialized,
    'fileFormat': 'PNG',
    'bandIds': ['B4','B3','B2'],
    'grid': {
      'dimensions': {
        'width': 640,
        'height': 640
      },
      'affineTransform': {
        'scaleX': scale_x,
        'shearX': 0,
        'translateX': coords[0],
        'shearY': 0,
        'scaleY': scale_y,
        'translateY': coords[1]
      },
      'crsCode': 'EPSG:4326',
    },
    'visualizationOptions': {'ranges': [{'min': 0, 'max': 3000}]},
  })
)

image_content = response.content
from IPython.display import Image
Image(image_content)

Landsat8 = ee.Image('LANDSAT/LC08/C01/T1_TOA/LC08_170052_20170108')\
.select('B4', [''])