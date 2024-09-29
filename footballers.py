import pandas as pd
import argparse

df = pd.read_csv('/Users/wolastoqeducation/Downloads/pbp-2024.csv')

def get_completion_count(team_id):

    # Filter the DataFrame to include only rows where OffenseTeam is 'KC'
    team_df = df[df['OffenseTeam'] == team_id]
    completion_count = df['IsPass'].sum() - df['IsIncomplete'].sum()
    team_completion_count = team_df['IsPass'].sum() - team_df['IsIncomplete'].sum()
    return team_completion_count

def get_incompletion_count(team_id):

    # Filter the DataFrame to include only rows where OffenseTeam is 'KC'
    team_df = df[df['OffenseTeam'] == team_id]
    incompletion_count = df['IsPass'].sum() + df['IsIncomplete'].sum()
    team_incompletion_count = team_df['IsPass'].sum() + team_df['IsIncomplete'].sum()
    return team_incompletion_count
    # Count the number of times IsPass is 1 in the filtered DataFrame
    #print(f"The number of times IsPass is 1 when OffenseTeam is KC is: {count}")
    #print(f"The number of completed passes for Kansas City on offense is {kc_completion_count}")

def get_oformation_count(team_id):
    
    team_df = df[df['OffenseTeam'] == team_id]
    #shotgun_count = df(['Formation'] == "SHOTGUN")
    team_shotgun_count = team_df['Formation'].apply(lambda x: str(x).upper().split().count('SHOTGUN') if isinstance(x, str) else 0).sum()
    return team_shotgun_count


if __name__ == "__main__": 

    parser = argparse.ArgumentParser(prog="footballers")
    parser.add_argument("team_id")
    args = parser.parse_args()
    print(f"{args.team_id} has {get_completion_count(args.team_id)} completions")
    print(f"{args.team_id} has {get_incompletion_count(args.team_id)} incompletions")
    print(f"{args.team_id} has {get_oformation_count(args.team_id)} SHOTGUN formations")

