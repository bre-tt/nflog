import pandas as pd
df = pd.read_csv('/Users/wolastoqeducation/Downloads/pbp-2024.csv')
# Filter the DataFrame to include only rows where OffenseTeam is 'KC'
kc_df = df[df['OffenseTeam'] == 'KC']
completion_count = df['IsIncomplete'].sum()
kc_completion_count = df['[kc_df]' & df['IsIncomplete']].sum()
# Count the number of times IsPass is 1 in the filtered DataFrame
count = kc_df['IsPass'].sum()
print(f"The number of times IsPass is 1 when OffenseTeam is KC is: {count}")
print(f"The number of completed passes for Kansas City on offense is {kc_completion_count}")
