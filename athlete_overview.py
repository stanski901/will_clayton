
# this function takes the tfrrs dataframe as of 3-aug-2025 and summarizes an athlete's data



import pandas as pd



def summarize_athlete(data, name):
    unique_schools = data.loc[data['athlete_name'] == name, 'school'].unique()
    unique_divisions = data.loc[data['athlete_name'] == name, 'division'].unique()
    unique_regions = data.loc[data['athlete_name'] == name, 'region'].unique()
    unique_conferences = data.loc[data['athlete_name'] == name, 'main_conference'].unique()
    unique_events = data.loc[data['athlete_name'] == name, 'event'].unique()
    first_race = min(data.loc[data['athlete_name'] == name, 'parsed_date'])
    last_race = max(data.loc[data['athlete_name'] == name, 'parsed_date'])
    def print_unique(label, unique_values):
        if len(unique_values) == 1:
            print(f"{label}: {unique_values[0]}")
        else:
            print(f"multiple_{label.lower()}s:")
            for value in unique_values:
                print(value)


    print(f'name: {name}')
    print(f'first race: {first_race}\nlast race: {last_race}')
    print_unique('school', unique_schools)
    print_unique('conference', unique_conferences)
    print_unique('region', unique_regions)
    print_unique('division', unique_divisions)
    print(f'unique events:{unique_events}')


