import pandas as pd

# Load the chatbot archive dataset (example file path)
file_path = '/mnt/data/chatbot_archive.csv'

# Read the CSV file
try:
    chatbot_data = pd.read_csv(file_path)
    # Display basic information about the dataset
    summary = {
        "Number of Records": len(chatbot_data),
        "Columns": list(chatbot_data.columns),
        "Missing Values": chatbot_data.isnull().sum().to_dict(),
    }
except FileNotFoundError:
    summary = "CSV file not found. Please upload your chatbot archive file."

summary

