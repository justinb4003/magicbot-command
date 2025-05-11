import commands2
from magicbot import MagicRobot

class MagicCommandRobot(MagicRobot):
    import commands2

    def robotInit(self) -> None:
        super().robotInit()

    def createSubsystems(self) -> None:
        raise NotImplementedError(
            "You must implement createSubsystems() in your robot class"
        )

    def robotPeriodic(self):
        commands2.CommandScheduler.getInstance().run()
        return super().robotPeriodic()

    def registerSubsystem(self, subsystem: commands2.SubsystemBase) -> None:
        """
        Register a subsystem with the command scheduler.

        :param subsystem: The subsystem to register
        """
        inst = commands2.CommandScheduler.getInstance()
        inst.registerSubsystem(subsystem)

    def scheduleCommand(self, command: commands2.Command) -> None:
        """
        Schedule a command to run. This is a wrapper around
        :meth:`CommandScheduler.add` that allows you to
        schedule commands.

        :param command: The command to schedule
        """
        inst = commands2.CommandScheduler.getInstance()
        inst.schedule(command)

