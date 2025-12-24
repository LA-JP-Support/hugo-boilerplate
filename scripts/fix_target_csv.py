import csv

source_file = '/Users/TM-MBP1/Documents/GitHub/hugo-boilerplate/docs/glossaries_flowhunt.csv'
target_file = '/Users/TM-MBP1/Documents/GitHub/hugo-boilerplate/docs/target_generation.csv'
target_filename = 'Natural-Language-Processing--NLP-.md'

print(f"Reading from {source_file}...")

found = False
with open(source_file, 'r', encoding='utf-8') as f_in, \
     open(target_file, 'w', encoding='utf-8', newline='') as f_out:
    
    reader = csv.DictReader(f_in)
    writer = csv.DictWriter(f_out, fieldnames=reader.fieldnames)
    writer.writeheader()
    
    for row in reader:
        if row['filename'].strip() == target_filename:
            writer.writerow(row)
            found = True
            break

if found:
    print(f"✅ Successfully wrote entry for {target_filename} to {target_file}")
else:
    print(f"❌ Could not find entry for {target_filename}")
