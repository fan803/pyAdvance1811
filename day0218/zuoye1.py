#实现功能：能够将所有属性更名为小写类名+小写属性名
#		  如果存在属性名以temp开头的则删除该属性

def mydesigclass(classname, prentclassname, attrdict ):
    #print(classname,prentclassname,attrdict)
    #print(classname.lower())
    newdict = {}

    for k,v in attrdict.items():
        if not k.startswith("__"):
            newdict[classname.lower()+k.lower()] = v
    #print(newdict)
    return  type(classname, (),newdict)
class ABC(metaclass=mydesigclass):
    Speed =10
    name = "sb"



print(hasattr(ABC,"Speed"))
print(hasattr(ABC,"abcspeed"))