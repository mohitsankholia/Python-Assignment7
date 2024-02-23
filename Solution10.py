class Business:
    pass


def getClassName(instance):
    return instance.__class__.__name__


obj = Business()
class_name = getClassName(obj)
print("Class name :", class_name)
