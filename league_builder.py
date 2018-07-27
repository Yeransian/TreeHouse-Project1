
import csv

def get_player(file, new_line, delimiter):
    with open("soccer_players.csv", "r") as csvfile:
        file_reader = csv.DictReader(csvfile, delimiter=delimiter)
        players = list(file_reader)
        return players


def sort_players(players):
    inexperienced = []
    experienced = []
    for player in players:                       # loop through players
        if player['Soccer Experience'] == "NO":  # assign group
            inexperienced.append(player)
        else:
            experienced.append(player)
    return inexperienced, experienced


def assign_players(players, team_list):        # assign players to teams.4
    index = 0
    sorted_players = sort_players(players)
    player_list = []                           # Hold the players in a list
    teams = []
    for key, value in team_list.items():       # break team dictionary into a list
        teams.append(key)
    for group in sorted_players:               # loop through the 2 player groups
        range = len(teams) - 1                 # set range = to the number of teams, use this   # value to select a team based on its current index
        for player in group:                   # loop through players in this group
            player['Team'] = teams[index]      # assign player to the current team (index value)
            player_list.append(player)         # add the updated player to a clean list
            if index < range:                  # if index is less than the number of teams,
                index += 1                     # increment by one..
            else:
                index = 0                      # otherwise reset the index
    return player_list                         # return an updated list of players with their team assignments


def populate_teams(team_list, player_list):    # Populate the list of teams
    for player in player_list:
        team = player['Team']
        if team in team_list:
            team_list[team].append(player)
    return team_list


def write_teams(teams):
    file = open('teams.txt', 'a')
    for team, players in teams.items():                  # loop through the teams
        file.write(team + "\n")                          # for each team, write the team name
        for player in players:                           # loop through players and write player info
            name = player['Name']                        # set vars to the write line is easier to read
            experience = player['Soccer Experience']
            guardians = player['Guardian Name(s)']
            file.write("{}, {}, {}\n".format(name, experience, guardians))
        file.write("\n")


def write_parent_letters(players):
    for player in players:                        # for each player
        guardian = player['Guardian Name(s)']     # set up variables
        team = player['Team']
        name = player['Name']
        date = 'August 12th'
        time = '6am'
        filename = name.replace(' ', '_')         # set up lower case _ separated file names
        filename = filename.lower() + '.txt'
        file_path = 'welcome-letters/' + filename # put these in a separate directory, to keep things a little neater...
        file = open(file_path, 'a')
        file.write('Dear {},\n\n'                 # stuff to write
                   'We are pleased to inform you that your child, {}, has been assigned '
                   'to the {} soccer team! \n'
                   'Practice begins {} at {}.\n'
                   'We cannot wait to see you!\n\n'
                   'Thanks,  \n '
                   '- Soccer Coach'.format(guardian, name, team, date, time))


####### MAIN #######
if __name__ == "__main__":
    imported_players = get_player('soccer_players.csv', '', ',') # open file & get players
    team_list = {           # team names
        'Sharks': [],
        'Dragons': [],
        'Raptors': []
    }
    assigned_players = assign_players(imported_players, team_list) # assign players to teams
    teams = populate_teams(team_list, assigned_players)            # populate team lists
    write_teams(teams)                                             # output file
    write_parent_letters(assigned_players)                         # write parent letters
