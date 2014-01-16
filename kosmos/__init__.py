__version__ = '0.6'

########################################################################################################################
# Settings
########################################################################################################################
import os

app_store_path = os.path.expanduser('~/.kosmos')
if not os.path.exists(app_store_path):
    os.mkdir(app_store_path)

settings = dict(
    library_path=os.path.dirname(__file__),
    app_store_path=app_store_path
)

########################################################################################################################
# Misc
########################################################################################################################
from collections import namedtuple

########################################################################################################################
# Signals
########################################################################################################################
import blinker

signal_task_status_change = blinker.Signal()
signal_stage_status_change = blinker.Signal()


########################################################################################################################
# Enums
########################################################################################################################
import enum


class TaskStatus(enum.Enum):
    no_attempt = 'Has not been attempted',
    waiting = 'Waiting to execute',
    submitted = 'Submitted to the job manager',
    successful = 'Finished successfully',
    failed = 'Finished, but failed'
    killed = 'Manually Killed'


class StageStatus(enum.Enum):
    no_attempt = 'Has not been attempted',
    running = 'Submitted to the job manager',
    finished = 'All Tasks have finished'
    killed = 'Manually Killed'

########################################################################################################################
# Imports
########################################################################################################################

from .models import rel
from .models.Recipe import Recipe
from .models.TaskFile import TaskFile
from .models.Task import Task, INPUT
from .models import rel
from .models.Stage import Stage
from .models.Execution import Execution
from .util.args import add_execution_args, parse_and_start, default_argparser
from .db import get_session


__all__ = ['rel', 'Recipe', 'TaskFile', 'Task', 'INPUT', 'rel', 'Stage', 'Execution', 'TaskStatus', 'StageStatus']