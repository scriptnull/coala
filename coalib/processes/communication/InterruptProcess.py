import platform

if platform.system() == "Windows":
    from ctypes import windll
    from time import sleep
    CTRL_C_EVENT = 0x0
else:
    import os
    import signal


def interrupt_process(pid):
    """
    Interrupt a process by its pid.

    Note for Windows users:
    Be sure that the pid you pass shares the same process group as your program
    that calls this function. If they don't share the same process group, this
    call blocks for 10 seconds to be sure that this is the case.
    Also be aware to catch the KeyboardInterrupt in the main thread correctly
    since it is sent first to the parent thread and propagate it down to your
    call.

    :param pid: The pid of the process to interrupt.
    """
    if platform.system() == "Windows":  # pragma: no cover
        try:
            windll.kernel32.GenerateConsoleCtrlEvent(CTRL_C_EVENT, pid)
            sleep(10)
        except KeyboardInterrupt:
            pass
    else:
        os.kill(pid, signal.SIGINT)
