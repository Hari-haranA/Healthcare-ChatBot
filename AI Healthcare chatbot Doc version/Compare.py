import csv

def compare_csv_files(file1, file2):
    mismatching_lines = []

    with open(file1, 'r') as f1, open(file2, 'r') as f2:
        reader1 = csv.reader(f1)
        reader2 = csv.reader(f2)

        for line_num, (row1, row2) in enumerate(zip(reader1, reader2), start=1):
            if row1 != row2:
                mismatching_lines.append(f"Line {line_num}: {', '.join(row1)} != {', '.join(row2)}")

    return mismatching_lines

if __name__ == "__main__":
    file1 = "DiseasesWithSymptoms.csv"
    file2 = "DatasetWithSymptomsCleaned.csv"

    mismatching_lines = compare_csv_files(file1, file2)

    if not mismatching_lines:
        print("The CSV files are identical.")
    else:
        print("Mismatching lines:")
        for line in mismatching_lines:
            print(line)
