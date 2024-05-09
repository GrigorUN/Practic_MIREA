class MealyError(Exception):
    pass


class StateMachine:
    def __init__(self):
        self.state = "A"

    def unite(self):
        if self.state == "A":
            self.state = "B"
            return 0
        if self.state == "B":
            self.state = "C"
            return 1
        if self.state == "C":
            self.state = "D"
            return 3
        if self.state == "D":
            self.state = "F"
            return 5
        if self.state == "E":
            self.state = "F"
            return 6
        if self.state == "F":
            self.state = "G"
            return 7
        if self.state == "H":
            self.state = "F"
            return 11
        if self.state == "G":
            self.state = "A"
            return 9

        raise MealyError("unite")

    def exit(self):
        if self.state == "B":
            self.state = "F"
            return 2
        if self.state == "D":
            self.state = "E"
            return 4
        if self.state == "H":
            self.state = "A"
            return 10
        if self.state == "G":
            self.state = "H"
            return 8
        raise MealyError("exit")


def main():
    return StateMachine()


def raises(function, error):
    output = None
    try:
        output = function()
    except Exception as e:
        assert type(e) == error
    assert output is None


def test():
    o = main()
    assert o.unite() == 0
    assert o.exit() == 2
    assert o.unite() == 7
    assert o.exit() == 8
    assert o.unite() == 11
    o = main()
    assert o.unite() == 0
    assert o.exit() == 2
    assert o.unite() == 7
    assert o.exit() == 8
    assert o.exit() == 10
    o = main()
    assert o.unite() == 0
    assert o.exit() == 2
    assert o.unite() == 7
    assert o.unite() == 9
    o = main()
    assert o.unite() == 0
    assert o.unite() == 1
    assert o.unite() == 3
    assert o.exit() == 4
    assert o.unite() == 6
    assert o.unite() == 7
    assert o.exit() == 8
    assert o.unite() == 11
    o = main()
    assert o.unite() == 0
    assert o.unite() == 1
    assert o.unite() == 3
    assert o.exit() == 4
    assert o.unite() == 6
    assert o.unite() == 7
    assert o.exit() == 8
    assert o.exit() == 10
    o = main()
    assert o.unite() == 0
    assert o.unite() == 1
    assert o.unite() == 3
    assert o.exit() == 4
    assert o.unite() == 6
    assert o.unite() == 7
    assert o.unite() == 9
    o = main()
    assert o.unite() == 0
    assert o.unite() == 1
    assert o.unite() == 3
    assert o.unite() == 5
    assert o.unite() == 7
    assert o.exit() == 8
    assert o.unite() == 11
    o = main()
    assert o.unite() == 0
    assert o.unite() == 1
    assert o.unite() == 3
    assert o.unite() == 5
    assert o.unite() == 7
    assert o.exit() == 8
    assert o.exit() == 10
    o = main()
    assert o.unite() == 0
    assert o.unite() == 1
    assert o.unite() == 3
    assert o.unite() == 5
    assert o.unite() == 7
    assert o.unite() == 9

    o.state = "R"
    raises(lambda: o.unite(), MealyError)
    raises(lambda: o.exit(), MealyError)
