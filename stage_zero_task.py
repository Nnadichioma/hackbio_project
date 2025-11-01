"""
HackBio Internship — Stage 0 Task
Team: Leucine

# Task: 
# Write a simple Python script for printing the names, Slack username,
# country, one hobby, affiliations of people on your team, 
# and the DNA sequence of the genes they love most.
# Author: Chioma Nnadi
# GitHub: https://github.com/Nnadichioma
# LinkedIn: https://www.linkedin.com/in/NnadiChioma/
"""
# Created a list of dictionaries for team_leucine_info
team_leucine_info = [
    {
    "Name":"Chioma Nnadi",
    "Slack": "Chioma",
    "Country": "Nigeria",
    "Hobby": "Writing",
    "Affiliation": "None",
    "Gene": "BRCA1",
    "Sequence": "GCTGAGACTTCCTGGACGGGGGACAGGCTGTGGGGTTTCTCAGATAACTGGGCCCCTGCGCTCAGGAGGC"
},
    
    {
    "Name": "Kashish Arora",
    "Slack": "Kashish",
    "Country": "India",
    "Hobby": "Reading",
    "Affiliation": "University of Glasgow",
    "Gene": "CDKN1A",
    "Sequence": "GAACATGTCCCAACATGTTG"
},
     
    {
    "Name": "Keola Merl Joanes",
    "Slack": "Keola",
    "Country": "India",
    "Hobby": "Reading",
    "Affiliation": "PCCAS.",
    "Gene": "HBB gene",
    "Sequence": "GGGGGATATTATGAAGGGCCTTGAGCATCTGGATTCTGCCTAATAAAAAACATTTATTTTCATTGCAA"
},
     
    {
    "Name": "Lavinia Dorothea F Joseph",
    "Slack": "Lavinia",
    "Country": "Antigua & Barbuda",
    "Hobby": "Sudoku",
    "Affiliation": "University Mohammed V, Faculty of Medicine and Pharmacy",
    "Gene": "DHh gene",
    "Sequence": "GTTCCAGGTAGTGCCTGAAACTACTTTTCTGAAGAAGTATAATTAAAAGTAATCTTGTTTTGAGAA"
},
     
    {
    "Name": "Atairoro Joshua",
    "Slack": "Atairoro Joshua",
    "Country": "Nigeria",
    "Hobby": "Music",
    "Affiliation": "None",
    "Gene": "BRCA1",
    "Sequence": "ATGGAAGTTGTCATTTTATAAAGTCAGTAGTTTCTTTGGCAGCAATGCCAGGAAAGGCTCTGAGGAA"
},
     
    {
    "Name": "Bezaleel Akinbami",
    "Slack": "B3z",
    "Country": "Nigeria",
    "Hobby": "Gaming",
    "Affiliation": "None",
    "Gene": "None",
    "Sequence": "None"
},
     
    {
    "Name": "Sharon Addy",
    "Slack": "Sharon Addy",
    "Country": "Ghana",
    "Hobby": "Reading",
    "Affiliation": "None",
    "Gene": "MIR1-1",
    "Sequence": "UGGAAUGUAAAGAAGUAUGUAU"
},
    {
    "Name": "Jegede Joseph.O",
    "Slack": "Joseph",
    "Country": "Nigeria",
    "Hobby": "Gaming",
    "Affiliation": "Obafemi Awolowo University",
    "Gene": "None",
    "Sequence": "None"
}
]

# Validate DNA contains only A, T, C, G
def validate_dna(seq):
    if seq is None:
        return False
    valid = {"A", "T", "C", "G"}
    return set(seq.upper()).issubset(valid)

# Calculate GC content
def gc_content(seq):
    g = seq.count("G")
    c = seq.count("C")
    return round((g + c) / len(seq) * 100, 2)

# Print results
# Iterate through each team member and print their details
for member in team_leucine_info:
    seq = member["Sequence"]
    print(f"\nName: {member['Name']}")
    print(f"Slack: {member['Slack']}")
    print(f"Country: {member['Country']}")
    print(f"Hobby: {member['Hobby']}")
    print(f"Affiliation: {member['Affiliation']}")
    print(f"Favorite Gene: {member['Gene']}")

    if validate_dna(seq):
        print(f"GC Content: {gc_content(seq)}%")
    else:
        print("GC Content: N/A (Invalid or no DNA sequence)")






