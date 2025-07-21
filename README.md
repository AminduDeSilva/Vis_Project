# Sri Lanka's Journey: A Comparative Study with Germany

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://visproject-wrdzidkcglvterjwqprntr.streamlit.app/)

An interactive data visualization application that tells the story of Sri Lanka's socio-economic journey over the past 25 years, comparing it with Germany to provide insights into their respective economic and social landscapes.

## Project Overview

This project explores Sri Lanka's resilience through various challenges, including natural disasters, civil conflicts, terrorist attacks, and the COVID-19 pandemic. Through interactive visualizations, we compare key indicators between Sri Lanka and Germany, including:

- **Economic Indicators**: GDP, Inflation rates
- **Social Metrics**: Happiness index, Quality of life
- **Tourism Impact**: Visitor arrivals and industry growth
- **Historical Events**: Impact of major incidents on national development

## Live Demo

Visit the live application: [Sri Lanka's Journey](https://visproject-wrdzidkcglvterjwqprntr.streamlit.app/)

## Features

- **Interactive Visualizations**: Built with Plotly for dynamic data exploration
- **Comparative Analysis**: Side-by-side comparison between Sri Lanka and Germany
- **Historical Context**: Timeline of major events and their impact
- **Multiple Data Sources**: Comprehensive datasets covering 25+ years
- **Responsive Design**: Works on desktop and mobile devices

## Installation & Setup

### Prerequisites

- Python 3.9+
- Git

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

# Install requirements
pip install -r requirements.txt

# Navigate to the app directory and run
cd srilanka
streamlit run "Code/Sri Lanka's Journey.py"
```

## Project Structure

```
Vis_Project/
├── README.md
├── requirements.txt               # Python dependencies
├── .streamlit/
│   └── config.toml               # Streamlit configuration
├── srilanka/                     # Main application directory
│   ├── Code/
│   │   ├── Sri Lanka's Journey.py # Main Streamlit application
│   │   ├── data_utils.py         # Data processing utilities
│   │   ├── plot_utils.py         # Visualization utilities
│   │   ├── definitions.py        # UI components and constants
│   │   └── pages/                # Additional Streamlit pages
│   │       └── Incidents.py      # Historical incidents analysis
│   ├── data/                     # All datasets
│   │   ├── tourism/              # Tourism arrival data
│   │   ├── inflation/            # Inflation rate data
│   │   ├── gdp/                  # GDP data
│   │   ├── happiness/            # Happiness index data
│   │   └── pictures/             # Images used in the app
│   ├── plots/                    # Generated visualizations
│   ├── Dockerfile                # Docker configuration
│   └── requirements.txt          # Python dependencies
```

## Data Sources

The project uses multiple datasets spanning 25+ years:

- **Tourism Data**: Visitor arrivals for both Sri Lanka and Germany
- **Economic Data**: GDP growth rates and inflation indicators
- **Social Data**: World Happiness Report indices
- **Historical Events**: Major incidents and their timeline

All data sources are documented in the respective data subdirectories.

## Technologies Used

- **Frontend**: Streamlit
- **Data Visualization**: Plotly, Matplotlib, Seaborn
- **Data Processing**: Pandas, NumPy
- **Deployment**: Docker, Streamlit Cloud
- **Development**: Jupyter Notebooks

## Dependencies

```
streamlit>=1.36.0
plotly>=5.22.0
pandas>=2.2.0
numpy>=2.0.0
matplotlib>=3.9.0
seaborn>=0.13.0
openpyxl>=3.1.0
xlrd>=2.0.0
```

See [`requirements.txt`](requirements.txt) for complete list.

## Deployment

### Deploy to Streamlit Cloud

1. Push your code to GitHub
2. Visit [share.streamlit.io](https://share.streamlit.io)
3. Connect your GitHub repository
4. Set main file path: `srilanka/Code/Sri Lanka's Journey.py`
5. Deploy!

## Contributing

This project was developed as part of the "Storytelling with Interactive Data Visualizations" course at TH Rosenheim.


### Development Workflow

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## Usage

1. **Main Dashboard**: Overview of Sri Lanka's journey with key metrics
2. **Comparative Analysis**: Side-by-side comparison with Germany
3. **Historical Timeline**: Major events and their impact
4. **Detailed Incidents**: In-depth analysis of specific events

Navigate through the application using the sidebar menu.

## Configuration

The application can be configured through:
- [`definitions.py`](srilanka/Code/definitions.py): Colors, constants, and UI components
- [`.streamlit/config.toml`](.streamlit/config.toml): Streamlit-specific settings


---

**Sri Lanka 🇱🇰 & Comparative Study with Germany 🇩🇪 ** 

*This project was completed as a group project for the Storytelling with Interactive Data Visualizations coursework at TH Rosenheim* 
