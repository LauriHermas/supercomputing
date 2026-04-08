import random
from pathlib import Path

import numpy as np


# Folder that contains the .npy files
DATA_FOLDER = Path("/projappl/project_2018026/super_data")

# We must use at least 15 random files
HOW_MANY_FILES = 15


def main():
	# 1) Find all .npy files
	all_files = list(DATA_FOLDER.glob("*.npy"))

	if len(all_files) < HOW_MANY_FILES:
		print("Not enough files for analysis.")
		print(f"Found only {len(all_files)} files.")
		return

	# 2) Pick 15 random files
	selected_files = random.sample(all_files, HOW_MANY_FILES)

	# 3) Take one value from each file and sum the values
	total_sum = 0.0
	results = []

	for file_path in selected_files:
		data = np.load(file_path)
		value = float(data.flat[0])  # first value in the file
		total_sum += value
		results.append((file_path.name, value))

	# 4) Show results to the user
	print("ANALYYSI")
	print("MITÄ ANALYSOITIIN: Ensimmäinen arvo 15 satunnaisesta tiedostosta kansiossa super_data1")
	print()

	print("Tiedostot ja arvot:")
	for file_name, value in results:
		print(f"- {file_name}: {value}")

	print()
	print(f"Lopullinen summa 15 arvosta: {total_sum}")


if __name__ == "__main__":
	main()
