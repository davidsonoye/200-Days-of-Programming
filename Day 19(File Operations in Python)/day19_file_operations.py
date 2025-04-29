# Step 1: Create and write initial smart meter readings
filename = "smart_meter_readings.txt"
initial_readings = [
    "Voltage: 230V\n",
    "Current: 5A\n",
    "Power: 1150W\n"
]

# Create a file and write to it
fh = open(filename, 'w')  # create file for writing
fh.writelines(initial_readings)  # write a list of readings
fh.close()  # close file

# Step 2: Read the entire file contents
fh = open(filename, 'r')  # open file for reading
all_contents = fh.read()
print("=== Read Entire File ===")
print(all_contents)
fh.close()

# Step 3: Read file line by line using readline()
fh = open(filename, 'r')
print("=== Read Line by Line ===")
print(fh.readline().strip())  # reads first line
print(fh.readline().strip())  # reads second line
print(fh.readline().strip())  # reads third line
fh.close()

# Step 4: Read all lines into a list
fh = open(filename, 'r')
lines = fh.readlines()
print("=== Read Lines as List ===")
for line in lines:
    print(line.strip())
fh.close()

# Step 5: Append new readings
more_readings = [
    "Frequency: 50Hz\n",
    "Energy: 3.5kWh\n"
]
fh = open(filename, 'a')  # open file for appending
fh.writelines(more_readings)
fh.close()

# Step 6: Confirm all contents again
fh = open(filename, 'r')
print("=== Final File Contents After Append ===")
print(fh.read())
fh.close()
