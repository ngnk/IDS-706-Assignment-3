# Week 3 Mini-Assignment - Testing and Environment Setup

A step-by-step tutorial that walks you through how to setup the docker environment and run the project completed last week.

---

## 1) Overview

This notebook takes the exact same analysis from last week's commodities data project and adds Docker containerization and testing validation. To recap, the script uses data from commodities dating back to 2000, does some basic EDA, analysis, and filtering, before running some basic ML on the price of gold, and finally displays some visualizations.

---

## 2) Dataset description

The notebook expects a single CSV file (found in the repository) named **all_commodities_data.csv**, with the following columns:

- **Date** *(YYYY-MM-DD)* – trading day.
- **Open** – opening price.
- **High** – high price of the day.
- **Low** – low price of the day.
- **Close** – closing price.
- **Volume** – trading volume.
- **Commodity** – commodity name (e.g., "Gold", "Silver").
- **Ticker** – commodity code (e.g., "GC").

---

## 3) Setup Instructions

**Github clone**

Open desktop or whichever folder and cd the pathname in terminal.

Clone this repository by doing the following commands:
```bash
git init
git clone <repository URL>
```

The folder should appear in the directory.

**Verify it has the following files:**

1. **706_A3.ipynb**
2. **README.md**
3. **All_commodities_data.csv**
4. **Dockerfile**
5. **Requirements.txt**
6. **Test_script.py**

## 4) Docker Setup and Environment Creation (Step-by-Step Tutorial)

1. Install Docker Desktop  
   - Download and install Docker Desktop for your OS (Mac, Windows, Linux).  
   - Open Docker Desktop and make sure the daemon is running (look for the whale 🐳 icon in your menu bar/system tray).  

2. Open the repository in VS Code  
   - Open the project folder in VS Code.  
   - Open a terminal inside VS Code (View > Terminal).  

3. Build the Docker image  
   Run this command in the terminal from the repo root (where the Dockerfile is located):

   ```bash
   docker build -t my-analysis .
   ```

5. Run the tests inside the container  
   Once the build is complete, run:

   ```bash 
   docker run --rm my-analysis
   ```
     
   This executes pytest -v inside the container.  

---

## 🧪 Tests Included

The test suite checks that:  
- Data loads properly (no empty DataFrame)  
- Expected columns exist: Date, Open, High, Low, Close, Volume, Ticker, Commodity  
- No null values in price columns (Open, High, Low, Close)  
- "Gold" is present in the commodity column  
- Required packages (pandas, numpy, seaborn, matplotlib, scikit-learn) import successfully  

---

## ✅ Requirements

Dependencies are listed in requirements.txt:  

pandas>=1.3.0  
numpy>=1.21.0  
matplotlib>=3.5.0  
seaborn>=0.11.0  
scikit-learn>=1.0.0  
pytest>=7.0.0  

---

## 🔄 Reusability

To rerun the project in the future:  
1. Start Docker Desktop  
2. Open this repo in VS Code  
3. Build the image again if needed:  
   docker build -t my-analysis .  
4. Run the tests:  
   docker run --rm my-analysis  

The environment is fully reproducible across systems.
