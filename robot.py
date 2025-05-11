import wpilib
import commands2
from base.magiccommandbot import MagicCommandRobot


# Component example (for magicbot)
class ExampleComponent:
    def execute(self) -> None:
        # print('Magic component executing')
        ...


# Command2 subsystem example
class ExampleSubsystem(commands2.SubsystemBase):
    def __init__(self) -> None:
        # Initialize hardware
        self.setDefaultCommand(ExampleCommand(self))
        ...

    def periodic(self) -> None:
        # print('Command2 subsystem periodic running')
        ...


class ExampleCommand(commands2.Command):

    def __init__(self, subsystem: ExampleSubsystem) -> None:
        super().__init__()
        self.addRequirements(subsystem)
        ...

    def initialize(self) -> None:
        print('Default command initialized')
        ...

    def execute(self) -> None:
        print('Default command executing')
        ...

    def end(self, interrupted: bool) -> None:
        print('Default command ended')
        ...

    def isFinished(self) -> bool:
        return False


class MyRobot(MagicCommandRobot):
    # Define components for magicbot
    example: ExampleComponent

    def createObjects(self) -> None:
        self.joystick = wpilib.Joystick(0)
        self.example_subsystem = ExampleSubsystem()

    def teleopInit(self) -> None:
        ...

    def teleopPeriodic(self) -> None:
        # Example of binding a button to a command
        if self.joystick.getRawButton(2):
            # This will halt the default command on our example subsystem
            # and run the command we are scheduling.
            self.scheduleCommand(
                commands2.InstantCommand(
                    lambda: print("Button 2 pressed!"), self.example_subsystem
                )
            )
