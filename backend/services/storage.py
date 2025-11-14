import os
import uuid

# Example of saving summaries locally for MVP
def save_summary(original_text, summary):
    summary_id = str(uuid.uuid4())
    filename = f"storage/{summary_id}.txt"
    with open(filename, 'w') as f:
        f.write(summary)
    return summary_id

def get_summary_by_id(summary_id):
    filename = f"storage/{summary_id}.txt"
    if os.path.exists(filename):
        with open(filename, 'r') as f:
            return f.read()
    return None 