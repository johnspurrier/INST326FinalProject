from cmdlineargs import main as cla_main

MEMBERS = [
    ("John", 32, "average person", False),
    ("Mary", 27, "fairly important person", False), 
    ("Pat", 41, "super important person", True)
           ]
def main():
    for member in MEMBERS:
        cla_main = (member)
        
if __name__ =="__main__":
    main()