# 🌍 GIS based Urban Heat Island Mitigation System

This project provides an end-to-end intelligent system for predicting and mitigating Urban Heat Island (UHI) impacts using integrated **AI, GIS, and IoT** technologies.

## Project Overview

Urban Heat Island (UHI) is a major urban climate challenge caused by heat-retaining infrastructure and low vegetation.  
This system integrates:

- **GIS datasets** (NDVI, NDWI, NDBI, LST, soil, roads, buildings)
- **IoT sensors** providing real-time temperature & humidity
- **AI (Spatio-Temporal Graph Neural Networks)** for ward-level UHI prediction
- **NLP** for human-readable mitigation recommendations (Pretrained Transformer Model)
- **Interactive dashboards** for visualization and urban planning

The system identifies UHI hotspots and recommends **green infrastructure interventions** such as green roofs, tree corridors, pocket parks, and permeable pavements.

## System Architecture
<img width="882" height="704" alt="image" src="https://github.com/user-attachments/assets/2219ab89-7e84-4e76-9544-9870714e4879" />

## Key Features

### 🔹 1. AI-Based UHI Prediction (ST-GNN)

- Learns **spatial adjacency** between wards
- Captures **temporal climate patterns**
- Predicts LST/UHI with high accuracy:
  - **MAE:** 0.019
  - **RMSE:** 0.01
  - **R²:** 0.79

### 🔹 2. IoT Sensor Integration

Real-time IoT data is used to calibrate and validate AI predictions continuously.


### 🔹 3. Detailed GIS-Based Spatial Analysis

GIS layers used include:

- NDVI, NDWI, NDBI
- Soil Organic Carbon, Sand Fraction
- Land Use / Buildings / Roads
- Monthly climate data (2019–2024)

Data is clipped & aggregated at ward level to form a spatio-temporal dataset.

Vellore District Wardwise Boundary Extraction:

<img width="831" height="529" alt="image" src="https://github.com/user-attachments/assets/da8f31d0-3207-4ffe-b75b-59733989c12d" />

Distribution map of organic carbon content in soils across the wards:

<img width="208" height="199" alt="image" src="https://github.com/user-attachments/assets/cc0c5693-73f3-435f-a773-88290e078607" />

NDVI (Normalized Difference Vegetation Index):

<img width="399" height="393" alt="image" src="https://github.com/user-attachments/assets/aeb48d0d-c4d9-40a4-a5e0-d85a3224c9ff" />

NDWI (Normalized Difference Water Index:

<img width="383" height="369" alt="image" src="https://github.com/user-attachments/assets/ffd17d9e-adb9-477e-93a8-8fb15914f2bd" />

LST (Land Surface Temperature):

<img width="392" height="385" alt="image" src="https://github.com/user-attachments/assets/0ff9b04c-4897-4e6b-9681-3c4fa852a9e0" />

Extracting markers for infrastructure areas from Overpass turbo Database
Map highlighting key infrastructure features extracted for spatial context in the model:

<img width="882" height="413" alt="image" src="https://github.com/user-attachments/assets/9cc8d703-3789-48ce-970f-814e73ab7b28" />

Vector data of each roadway id and their associated tags:

<img width="886" height="553" alt="image" src="https://github.com/user-attachments/assets/c7e01937-5e06-464c-a039-0346e13f5d29" />


### 🔹 4. Smart Mitigation Recommendation Engine

| Land Type           | Recommended Intervention          |
| ------------------- | --------------------------------- |
| Large buildings     | Green roofs, rooftop gardens      |
| Major roads         | Street tree corridors, bioswales  |
| Vacant lots         | Pocket parks, infiltration areas  |
| High built-up zones | Reflective or permeable pavements |

Recommendations are generated using the trained model + GIS spatial context.

### 🔹 5. Dashboard & Visualization

Interactive UI includes:

- Integrated **AI-GIS-IoT framework**
- Ward-level UHI prediction using **ST-GNN**
- Context-aware **green infrastructure recommendation engine**
- Before/After **simulation visualization module**
- Smart City–grade decision support system

<img width="882" height="269" alt="image" src="https://github.com/user-attachments/assets/cb2767d6-a532-4906-9f5e-d2d5299858a3" />
<img width="882" height="459" alt="image" src="https://github.com/user-attachments/assets/260eb772-9609-4118-8655-386ccc0c4f62" />
<img width="882" height="587" alt="image" src="https://github.com/user-attachments/assets/e0b1f3b6-d90b-4a9a-b3fb-ccee0f3ecd76" />
<img width="882" height="318" alt="image" src="https://github.com/user-attachments/assets/1a766a15-6e17-4392-9677-5c333264746a" />
<img width="882" height="448" alt="image" src="https://github.com/user-attachments/assets/dbaabfad-c9ff-4efe-9c80-e70540e33f1b" />
<img width="882" height="358" alt="image" src="https://github.com/user-attachments/assets/1a42d977-83de-42da-a24d-8b1a5d7fae7e" />
<img width="882" height="447" alt="image" src="https://github.com/user-attachments/assets/689a69f6-cd0d-4cd2-8058-4fb0ec0cd9fe" />


## ⚙️ Technology Stack

### Backend / Modeling

- Python
- PyTorch, DGL
- GeoPandas, Rasterio
- MQTT / HTTP for IoT ingestion

### Dashboard

- React / Next.js
- Mapbox / Leaflet for GIS visualization

### AI / NLP

- Spatio-Temporal GNN
- GPT-based text generation


## Workflow

1. Collect GIS + Climate Data
2. Build Spatio-Temporal Dataset
3. Construct Ward Adjacency Graph
4. Train ST-GNN to Predict UHI
5. Ingest IoT Data for Calibration
6. Generate Smart Recommendations
7. Visualize in Dashboard


## Experimental Results

- Integrated multi-source GIS layers correlate strongly with UHI hotspots.
- ST-GNN achieved **R² = 0.8** predicting ward-level UHI.
- Dashboard visualizations show up to **3.4°C reduction** after interventions (sample scenario).


## 📦 Installation

```bash
# Clone repository
git clone https://github.com/RufinaM03/GIS-based-Urban-Heat-Island-Mitigation-For-Vellore-Region.git
cd urban-heat-mitigation-system

# Install backend dependencies
pip install -r requirements.txt

# Train model
python models/train_stgnn.py

# Start dashboard
cd dashboard
npm install
npm start


```
