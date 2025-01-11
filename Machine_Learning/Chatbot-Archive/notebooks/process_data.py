import pandas as pd

# Load the chatbot archive dataset
file_path = '../datasets/chatbots_dataset.csv'

# Read the CSV file
try:
    chatbot_data = pd.read_csv(file_path)
    # Display basic information about the dataset
    summary = {
        "Number of Records": len(chatbot_data),
        "Columns": list(chatbot_data.columns),
        "Missing Values": chatbot_data.isnull().sum().to_dict(),
    }
    print(summary)
except FileNotFoundError:
    print("CSV file not found. Please check the file path.")
