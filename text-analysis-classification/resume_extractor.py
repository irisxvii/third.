import re
import json
import os

resumes = {
    "resume_1": """
    Aswin V Sivan
    Email: aswinvsivan@gmail.com
    Phone: 9938473645
    Software Engineer with 5 years experience.
    """,

    "resume_2": """
    Mariamma Joseph
    Contact: mariammajoseph@outlook.com
    Mobile: 9876543210
    Data Analyst skilled in Python and SQL.
    """,

    "resume_3": """
    Yahya Sulaim
    Email ID: yahme@company.co.in
    Phone Number: 8837463829
    Machine Learning Enthusiast.
    """
}

# Regex patterns
email_pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
phone_pattern = r'(?:\+?\d{1,3}[\s-]?)?(?:\(?\d{3}\)?[\s-]?)?\d{3}[\s-]?\d{4}'

extracted_data = {}

for key, text in resumes.items():
    emails = re.findall(email_pattern, text)
    phones = re.findall(phone_pattern, text)

    email = list(dict.fromkeys(emails))[0] if emails else ""
    phone = list(dict.fromkeys(phones))[0] if phones else ""

    extracted_data[key] = {
        "email": email,
        "phone_number": phone
    }

# Save to JSON
output_path = os.path.join(os.path.dirname(__file__), "output.json")
with open(output_path, "w") as f:
    json.dump(extracted_data, f, indent=4)

print("Extraction complete. Data saved to output.json")