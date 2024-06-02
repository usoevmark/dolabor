import csv

def write_done(current_data, filename):
  """Writes the current data to a csv file."""

  with open(filename, 'w', newline='') as csvfile:
    csvwriter = csv.writer(csvfile)
    csvwriter.writerows(current_data)

