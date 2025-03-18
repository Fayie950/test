import re

# I. Extract email addresses
text = "Please contact faith@osiriuniversity.org and pg244164h@cuz.ac.zw for further info."
emails = re.findall(r"[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+", text)
print("Emails:", emails)

# II. Validate a date in "YYYY-MM-DD" format
date = "2025-03-18"
date_pattern = r"^\d{4}-\d{2}-\d{2}$"
if re.match(date_pattern, date):
    print("Valid date format.")
else:
    print("Invalid date format.")

# III. Replace occurrences of a word
text = "Hello world! This world is great!"
updated_text = re.sub(r"world", "Fafie", text)
print("Updated text:", updated_text)

# IV. Split a string by non-alphanumeric characters
string = "Hello! How are you? I'm fine."
split_text = re.split(r"[^a-zA-Z0-9]", string)
print("Split text:", split_text)
