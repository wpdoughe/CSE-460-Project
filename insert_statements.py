def seasons(year, gp, w, l, otl, sol, pts, mp):
    return f"INSERT INTO Seasons VALUES({year}, {gp}, {w}, {l}, {otl}, {sol}, {pts}, {mp})"

def forwards(name, gp, g, a, pts, plusminus):
    return f"INSERT INTO Forwards VALUES({name}, {gp}, {g}, {a}, {pts}, {plusminus})"

def defensemen(name, gp, g, a, pts, plusminus):
    return f"INSERT INTO Defensemen VALUES({name}, {gp}, {g}, {a}, {pts}, {plusminus})"

def players(starting_season, ending_season, name):
    return f"INSERT INTO Players VALUES({starting_season}, {ending_season}, {name})"

def goalies(name, gp, w, l, gaa, sv):
    return f"INSERT INTO Goalies VALUES({name}, {gp}, {w}, {l}, {gaa}, {sv})"