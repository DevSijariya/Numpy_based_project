import csv
import numpy as np
data=[]
with open(r"C:\Users\sansk\Downloads\MER_T07_02A-2020-02-03.csv",'r') as csvfile:
    file_reader=csv.reader(csvfile,delimiter=',')
    for row in file_reader:
        data.append(row)
data=np.array(data)
# 1. Explore the important attributes like dimension,shape, data type etc, of the array formed above
print("Shape of the given data is ",data.shape)
print("Dimensions of given data is",data.ndim)
print("Data type of given data is",data.dtype)
# 2. Print the data contained in the first 10 rows of the 4th column
print("data in 4th column \n",data[0:11,3])
# 3. Which row serves as the headers/titles for all the columns.
print("First row serves as the headers/titles for all the columns \n",data[0,:])
# 4. Print the data contained in column 2 and 3 from row 1 till row 20
print("data contained in 2 and 3 column\n",data[0:21,1:3])
# 5. Print the data present in only the first three and the last three rows of all the columns in a single output.
print("Data present in the first three and last three rows of all column",data[0:4,:],data[8214:8217:])
# 6. Sort the data on the basis of net amount of electricity generated irrespective of the source.
print("Sort data ",np.argsort(data[:,2]))
# 7. Find the total amount of electricity generated using coal and nuclear between 1949-1990.
# ( In this dataset, rows containing monthly data express date in the format 'YYYYMM'. Rows containing annual data express the date in the format 'YYYY13'.)
msn_column_index = 0
date_column_index = 1
value_column_index = 2

coal_data = data[data[:, msn_column_index] == 'CLETPUS']
nuclear_data = data[data[:, msn_column_index] == 'NUETPUS']

start_year = 1949
end_year = 1990

def is_within_date_range(date):
    year = int(date[:4])
    return start_year <= year <= end_year

filtered_coal_data = coal_data[np.vectorize(is_within_date_range)(coal_data[:, date_column_index])]
filtered_nuclear_data = nuclear_data[np.vectorize(is_within_date_range)(nuclear_data[:, date_column_index])]
total_coal_generation = np.sum(filtered_coal_data[:, value_column_index].astype(float))
total_nuclear_generation = np.sum(filtered_nuclear_data[:, value_column_index].astype(float))

print("Total coal generation between 1949-1990:", total_coal_generation)
print("Total nuclear generation between 1949-1990:", total_nuclear_generation)

# 8. Print all the unique sources of Energy generation present in the dataset
print("Unique sources of Energy generation present in the dataset ",np.unique(data[1:,0]))

# 9. Print all the details(annual) where the energy source is Wind Energy. Use the concept of masking to filter the data.
Wind_data = data[data[:, msn_column_index] == 'WDETPUS']
print("Wind energy sources detail \n ",Wind_data)
# 10. Print the Total Energy generated in the USA till date
energy_column_index = 2  # Adjust this index according to your dataset

total_energy_generated = 0

# Loop through the data and accumulate energy values
for row in data[1:]:  # Skip the header row
    energy_value_str = row[energy_column_index]
    
    if energy_value_str != "Not Available":
        energy_value = float(energy_value_str)
        total_energy_generated += energy_value

# Print the total energy generated till date
print("Total Energy Generated:", total_energy_generated)

# 11. Print the average annual energy generated from wind in the USA and also the standard  deviation present in the energy generation
energy_generation_column = data[:, 1]

# Convert energy generation values to numeric data
energy_generation_numeric = np.array(energy_generation_column[1:], dtype=float)  # Skipping the header row

# Calculate average annual energy generated and standard deviation
average_energy = np.mean(energy_generation_numeric)
std_deviation = np.std(energy_generation_numeric)

print("Average annual energy generated:", average_energy)
print("Standard deviation of energy generation:", std_deviation)

# 12. What and when was the maximum annual energy generated?
energy_column_index = 2  
date_column_index = 1  
max_energy = -1  # Initialize with a small value
max_energy_date = ""

# Loop through the data and find the maximum energy value and its date
for row in data[1:]:  # Skip the header row
    energy_value_str = row[energy_column_index]
    
    if energy_value_str != "Not Available":
        energy_value = float(energy_value_str)
        date = row[date_column_index]
        
        if energy_value > max_energy:
            max_energy = energy_value
            max_energy_date = date

# Print the maximum annual energy generated and its corresponding date
print("Maximum Annual Energy Generated:", max_energy)
print("Date:", max_energy_date)


# 13. Find from the above data if the energy production in the USA has increased in the last 10 years.
energy_column_index = 2  
date_column_index = 1  

# Define the years for the analysis
current_year = 2023
last_10_years = range(current_year - 10, current_year)
previous_10_years = range(current_year - 20, current_year - 10)

# Calculate total energy production for the last 10 years
total_energy_last_10_years = 0
for row in data[1:]:  # Skip the header row
    energy_value_str = row[energy_column_index]
    date = int(row[date_column_index].split('-')[0])  # Extract year
    
    if energy_value_str != "Not Available" and date in last_10_years:
        energy_value = float(energy_value_str)
        total_energy_last_10_years += energy_value

# Calculate total energy production for the 10 years preceding the last 10 years
total_energy_previous_10_years = 0
for row in data[1:]:  # Skip the header row
    energy_value_str = row[energy_column_index]
    date = int(row[date_column_index].split('-')[0])  # Extract year
    
    if energy_value_str != "Not Available" and date in previous_10_years:
        energy_value = float(energy_value_str)
        total_energy_previous_10_years += energy_value

# Compare energy production
if total_energy_last_10_years > total_energy_previous_10_years:
    print("Energy production has increased in the last 10 years.")
else:
    print("Energy production has not increased in the last 10 years.")

# 14. What is the trend in the energy generated from wind over the years? Which source of energy has been the largest contributor to the annual electricity production over the years.
#largest contributor to the annual electricity production over the years
from collections import defaultdict
# Replace with the index of the column containing energy generation data
energy_column_index = 2  # Adjust this index according to your dataset
date_column_index = 1  # Adjust this index according to your dataset

# Create a dictionary to store total energy generated for each year
total_energy_by_year = defaultdict(float)

# Create a dictionary to store the largest energy contributor for each year
largest_contributor_by_year = {}

# Loop through the data and calculate total energy and largest contributor for each year
for row in data[1:]:  # Skip the header row
    energy_value_str = row[energy_column_index]
    date_parts = row[date_column_index].split('-')
    year = int(date_parts[0])
    energy_source = row[0]  # Assuming energy source is in the first column
    
    if energy_value_str != "Not Available":
        energy_value = float(energy_value_str)
        total_energy_by_year[year] += energy_value
        
        if year not in largest_contributor_by_year or energy_value > largest_contributor_by_year[year][0]:
            largest_contributor_by_year[year] = (energy_value, energy_source)

# Analyze the trend in energy generation over the years
previous_year = None
for year, total_energy in sorted(total_energy_by_year.items()):
    print(f"Year: {year}, Total Energy Generated: {total_energy:.2f} GWh")
    
    if previous_year is not None:
        trend = "increased" if total_energy > total_energy_by_year[previous_year] else "decreased"
        print(f"Trend: Energy generation {trend} compared to {previous_year}")
    
    if year in largest_contributor_by_year:
        largest_contributor = largest_contributor_by_year[year][1]
        print(f"Largest Contributor: {largest_contributor}")
    
    print("------------------\n------------------\n")
    
    previous_year=year
# 15. Which renewable source of energy is expected to meet the major demand of energy in the coming years. Can we predict an estimate for the same.

# 16. Compute the contribution of wind, solar, and their combined contribution compared to the total energy generation in the USA, and answer whether the national grid is fundamentally shifting toward wind energy? Use numpy and appropriate metrics to answer the question.
