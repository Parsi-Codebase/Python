class Outer:
    def __init__(self):
        self.outer_name = "Outer Class"

    def show_outer(self):
        print("This is the Outer class method")

    # Inner class defined inside
    class Inner:
        def __init__(self):
            self.inner_name = "Inner Class"

        def show_inner(self):
            print("This is the Inner class method")
# Access inner class through outer
outer_obj = Outer()
inner_obj = Outer.Inner()

outer_obj.show_outer()
inner_obj.show_inner()