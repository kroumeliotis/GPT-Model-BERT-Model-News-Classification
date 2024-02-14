from GPTmethods import GPTmethods
from LLAMAmethods import LLAMAmethods
import time
import csv
from google.colab import drive

drive.mount('/content/gdrive')

def run_sentiment(model, model_id, dataset):
    output_file = '/content/gdrive/My Drive/Recommendation/Datasets/recommendations.csv'

    with open(dataset, 'r', newline='', encoding='utf-8') as csvfile:
        csvreader = csv.reader(csvfile)  # Create a CSV reader
        header = next(csvreader, None)  # Skip the header row

        # Open the output CSV file for writing
        with open(output_file, 'w', newline='', encoding='utf-8') as csvfile_out:
            csvwriter = csv.writer(csvfile_out)

            # Add 'evaluation' column to the header only once
            if model+'_evaluation' not in header:
                header.append(model+'_evaluation')
                csvwriter.writerow(header)

            # Loop through each row in the CSV file
            for row in csvreader:
                comment = row['kMeans']
                comment = comment[:200]
                print(f"Comment: {comment}")

                # Run GPT Model
                GPT = GPTmethods(model_id=model_id)
                prediction = GPT.gpt_ratings(comment)  # the prediction
                print(f"Prediction: {prediction}")

                # Add the prediction value to the 'prediction' column for each row
                row.append(prediction)

                # Write the row to the output CSV file
                csvwriter.writerow(row)

                # Add a delay of 5 seconds (reduced for testing)
                time.sleep(2)

            print(f"Predictions added to the 'prediction' column in {output_file}")

# evaluate('kMeans', 'gpt-3.5-turbo', '/content/gdrive/My Drive/Recommendation/Datasets/recommendations.csv')