# -*- coding: utf-8 -*-
"""Data import.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1EFRJsTH7jTlGJzu-KSS1WZxGATSJDWXr

    Moving data from google drive into supabase
"""

from google.colab import drive
drive.mount('/content/drive')

!pip install supabase

from supabase import create_client, Client

url = "https://hrtjlralgdecioejfqct.supabase.co"  # Replace with your Supabase project URL
key = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImhydGpscmFsZ2RlY2lvZWpmcWN0Iiwicm9sZSI6ImFub24iLCJpYXQiOjE3NDIzMjg0NDEsImV4cCI6MjA1NzkwNDQ0MX0.Psth4TM1dsMsb4Yxrpfku4LK938H4HL2ORGAmhOVMSU"  # Replace with your Supabase anon/public service key

supabase: Client = create_client(url, key)

pip install python-dotenv psycopg2

import pandas as pd

# Example path to a CSV
df = pd.read_csv('/content/drive/MyDrive/lifting videos/processed_data/barbell biceps curl/barbell biceps curl_1.csv')

# Preview the first few rows
df.head()

import os
import pandas as pd
from supabase import create_client, Client
import uuid

# Supabase connection
SUPABASE_URL = "https://hrtjlralgdecioejfqct.supabase.co"
SUPABASE_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImhydGpscmFsZ2RlY2lvZWpmcWN0Iiwicm9sZSI6ImFub24iLCJpYXQiOjE3NDIzMjg0NDEsImV4cCI6MjA1NzkwNDQ0MX0.Psth4TM1dsMsb4Yxrpfku4LK938H4HL2ORGAmhOVMSU"
supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)

# Path to your folder
data_folder = "/content/drive/MyDrive/lifting videos/processed_data"

# Batch size for inserting records
BATCH_SIZE = 100

def process_and_upload_csv(csv_path, file_name):
    try:
        # Read CSV
        df = pd.read_csv(csv_path)

        # Add required columns
        df['frame_number'] = df.index
        df['timestamp_seconds'] = df.index / 30.0
        df['source_video'] = file_name.replace('.csv', '')
        df['video_id'] = None

        # Convert DataFrame to records
        records = df.to_dict(orient="records")

        # Process in batches
        for i in range(0, len(records), BATCH_SIZE):
            batch = records[i:i + BATCH_SIZE]
            try:
                response = supabase.table("video_frames").insert(batch).execute()
                print(f"✅ Uploaded batch {i//BATCH_SIZE + 1} of {file_name}")
            except Exception as e:
                print(f"❌ Error uploading batch {i//BATCH_SIZE + 1} of {file_name}: {str(e)}")

        return True
    except Exception as e:
        print(f"❌ Error processing {file_name}: {str(e)}")
        return False

# Main processing loop
successful_files = 0
failed_files = 0

for root, dirs, files in os.walk(data_folder):
    for file in files:
        if file.endswith(".csv"):
            csv_path = os.path.join(root, file)
            print(f"📁 Processing {file}...")

            if process_and_upload_csv(csv_path, file):
                successful_files += 1
            else:
                failed_files += 1

print(f"\nUpload Complete!")
print(f"Successfully processed: {successful_files} files")
print(f"Failed to process: {failed_files} files")

print({key: type(value) for key, value in row.items()})
