import commands2
from magicbot import MagicRobot

class MagicCommandRobot(MagicRobot):
    import commands2


    def robotPeriodic(self):
        commands2.CommandScheduler.getInstance().run()
        return super().robotPeriodic()

    def scheduleCommand(self, command: commands2.Command) -> None:
        """
        Schedule a command to run. This is a wrapper around
        :meth:`CommandScheduler.add` that allows you to
        schedule commands.

        :param command: The command to schedule
        """
        inst = commands2.CommandScheduler.getInstance()
        inst.schedule(command)

