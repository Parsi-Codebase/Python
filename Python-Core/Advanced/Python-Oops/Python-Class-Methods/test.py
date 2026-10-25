class Test:
    @classmethod
    def hello(cls):
        print("Hello from class method!")

Test.hello()   # called using class
obj = Test()
obj.hello()    # called using object (also works)
