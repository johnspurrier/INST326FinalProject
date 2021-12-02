class Team: 
    def __init__(self, name, role): 
        self.name = name
        self.role = role
        
    
members = [
    ("Pierre", "professor"),
    ("Regina", "TA"),
    ("Shannon", "athletic director"),
    ("Rufus", "coach")
    ("Janelle", "teacher")
    ("Corey", "research assistant")
    ("Garth", "advisor")
    ("Maggie", "president")
    ]
team1 = Team(members)
    
def get_name(role):
    for x in members:
       if x[1] == role:
           return x[0] 
    else: 
        return None

def get_names(): 
    names = {}
    for x in members:
        names.add(x[0])
    return names 
        
def get_role(name): 
    for y in members:
        if y[0] == name:
            return y[1] 
    else:
        return None
        
def get_roles(): 
    roles = {}
    for y in members:
        roles.add(y[1])
    return roles 
    
def subteam(name, role):
    return 