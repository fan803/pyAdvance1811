# class NPC(AI):
#     pass

def renameattribute(classname, parentclass, attributedic):
    newattribute = {}
    for key, value in attributedic.items():
        if not key.startswith("__"):
            key = classname.lower() + key
    newattribute[key] = value
    for key, value in newattribute.items():
        print(key, value)
    return type(classname, parentclass, newattribute)
class AI(object, metaclass=renameattribute):
    isalive = False
ai = AI()
print(hasattr(ai, "isalive")) #false
print(hasattr(ai, "aiisalive")) #true
