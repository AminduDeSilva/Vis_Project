# Sri Lanka's Journey: A Comparative Study with Germany


An interactive data visualization application that tells the story of Sri Lanka's socio-economic journey over the past 25 years, comparing it with Germany to provide insights into their respective economic and social landscapes.

## 🌟 Project Overview

This project explores Sri Lanka's resilience through various challenges including natural disasters, civil conflicts, terrorist attacks, and the COVID-19 pandemic. Through interactive visualizations, we compare key indicators between Sri Lanka and Germany, including:

- **Economic Indicators**: GDP, Inflation rates
- **Social Metrics**: Happiness index, Quality of life
- **Tourism Impact**: Visitor arrivals and industry growth
- **Historical Events**: Impact of major incidents on national development

## 🚀 Live Demo

Visit the live application: [Sri Lanka's Journey](visproject-c5hjgjg9wm6t3oleevh7fy.streamlit.app/)

## 📊 Features

- **Interactive Visualizations**: Built with Plotly for dynamic data exploration
- **Comparative Analysis**: Side-by-side comparison between Sri Lanka and Germany
- **Historical Context**: Timeline of major events and their impact
- **Multiple Data Sources**: Comprehensive datasets covering 25+ years
- **Responsive Design**: Works on desktop and mobile devices

## 🛠️ Installation & Setup

### Prerequisites

- Python 3.12.x
- Docker (optional, recommended)

### Option 1: Using Docker (Recommended)

```bash
# Clone the repository
git clone https://github.com/yourusername/Vis_Project.git
cd Vis_Project/srilanka

# Build and run with Docker
docker build -t srilanka-vis .
docker run -p 8501:8501 srilanka-vis
```

Open http://localhost:8501 in your browser.

### Option 2: Local Installation

```bash
# Clone the repository
git clone https://github.com/yourusername/Vis_Project.git
cd Vis_Project

# Create conda environment
conda env create -f environment.yml
conda activate vis24

# Navigate to the app directory
cd srilanka

# Install requirements
pip install -r requirements.txt

# Run the application
streamlit run "Code/Sri Lanka's Journey.py"
```

## 📁 Project Structure

```
Vis_Project/
├── README.md
├── environment.yml                 # Conda environment configuration
├── hello-rosenheim.ipynb          # Development setup notebook
├── srilanka/                       # Main application directory
│   ├── Code/
│   │   ├── Sri Lanka's Journey.py  # Main Streamlit application
│   │   ├── data_utils.py          # Data processing utilities
│   │   ├── plot_utils.py          # Visualization utilities
│   │   ├── definitions.py         # UI components and constants
│   │   └── pages/                 # Additional Streamlit pages
│   │       └── Incidents.py       # Historical incidents analysis
│   ├── data/                      # All datasets
│   │   ├── tourism/               # Tourism arrival data
│   │   ├── inflation/             # Inflation rate data
│   │   ├── gdp/                   # GDP data
│   │   ├── happiness/             # Happiness index data
│   │   ├── pictures/              # Images used in the app
│   │   └── plot_descriptions.json # Chart descriptions
│   ├── plots/                     # Generated visualizations
│   ├── Dockerfile                 # Docker configuration
│   ├── requirements.txt           # Python dependencies
│   └── .streamlit/
│       └── config.toml            # Streamlit configuration
```

## 📈 Data Sources

The project uses multiple datasets spanning 25+ years:

- **Tourism Data**: Visitor arrivals for both Sri Lanka and Germany
- **Economic Data**: GDP growth rates and inflation indicators
- **Social Data**: World Happiness Report indices
- **Historical Events**: Major incidents and their timeline

All data sources are documented in the respective data subdirectories.

## 🎨 Technologies Used

- **Frontend**: Streamlit
- **Data Visualization**: Plotly, Matplotlib, Seaborn
- **Data Processing**: Pandas, NumPy
- **Deployment**: Docker, Streamlit Cloud
- **Development**: Jupyter Notebooks

## 📋 Dependencies

```
streamlit>=1.36.0
plotly>=5.22.0
pandas>=2.2.0
numpy>=2.0.0
matplotlib>=3.9.0
seaborn>=0.13.0
```

See [`requirements.txt`](srilanka/requirements.txt) for complete list.

## 🤝 Contributing

This project was developed as part of the "Storytelling with Interactive Data Visualizations" course at TH Rosenheim.

### Development Workflow

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📖 Usage

1. **Main Dashboard**: Overview of Sri Lanka's journey with key metrics
![Screenshot 2025-06-29 at 21 24 59 (2)](https://github.com/user-attachments/assets/46ef61a4-1fd1-454a-baa0-ace63bc1f2d6)                      


2. **Comparative Analysis**: Side-by-side comparison with Germany
![Screenshot 2025-06-29 at 21 24 40 (2)](https://github.com/user-attachments/assets/a63aaf53-ef86-44e4-a2ee-5d90cfd24487)

4. **Historical Timeline**: Major events and their impact
![Screenshot 2025-06-29 at 21 24 10 (2)](https://github.com/user-attachments/assets/bcecbc91-2670-4b09-8921-1c982454f63a)
5. **Detailed Incidents**: In-depth analysis of specific events
![Screenshot 2025-06-29 at 21 26 06 (2)](https://github.com/user-attachments/assets/254e3587-deca-4144-9b33-281c94aa78ab)
![Screenshot 2025-06-29 at 21 25 38 (2)](https://github.com/user-attachments/assets/b210f199-6660-44a4-8e02-f9d62fc53a3c)


Navigate through the application using the sidebar menu.  

## 🔧 Configuration

The application can be configured through:
- [`definitions.py`](srilanka/Code/definitions.py): Colors, constants, and UI components
- [`.streamlit/config.toml`](srilanka/.streamlit/config.toml): Streamlit-specific settings



*Sri Lanka - The Pearl of the Indian Ocean* 🇱🇰
