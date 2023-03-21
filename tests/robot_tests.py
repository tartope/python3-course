import unittest
from robot import Robot


class RobotTests(unittest.TestCase):
    # setUp re-runs before each test method; creates an instance of a class
    def setUp(self):
        # charge is set to 50
        self.mega_man = Robot("Mega Man", battery=50)

    # tests that charge is now set to 100
    def test_charge(self):
        # call mega_man.charge() to update battery charge to 100
        self.mega_man.charge()
        # test if battery is now set to 100
        self.assertEqual(self.mega_man.battery, 100)

    # tests say_name method
    def test_say_name_good_battery(self):
        # call mega_man.say_name() and see if it's equal to the return statement
        self.assertEqual(
            self.mega_man.say_name(),
            "BEEP BOOP BEEP BOOP.  I AM MEGA MAN"
        )
        # also check if battery has been decremented by 1
        self.assertEqual(self.mega_man.battery, 49)

    def test_say_name_bad_battery(self):
        self.mega_man = Robot("Mega Man", battery=-1)
        self.assertEqual(
            self.mega_man.say_name(),
            "Low power.  Please charge and try again"
        )

    def test_learn_skill_yes(self):
        self.assertEqual(
            self.mega_man.learn_skill("cooking", 25),
            "WOAH. I KNOW COOKING"
        )
        self.assertEqual(self.mega_man.battery, 25),
        self.assertEqual(self.mega_man.skills, ["cooking"])

    def test_learn_skill_no(self):
        self.assertEqual(
            self.mega_man.learn_skill("driving", 51),
            "Insufficient battery. Please charge and try again"
        )


if __name__ == "__main__":
    unittest.main()
