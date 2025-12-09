# 🌍 GIS based Urban Heat Island Mitigation System

### (GIS + IoT + AI + ST-GNN + NLP)

This project provides an end-to-end intelligent system for predicting and mitigating Urban Heat Island (UHI) impacts using integrated **AI, GIS, and IoT** technologies.

---

## 📘 Project Overview

Urban Heat Island (UHI) is a major urban climate challenge caused by heat-retaining infrastructure and low vegetation.  
This system integrates:

- 🌐 **GIS datasets** (NDVI, NDWI, NDBI, LST, soil, roads, buildings)
- 📡 **IoT sensors** providing real-time temperature & humidity
- 🤖 **AI (Spatio-Temporal Graph Neural Networks)** for ward-level UHI prediction
- 🗣️ **NLP** for human-readable mitigation recommendations
- 📊 **Interactive dashboards** for visualization and urban planning

The system identifies UHI hotspots and recommends **green infrastructure interventions** such as green roofs, tree corridors, pocket parks, and permeable pavements.

---

## ⭐ Key Features

### 🔹 1. AI-Based UHI Prediction (ST-GNN)

- Learns **spatial adjacency** between wards
- Captures **temporal climate patterns**
- Predicts LST/UHI with high accuracy:
  - **MAE:** 0.019
  - **RMSE:** 0.01
  - **R²:** 0.7768

---

### 🔹 2. IoT Sensor Integration

Real-time IoT data is used to calibrate and validate AI predictions continuously.

---

### 🔹 3. Detailed GIS-Based Spatial Analysis

GIS layers used include:

- NDVI, NDWI, NDBI
- Soil Organic Carbon, Sand Fraction
- Land Use / Buildings / Roads
- Monthly climate data (2019–2024)

Data is clipped & aggregated at ward level to form a spatio-temporal dataset.

---

### 🔹 4. Smart Mitigation Recommendation Engine

| Land Type           | Recommended Intervention          |
| ------------------- | --------------------------------- |
| Large buildings     | Green roofs, rooftop gardens      |
| Major roads         | Street tree corridors, bioswales  |
| Vacant lots         | Pocket parks, infiltration areas  |
| High built-up zones | Reflective or permeable pavements |

Recommendations are generated using AI + GIS spatial context.

---

### 🔹 5. Dashboard & Visualization

Interactive UI includes:

- UHI severity & hotspot identification
- Smart recommendations
- Before/After mitigation impact simulation
- Implementation timeline & cost breakdown

---

## 🧠 System Architecture

The architecture integrates:

- Data Acquisition Layer
- GIS Preprocessing Pipeline
- ST-GNN Modeling
- IoT Feedback Calibration
- NLP Recommendation Engine
- Dashboard Visualization Layer

This multi-layer architecture enables **real-time**, adaptive UHI mitigation planning.

---

---

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

---

## 🚀 Workflow

1. Collect GIS + Climate Data
2. Build Spatio-Temporal Dataset
3. Construct Ward Adjacency Graph
4. Train ST-GNN to Predict UHI
5. Ingest IoT Data for Calibration
6. Generate Smart Recommendations
7. Visualize in Dashboard

---

## 🧪 Experimental Results

- Integrated multi-source GIS layers correlate strongly with UHI hotspots.
- ST-GNN achieved **R² = 0.8** predicting ward-level UHI.
- Dashboard visualizations show up to **3.4°C reduction** after interventions (sample scenario).

---

## 🔐 Aspects

- Integrated **AI-GIS-IoT framework**
- Ward-level UHI prediction using **ST-GNN**
- Context-aware **green infrastructure recommendation engine**
- Before/After **simulation visualization module**
- Smart City–grade decision support system

---

## 📦 Installation

```bash
# Clone repository
git clone https://github.com/your-repo.git
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
