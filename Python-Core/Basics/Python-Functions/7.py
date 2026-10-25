#Combining *args and **kwargs
def demo(*args, **kwargs):

    print("Arguments:", args)
    print("Keyword Arguments:", kwargs)


demo(10, 20, 30, name="Santhosh", course="Python")