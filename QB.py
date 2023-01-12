import pickle 

class QB:


    def __init__(self, season,team, name, position, status, height, weight, college,
    player_id, years_exp, headshot_url,qbRankWins, season_type, 
        completions, attempts, passing_yards,
        passing_tds, interceptions, sacks, sack_yards, sack_fumbles,
        sack_fumbles_lost, passing_air_yards, passing_yards_after_catch,
        passing_first_downs, passing_epa, passing_2pt_conversions, pacr, carries, rushing_yards, rushing_tds, rushing_fumbles,
        rushing_fumbles_lost, rushing_first_downs, rushing_epa,
        rushing_2pt_conversions,  fantasy_points, fantasy_points_ppr, games):
        
        self.season = season
        self.team = team 
        self.name = name
        self.position = position 
        self.status = status 
        self.height = height 
        self.weight = weight 
        self.college = college 
        self.player_id = player_id 
        self.years_exp = years_exp 
        self.headshot_url = headshot_url 
        self.qbRankWins = qbRankWins 
        self.season_type = season_type
        self.completions = completions
        self.attempts = attempts
        self.passing_yards = passing_yards
        self.passing_tds = passing_tds
        self.interceptions = interceptions
        self.sacks = sacks
        self.sack_yards = sack_yards
        self.sack_fumbles = sack_fumbles
        self.sack_fumbles_lost = sack_fumbles_lost
        self.passing_air_yards = passing_air_yards
        self.passing_yards_after_catch = passing_yards_after_catch
        self.passing_first_downs = passing_first_downs
        self.passing_epa = passing_epa
        self.passing_2pt_conversions = passing_2pt_conversions
        self.pacr = pacr
        self.carries = carries
        self.rushing_yards = rushing_yards
        self.rushing_tds = rushing_tds
        self.rushing_fumbles = rushing_fumbles
        self.rushing_fumbles_lost = rushing_fumbles_lost
        self.rushing_first_downs = rushing_first_downs
        self.rushing_epa = rushing_epa
        self.rushing_2pt_conversions = rushing_2pt_conversions
        self.fantasy_points = fantasy_points
        self.fantasy_points_ppr = fantasy_points_ppr
        self.games = games

    def save(self, fileName):
        """Save thing to a file."""
        f = open(fileName,"wb")
        pickle.dump(self,f
        )
        f.close()
    def load(fileName):
        """Return a thing loaded from a file."""
        f = open(fileName,"rb")
        obj = pickle.load(f)
        f.close()
        return obj  
    
        

    
    
    
        