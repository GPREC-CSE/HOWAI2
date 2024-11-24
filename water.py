
229X1A0587 PAMISETTI MOUNIKA
11:10 AM (4 hours ago)
to me

from collections import defaultdict
def waterJugSolver(amt1, amt2, jug1, jug2, aim, visited):
    if (amt1 == aim and amt2 == 0) or (amt2 == aim and amt1 == 0):
        print(amt1, amt2)
        return True
    if not visited[(amt1, amt2)]:
        print(amt1, amt2)
        visited[(amt1, amt2)] = True
        return (waterJugSolver(0, amt2, jug1, jug2, aim, visited) or
                waterJugSolver(amt1, 0, jug1, jug2, aim, visited) or
                waterJugSolver(jug1, amt2, jug1, jug2, aim, visited) or
                waterJugSolver(amt1, jug2, jug1, jug2, aim, visited) or
                waterJugSolver(amt1 + min(amt2, (jug1 - amt1)),
                              amt2 - min(amt2, (jug1 - amt1)), jug1, jug2, aim, visited) or
                waterJugSolver(amt1 - min(amt1, (jug2 - amt2)),
                              amt2 + min(amt1, (jug2 - amt2)), jug1, jug2, aim, visited))
   
    else:
        return False
jug1 = int(input("Enter the capacity of the first jug: "))
jug2 = int(input("Enter the capacity of the second jug: "))
aim = int(input("Enter the amount of water to be measured: "))
visited = defaultdict(lambda: False)
print("Steps: ")
waterJugSolver(0, 0, jug1, jug2, aim, visited)