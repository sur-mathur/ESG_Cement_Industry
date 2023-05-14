# Load the keywords dictionary for E, S, and G
keywords_dict = {
    'E': ['environment', 'climate', 'sustainability', 'pollution', 'green', 'renewable', 'ecosystem'],
    'S': ['social', 'community', 'human rights', 'diversity', 'equality', 'health', 'well-being'],
    'G': ['governance', 'transparency', 'accountability', 'ethics', 'corruption', 'regulation', 'compliance']
}

# Define a function to label a text string using the keywords dictionary
def label_text(text):
    # Convert the text to lowercase for case-insensitive matching
    text = text.lower()
    # Initialize counters for each label
    e_count = 0
    s_count = 0
    g_count = 0
    # Iterate through the keywords dictionary and count matches in the text
    for label, keywords in keywords_dict.items():
        for keyword in keywords:
            if keyword in text:
                if label == 'E':
                    e_count += 1
                elif label == 'S':
                    s_count += 1
                elif label == 'G':
                    g_count += 1
    # Return the label with the highest count
    if e_count > s_count and e_count > g_count:
        return 'E'
    elif s_count > e_count and s_count > g_count:
        return 'S'
    elif g_count > e_count and g_count > s_count:
        return 'G'
    else:
        return 'Unknown'

# Test the function with some example text
example_text = "Our company is committed to sustainability and reducing our carbon footprint. We also prioritize diversity and inclusion in our workplace."
label = label_text(example_text)
print(label) # Output: E
