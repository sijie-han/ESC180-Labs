def initialize():
    '''Initializes the global variables needed for the simulation.
    Note: this function is incomplete, and you may want to modify it'''

    global cur_hedons, cur_health

    global cur_time
    global last_activity, last_activity_duration

    global last_finished
    global bored_with_stars
    global cur_star, cur_star_activity
    cur_hedons = 0
    cur_health = 0

    cur_star = None
    cur_star_activity = None

    bored_with_stars = False

    last_activity = None
    last_activity_duration = 0

    cur_time = 0

    last_finished = -1000




def star_can_be_taken(activity):
    if cur_star_activity == activity and not bored_with_stars:
        return True
    return False



def perform_activity(activity, duration):
    global cur_health, last_activity, last_activity_duration,cur_time,cur_hedons,last_finished
    # Player is not tired and is taking the star
    if last_activity== "rest" and last_activity_duration >=120 and star_can_be_taken(activity):
        if activity == "running":
            if duration <= 10:
                cur_health += duration*3
                cur_hedons += duration*5
            elif duration<=180:
                cur_health += duration*3
                cur_hedons = 50+ cur_hedons-2*(duration-10)
            else:
                cur_health += 540+ duration-180
                cur_hedons = 20+ cur_hedons-2*(duration-10)
        elif activity == "textbooks":
            cur_health += 2*duration
            if duration<=10:
                cur_hedons += 4*duration
            elif duration<=20:
                cur_hedons = cur_hedons+40+ duration-10
            else:
                cur_hedons = cur_hedons = cur_hedons+50-(duration-20)
        elif activity == "resting":
            pass
    # Player is not tired and is not taking the star
    elif last_activity== "rest" and last_activity_duration >=120 and not star_can_be_taken(activity):
        if activity == "running" :
            if duration<=180:
                cur_health += duration*3
            else:
                cur_health += 540+ duration-180
            cur_hedons -= 2*duration
        elif activity == "textbooks":
            cur_health += 2*duration
            cur_hedons -= 2*duration
        elif activity == "resting":
            pass
    # Player is tired and taking the star
    elif star_can_be_taken(activity):
        if activity == "running":
            if duration <= 10:
                cur_health += duration*3
                cur_hedons += duration*1
            elif duration<=180:
                cur_health += duration*3
                cur_hedons = 10 - 2*(duration-10)
            else:
                cur_health += 540+ duration-180
                cur_hedons = 10 - 2*(duration-10)
        elif activity == "textbooks":
            cur_health += 2*duration
            if duration<=10:
                cur_hedons += 1*duration
            elif duration<=20:
                cur_hedons = 10 - 2*(duration-10)
            else:
                cur_hedons = 10 - 2*(duration-10)
    else:
        if activity == "running":
            if duration <= 10:
                cur_health += duration*3
                cur_hedons += duration*2
            elif duration<=180:
                cur_health += duration*3
                cur_hedons = 20+ cur_hedons-2*(duration-10)
            else:
                cur_health += 540+ duration-180
                cur_hedons = 20+ cur_hedons-2*(duration-10)
        elif activity == "textbooks":
            cur_health += 2*duration
            if duration<=20:
                cur_hedons += duration
            else:
                cur_hedons = cur_hedons+20-(duration-20)
        elif activity == "resting":
            pass
    last_finished = cur_time
    cur_time += duration
    last_activity = activity
    last_activity_duration = duration



def get_cur_hedons():
    global cur_hedons
    return cur_hedons

def get_cur_health():
    global cur_health
    return cur_health

def offer_star(activity):
    global cur_star_activity,cur_star
    if activity == "running":
        cur_star_activity = "running"
    elif activity == "resting":
        cur_star_activity = "resting"
    elif activity == "textbooks":
        cur_star_activity = "textbooks"
    cur_star_pre = cur_star
    cur_star = cur_time
    cur_star = True


def most_fun_activity_minute():
    pass

################################################################################
#These functions are not required, but we recommend that you use them anyway
#as helper functions

def get_effective_minutes_left_hedons(activity):
    '''Return the number of minutes during which the user will get the full
    amount of hedons for activity activity'''
    pass

def get_effective_minutes_left_health(activity):
    pass

def estimate_hedons_delta(activity, duration):
    '''Return the amount of hedons the user would get for performing activity
    activity for duration minutes'''
    pass


def estimate_health_delta(activity, duration):
    pass

################################################################################

if __name__ == '__main__':
    initialize()
    perform_activity("running", 30)
    print(get_cur_hedons())            # -20 = 10 * 2 + 20 * (-2)             # Test 1
    print(get_cur_health())            # 90 = 30 * 3                          # Test 2
    print(most_fun_activity_minute())  # resting                              # Test 3
    perform_activity("resting", 30)
    offer_star("running")
    print(most_fun_activity_minute())  # running                              # Test 4
    perform_activity("textbooks", 30)
    print(get_cur_health())            # 150 = 90 + 30*2                      # Test 5
    print(get_cur_hedons())            # -80 = -20 + 30 * (-2)                # Test 6
    offer_star("running")
    perform_activity("running", 20)
    print(get_cur_health())            # 210 = 150 + 20 * 3                   # Test 7
    print(get_cur_hedons())            # -90 = -80 + 10 * (3-2) + 10 * (-2)   # Test 8
    perform_activity("running", 170)
    print(get_cur_health())            # 700 = 210 + 160 * 3 + 10 * 1         # Test 9
    print(get_cur_hedons())            # -430 = -90 + 170 * (-2)              # Test 10