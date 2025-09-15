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
