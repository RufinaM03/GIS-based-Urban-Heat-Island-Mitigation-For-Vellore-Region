import ee
ee.Initialize(project='active-freehold-465811-h1')

# Load OpenLandMap Soil Sand Fraction dataset
sand_fraction = ee.Image("OpenLandMap/SOL/SOL_SAND-WFRACTION_USDA-3A1A1A_M/v02")

# Select the band (all OpenLandMap datasets usually have one band)
sand_band = sand_fraction.select("b0")

# Load your AOI (replace with your asset)
aoi = ee.FeatureCollection("projects/active-freehold-465811-h1/assets/Vellore_boundary")

# Clip sand data to AOI
sand_clip = sand_band.clip(aoi)

# Export sand fraction raster
task = ee.batch.Export.image.toDrive(
    image=sand_clip,
    description="Vellore_Soil_SandFraction",
    folder="GEE_exports",
    fileNamePrefix="Vellore_Soil_SandFraction",
    scale=250,     # OpenLandMap resolution
    region=aoi.geometry(),
    maxPixels=1e13
)
task.start()

print("Sand fraction export started. Check Google Drive > GEE_exports.")
