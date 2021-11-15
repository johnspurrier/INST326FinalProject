POSITIONS = {
    "A" :  0,
    "A#":  1,
    "Bb":  1,
    "B" :  2,
    "C" :  3,
    "C#":  4,
    "Db":  4,
    "D" :  5,
    "D#":  6,
    "Eb":  6,
    "E" :  7,
    "F" :  8,
    "F#":  9,
    "Gb":  9,
    "G" : 10,
    "G#": 11,
    "Ab": 11
}

PITCHES = {
    0:  ["A"],
    1:  ["A#", "Bb"],
    2:  ["B"],
    3:  ["C"],
    4:  ["C#", "Db"],
    5:  ["D"],
    6:  ["D#", "Eb"],
    7:  ["E"],
    8:  ["F"],
    9:  ["F#", "Gb"],
    10: ["G"],
    11: ["G#", "Ab"]
}


class Note:
    """Defines the Note class
    
    Attributes: 
        position(int): represents the position of the pitch on the chromatic scale
        perspective(str): has one of three values: "#", "b", or None
        other(str): another note object
    
    """
    def __init__(self,position,perspective = None):
        if type(position) == int:
                self.position = position
                self.perspective = perspective
        else:
            if len(position) == 2:
                self.position = POSITIONS.get(position)
                self.perspective = position[1]
            else:
                self.position = POSITIONS.get(position)
                self.perspective = perspective
                        
    def __invert__(self):
        if self.perspective == '#':
            return Note(self.position,'b')
        elif self.perspective == 'b':
            return Note(self.position,'#')
        else:
            return Note(self.position,self.perspective)
            
    def __add__(self,num):
        new_position = self.position + num
        if new_position > 11:
            new_position-=12
            
        return Note(new_position,self.perspective)
        
    def __sub__(self,num):
        new_position = self.position - num
        if new_position < 0:
            new_position+=12
            
        return Note(new_position,self.perspective)     
        
        
    def __rshift__(self,other):
        if self.position >= other.position:
            shift = self.position - other.position
            return shift
        else:
            new_note = self.position + 12
            shift = new_note - other.position
            return shift
        
    def __lshift__(self,other):
        if other.position >= self.position:
            shift = other.position - self.position
            return shift
        else:
            new_note = other.position + 12
            shift = new_note - self.position   
            return shift   
    
    def __repr__(self):
        return f'Note({self.position}, {self.perspective})'
    
    def __str__(self):
        picthes_list = PITCHES.get(self.position)
        if len(picthes_list) == 1:
            return picthes_list[0]
        else:
            if self.perspective == '#':
                return picthes_list[0]
            elif self.perspective == 'b':
                return picthes_list[1]
            else:
                return f'{picthes_list[0]}/{picthes_list[1]}'
