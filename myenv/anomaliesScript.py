import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_excel("../mockData/mock_data_stream.xlsx")

def calculate_z_score(value, mean, std_dev):
    if std_dev == 0:
        return 0
    return (value - mean) / std_dev

def calculate_z_scores(data):
    mean = data['Metric'].mean()
    std_dev = data['Metric'].std()
    data['Z_Score'] = data['Metric'].apply(lambda x: calculate_z_score(x, mean, std_dev))
    return data


data_with_z_scores = calculate_z_scores(data)

def detect_anomalies(data, threshold=3):
    data['Anomaly'] = data['Z_Score'].apply(lambda x: abs(x) > threshold)
    return data
data_with_anomalies = detect_anomalies(data_with_z_scores)

def plot_anomalies(data):
    plt.figure(figsize=(12, 6))
    
    plt.plot(data['Metric'], label='Metric', color='blue', marker='o', markersize=3, linestyle='-', linewidth=1)
    
    anomalies = data[data['Anomaly']]
    plt.scatter(anomalies.index, anomalies['Metric'], color='red', label='Anomaly', s=50, edgecolor='black')

    plt.title('Anomaly Detection in Data Stream')
    plt.xlabel('Index')
    plt.ylabel('Metric Value')
    plt.legend()
    
    plt.show()

plot_anomalies(data_with_anomalies)
