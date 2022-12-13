
from actions.menu import cancel, menu
from data.action_contexts import ActionContext
from data.data_action import Commands, Inline_actions


ACTIONS = {
    Commands.cancel                 : cancel,
    Commands.start                  : menu
}