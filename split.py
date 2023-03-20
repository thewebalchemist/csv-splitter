import csv
import os


csv_file = "/home/Alkemist/Documents/SEO/Writing/Content Planner/postscraper/assbuster.csv"
output_directory = "/home/Alkemist/Documents/SEO/Writing/Content Planner/postscraper"

csv.field_size_limit(100000000)
max_rows = 4000


def split_csv(csv_file, output_directory, max_rows):
    with open(csv_file, "r") as f:
        reader = csv.DictReader(f)
        rows = []
        file_count = 1
        for i, row in enumerate(reader):
            rows.append(row)
            if i % max_rows == max_rows - 1:
                output_file = os.path.join(output_directory, f"output_{file_count}.csv")
                with open(output_file, "w", newline="") as out:
                    writer = csv.DictWriter(out, fieldnames=["post", "title"])
                    writer.writeheader()
                    writer.writerows(rows)
                file_count += 1
                rows = []
        if rows:
            output_file = os.path.join(output_directory, f"output_{file_count}.csv")
            with open(output_file, "w", newline="") as out:
                writer = csv.DictWriter(out, fieldnames=["post", "title"])
                writer.writeheader()
                writer.writerows(rows)


split_csv(csv_file, output_directory, max_rows)

