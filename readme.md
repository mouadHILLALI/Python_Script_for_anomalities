#Running the Project
To run the project, please follow these steps:

Navigate to the Project Environment:

Open your terminal and use the command:
cd myenv


Run the Script:

In the terminal, execute the following command to start the anomaly detection script:

python anomaliesScript.py
Modifying the Data Source:

If you'd like to analyze a different dataset, replace the current mock data file with your own. Ensure the file is named mock_data_stream.xlsx and follows the same structure as the original.

#Explanation of the Algorithm:
The Z-score anomaly detection algorithm used here identifies outliers by calculating how many standard deviations a data point lies from the mean. Values above a certain threshold (in this case, 3) are flagged as anomalies, based on the assumption that normal data falls within three standard deviations of the mean in a normal distribution.
