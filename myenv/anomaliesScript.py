import pandas as pd
import matplotlib.pyplot as plt

# Attempt to read the data, handling potential file-related errors
try:
    data = pd.read_excel("../mockData/mock_data_stream.xlsx")
except FileNotFoundError:
    print("Error: File not found. Please check the file path.")
    exit()
except Exception as e:
    print(f"Error reading file: {e}")
    exit()

# Function to calculate Z-score, handling cases where std_dev = 0
def calculate_z_score(value, mean, std_dev):
    if std_dev == 0:
        return 0
    return (value - mean) / std_dev

# Main function to calculate Z-scores for the 'Metric' column in the dataset
def calculate_z_scores(data):
    # Handle missing column
    if 'Metric' not in data.columns:
        print("Error: 'Metric' column missing from data.")
        exit()
        
    mean = data['Metric'].mean()
    std_dev = data['Metric'].std()
    data['Z_Score'] = data['Metric'].apply(lambda x: calculate_z_score(x, mean, std_dev))
    return data

# Apply Z-score calculation to detect anomalies based on a defined threshold
def detect_anomalies(data, threshold=3):
    data['Anomaly'] = data['Z_Score'].apply(lambda x: abs(x) > threshold)
    return data

# Plotting function to visualize anomalies
def plot_anomalies(data):
    plt.figure(figsize=(12, 6))
    plt.plot(data['Metric'], label='Metric', color='blue', marker='o', markersize=3, linestyle='-', linewidth=1)
    
    # Highlight anomalies in the plot
    anomalies = data[data['Anomaly']]
    plt.scatter(anomalies.index, anomalies['Metric'], color='red', label='Anomaly', s=50, edgecolor='black')
    
    plt.title('Anomaly Detection in Data Stream')
    plt.xlabel('Index')
    plt.ylabel('Metric Value')
    plt.legend()
    
    plt.show()

# Run functions to process data and visualize results
data_with_z_scores = calculate_z_scores(data)
data_with_anomalies = detect_anomalies(data_with_z_scores)
plot_anomalies(data_with_anomalies)
