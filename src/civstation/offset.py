from .stations import Station

#TODO: Debug this code. I ahd to eat dinner and didn't get a chance.
class Offset:
    def __init__ (self, offset):
            if isinstance(offset, Offset):
                self.val=float(offset)
            elif "rt" in offset.lower() or "lt" in offset.lower():
                negative=False
                if "rt" in str(offset).lower()[-2:]:
                    if "'" in str(offset):
                        endnum=str(offset).index("'")
                    else: endnum=str(offset).lower().index("r")
                if "lt" in str(offset).lower()[-2:]:
                    negative=True
                    if "'" in str(offset):
                        endnum=str(offset).index("'")
                    else: endnum=str(offset).lower().index("l")                
                try:
                    self.val=float(str(offset)[:endnum])
                except: raise ValueError("Not a valid Offset")
                if negative: self.val=-self.val
            else:
                try: self.val = float(offset)
                except: raise ValueError("Not a valid offset.")
            
class Point:
    def __init__ (self,station,offset):
        self.station= Station(station)
        self.offset=offset
        #TODO add a parser to parse offsets such as "34.70RT" and "12.50'LT"
        #maybe add an Offset object. 