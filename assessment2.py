class Team: 
    """A class for all of the names and roles of members of the team
    
    Attributes: 
        members(list of str): a list of tuples containing the names and roles
        of all of the members of the team
    """
    
    def __init__(self, members): 
        self.members = members          

    def get_name(self, role):
        for x in self.members:
            if x[1] == role:
                return x[0] 
            else: 
                return None

    def get_names(self): 
        names = {}
        for x in self.members:
            names.add(x[0])
        return names 
        
    def get_role(self, name): 
        for y in self.members:
            if y[0] == name:
                return y[1] 
        else:
            return None
        
    def get_roles(self): 
        roles = {}
        for y in self.members:
            roles.add(y[1])
        return roles 
    
    def subteam(name, role):
        new_team = []
        new_team.append(name, role)
        return new_team

members = [
    ("Pierre", "professor"),
    ("Regina", "TA"),
    ("Shannon", "athletic director"),
    ("Rufus", "coach"),
    ("Janelle", "teacher"),
    ("Corey", "research assistant"),
    ("Garth", "advisor"),
    ("Maggie", "president")
]
team1 = Team(members)   