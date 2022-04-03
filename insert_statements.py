def seasons(year, gp, w, l, otl, sol, pts, mp):
    return f"INSERT INTO Seasons VALUES({year}, {gp}, {w}, {l}, {otl}, {sol}, {pts}, {mp})"

def forwards(name, gp, g, a, pts, plusminus):
    return f"INSERT INTO Forwards VALUES({name}, {gp}, {g}, {a}, {pts}, {plusminus})"
