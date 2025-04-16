import csv
import json

# Read CSV
with open('forum_articles.csv', mode='r', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    dataset = []

    # Convert each row to a prompt-completion format
    for row in reader:
        # Ignore 'date' column and focus on 'title' and 'body'
        prompt = f"Forum: {row['title']}\n\n{row['body'][:500]}"  # First 500 characters of the body as the prompt
        completion = row['body'][500:]  # The rest of the body as completion
        dataset.append({"prompt": prompt, "completion": completion})

# Save to jsonl
with open('forum_articles.jsonl', 'w', encoding='utf-8') as f:
    for entry in dataset:
        f.write(json.dumps(entry) + "\n")

print("Converted CSV to data.jsonl without date column")