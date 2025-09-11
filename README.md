# 🔍 Vigil
**Real-time Log and Video Analyzer**

Vigil is a powerful Python-based monitoring tool that provides real-time anomaly detection for time-series data streams. Using advanced statistical analysis (Z-score methodology), Vigil helps you identify unusual patterns and outliers in your log data, making it an essential tool for system monitoring, data quality assurance, and operational intelligence.

![Python](https://img.shields.io/badge/python-v3.8+-blue.svg)
![License](https://img.shields.io/github/license/shivraj-S-bhatti/vigil.svg)
![Status](https://img.shields.io/badge/status-active-green.svg)

## ✨ Key Features

- **Real-time Monitoring**: Stream and analyze time-series data in real-time
- **Statistical Anomaly Detection**: Uses Z-score analysis with configurable thresholds
- **Interactive GUI**: User-friendly Tkinter interface for easy operation
- **Flexible Data Input**: Supports CSV files with timestamp-value pairs
- **Configurable Thresholds**: Adjust sensitivity of anomaly detection
- **Live Alerts**: Real-time notifications when anomalies are detected
- **Sample Data Included**: Pre-configured with sample logs for testing
- **Portable Executable**: Can be packaged as a standalone Windows executable

## 🚀 Quick Start

### Prerequisites

- Python 3.8 or higher
- Git (for cloning the repository)
- GUI environment (for the interactive interface)
  - Note: GUI features require a desktop environment with tkinter support

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/shivraj-S-bhatti/vigil.git
   cd vigil
   ```

2. **Create a virtual environment** (recommended)
   ```bash
   python -m venv .venv
   
   # Windows
   .venv\Scripts\activate
   
   # macOS/Linux
   source .venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

### Running Vigil

#### Basic Usage
```bash
python src/main.py
```

#### With Custom Parameters
```bash
# Specify a custom CSV file and threshold
python src/main.py --file your_data.csv --threshold 2.5
```

#### Command Line Options
- `--file FILE`: Path to CSV file (default: `assets/sample_logs.csv`)
- `--threshold THRESHOLD`: Z-score threshold for anomaly detection (default: `3.0`)

## 📊 How It Works

### Data Format
Vigil expects CSV files with the following structure:
```csv
timestamp,value
2025-01-01 09:00:00.000,0.152
2025-01-01 09:00:00.100,-0.471
2025-01-01 09:00:00.200,0.473
...
```

### Anomaly Detection Algorithm
1. **Sliding Window Analysis**: Uses a configurable window size (default: 200 points)
2. **Statistical Calculation**: Computes rolling mean and standard deviation
3. **Z-score Computation**: Calculates Z-scores for each data point
4. **Threshold Comparison**: Flags points exceeding the specified threshold
5. **Real-time Alerting**: Displays alerts for detected anomalies

The Z-score formula used:
```
Z = (x - μ) / σ
```
Where:
- `x` = current value
- `μ` = rolling mean
- `σ` = rolling standard deviation

## 🎯 Usage Guide

### Using the GUI

1. **Launch the Application**
   ```bash
   python src/main.py
   ```

2. **Load Your Data**
   - Click "Open CSV" to select your time-series data file
   - The file should have timestamp and value columns

3. **Configure Detection**
   - Adjust the "Z-score threshold" (typical values: 2.0-4.0)
   - Lower values = more sensitive detection
   - Higher values = less sensitive detection

4. **Start Monitoring**
   - Click "Start" to begin real-time analysis
   - Watch for anomaly alerts in the log window
   - Click "Stop" to halt the analysis

### Sample Data
The project includes sample log data (`assets/sample_logs.csv`) for testing and demonstration purposes.

## 📁 Project Structure

```
vigil/
├── src/
│   ├── main.py          # Application entry point
│   ├── ui.py            # Tkinter GUI implementation
│   ├── pipeline.py      # Real-time processing pipeline
│   ├── rules.py         # Anomaly detection algorithms
│   └── dataio.py        # Data loading and processing
├── assets/
│   └── sample_logs.csv  # Sample time-series data
├── packaging/
│   └── build.exe.bat    # Windows executable build script
├── requirements.txt     # Python dependencies
├── README.md           # This file
└── LICENSE             # Project license
```

## 🛠️ Development

### Building from Source

#### For Development
```bash
# Install development dependencies
pip install -r requirements.txt

# Run tests (if available)
python -m pytest

# Run the application
python src/main.py
```

#### Creating Windows Executable
```bash
# On Windows
cd packaging
build.exe.bat

# The executable will be created at: dist/VIGIL-Logwatch.exe
```

### Dependencies
- **pandas**: Data manipulation and analysis
- **numpy**: Numerical computations and statistical analysis
- **tkinter**: GUI framework (included with Python)

## 🔧 Configuration

### Threshold Settings
- **Low sensitivity** (threshold > 3.0): Detects only extreme anomalies
- **Medium sensitivity** (threshold 2.0-3.0): Balanced detection
- **High sensitivity** (threshold < 2.0): Detects subtle anomalies

### Window Size
The analysis window size is automatically adjusted based on data size, with a default maximum of 200 points and minimum of data_length/2.

## 📈 Use Cases

- **System Monitoring**: Detect unusual spikes in CPU, memory, or network usage
- **Application Performance**: Monitor response times and throughput
- **Data Quality**: Identify data collection issues or sensor malfunctions
- **Financial Analysis**: Detect unusual trading patterns or market anomalies
- **IoT Monitoring**: Monitor sensor data for device malfunctions
- **Log Analysis**: Identify unusual patterns in application logs

## 🤝 Contributing

We welcome contributions! Please follow these steps:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

### Development Guidelines
- Follow PEP 8 style guidelines
- Add docstrings to new functions
- Include tests for new features
- Update documentation as needed

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- Built with Python and the scientific computing ecosystem
- Uses pandas for efficient data processing
- Statistical methods based on standard Z-score analysis
- GUI powered by tkinter for cross-platform compatibility

## 📞 Support

If you encounter any issues or have questions:

1. Check the existing issues in the GitHub repository
2. Create a new issue with detailed information about your problem
3. Include sample data and error messages if applicable

---

**Made with ❤️ for the monitoring and data analysis community**
