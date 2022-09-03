import os

for item in os.listdir():
    if "protein_processed.gro" == item:
        print (f"file ({item}) found")