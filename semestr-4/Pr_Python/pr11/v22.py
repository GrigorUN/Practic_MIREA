class MealyError(Exception):
    pass


class StateMachine:
    def __init__(self):
        self.state = "A"

    def stare(self):
        if self.state == "A":
            self.state = "B"
            return 0
        if self.state == "B":
            self.state = "G"
            return 2
        if self.state == "E":
            self.state = "F"
            return 5
        if self.state == "F":
            self.state = "G"
            return 7
        raise MealyError("stare")

    def reset(self):
        if self.state == "B":
            self.state = "C"
            return 1
        if self.state == "C":
            self.state = "D"
            return 3
        if self.state == "D":
            self.state = "E"
            return 4
        if self.state == "F":
            self.state = "D"
            return 8
        raise MealyError("reset")

    def coast(self):
        if self.state == "G":
            self.state = "D"
            return 9
        if self.state == "E":
            return 6
        raise MealyError("coast")


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
    assert o.stare() == 0
    assert o.reset() == 1
    assert o.reset() == 3
    assert o.reset() == 4
    assert o.coast() == 6
    assert o.stare() == 5
    assert o.reset() == 8
    o = main()
    assert o.stare() == 0
    assert o.reset() == 1
    assert o.reset() == 3
    assert o.reset() == 4
    assert o.coast() == 6
    o = main()
    assert o.stare() == 0
    assert o.reset() == 1
    assert o.reset() == 3
    assert o.reset() == 4
    assert o.coast() == 6
    assert o.stare() == 5
    assert o.stare() == 7
    assert o.coast() == 9
    o = main()
    assert o.stare() == 0
    assert o.stare() == 2
    assert o.coast() == 9

    raises(lambda: o.stare(), MealyError)
    raises(lambda: o.coast(), MealyError)
    o.state = "R"
    raises(lambda: o.reset(), MealyError)
