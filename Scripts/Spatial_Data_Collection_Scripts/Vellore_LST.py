import ee
ee.Initialize(project='active-freehold-465811-h1')

# Load AOI (Vellore boundary shapefile)
aoi = ee.FeatureCollection("projects/active-freehold-465811-h1/assets/Vellore_boundary")

# Sentinel-2 SR Collection
image = (ee.ImageCollection("COPERNICUS/S2_SR")
         .filterBounds(aoi)
         .filterDate('2024-08-01', '2025-08-01')
         .filter(ee.Filter.lt('CLOUDY_PIXEL_PERCENTAGE', 10))
         .median())

# Land Surface Temperature (MODIS)
modis = (ee.ImageCollection("MODIS/061/MOD11A2")
         .filterBounds(aoi)
         .filterDate('2024-08-01','2025-08-01')
         .mean())
lst = modis.select('LST_Day_1km').multiply(0.02).subtract(273.15).rename('LST')
ee.batch.Export.image.toDrive(
    image=lst,
    description='LST_Vellore',
    folder='GEE_exports',
    fileNamePrefix='LST_Vellore_2024_2025',
    scale=1000,
    region=aoi.geometry(),
    maxPixels=1e13
).start()

print("LST export started. Check your Google Drive -> GEE_exports folder.")