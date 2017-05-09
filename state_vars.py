import logging
import string
import random
import datetime

state_vars_list = []


def verify_state_var(response_state_var):
    for state, time in state_vars_list:
        # logging.debug(state + ", " + time.strftime("%Y-%m-%d %H:%M:%S"))
        if state == response_state_var:
            return True
    return False


def state_generator(size=10, chars=string.ascii_uppercase + string.digits):

    # remove state variables older than 5 minutes
    state_vars_list[:] = [x for x in state_vars_list if younger_than_five_mins(x)]
    # logging.debug(state_vars_list)

    # generate new state variable
    code = ''.join(random.choice(chars) for _ in range(size))
    state_vars_list.append((code, datetime.datetime.now()))
    return code


def younger_than_five_mins(x):
    if (datetime.datetime.now() - x[1]).total_seconds() > 300:
        return False
    else:
        return True
