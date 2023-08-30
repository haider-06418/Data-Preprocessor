# Analysis Functions for Ticket Analysis


# imports
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime


# Ticket Duration in hours
def ticket_duration_hours(row):
    format_str = '%Y-%m-%d %H:%M:%S' 
    start_time = datetime.strptime(row['Created'], format_str)
    end_time = datetime.strptime(row['Close Time'], format_str)

    duration = end_time - start_time
    total_hours = duration.total_seconds() / 3600

    return total_hours


# Missing Fields analysis Neighbourhood wise 
def analyze_neighbourhood_missing_fields(df):
    scenarios = {
        "House # Empty": (df['Type'] == 'house') & df['House #'].isna(),
        "Apartment # Empty": (df['Type'] == 'apartment') & df['Apartment #'].isna(),
        "Building Name Empty": (df['Type'] == 'apartment') & df['Building Name'].isna(),
    }

    for scenario, condition in scenarios.items():
        print(f"\nCounts for scenario '{scenario}':")
        counts = df.loc[condition, 'Neighbourhood'].value_counts()
        print(counts)
        
        counts.plot(kind='bar', figsize=(10, 5))
        plt.title(f"Counts for scenario '{scenario}'")
        plt.ylabel('Count')
        plt.show()
