'''
Completed by Andrew Wu and Andre Rodrigues on Oct 15, 2021
'''
def initialize(): #done
    global cur_hedons, cur_health, last_activity_duration, resting_duration
    cur_hedons, cur_health, last_activity_duration, resting_duration = 0, 0, 0, 0

    global last_activity, star_activity
    star_activity = ""
    last_activity = "" 

    global bored_with_stars, tired, has_run_text
    bored_with_stars, tired, has_run_text = False, False, False

    global cur_time, running_star_offered, textbooks_star_offered, star_taken, star_time 
    cur_time = [0,0,0]
    running_star_offered = [False, False, False]
    textbooks_star_offered = [False, False, False]
    star_taken = [False, False, False]
    star_time = [0,0,0]
    
def max_time_difference(a,b,c): #done
    diff = abs(a-b)

    if (abs(b-c) > diff):
        diff = abs(b-c)
    if (abs(a-c) > diff):
        diff = abs(a-c)

    return diff

def is_bored(): #done
    global bored_with_stars
    number_of_stars_offered = 0
    
    if (not bored_with_stars):
        for i in range(len(running_star_offered)):
            number_of_stars_offered += running_star_offered[i] 
    
        for i in range(len(textbooks_star_offered)):
            number_of_stars_offered += textbooks_star_offered[i]

        if (number_of_stars_offered > 2):
            if (max_time_difference(star_time[-1],star_time[-2],star_time[-3]) < 120):
                bored_with_stars = True

def is_tired(): #done
    global tired

    if (len(cur_time) > 3):
        if (last_activity is not "resting"):
            tired = True
        elif (resting_duration < 120 and has_run_text):
            tired = True
        else:
            tired = False
            
def star_can_be_taken(activity): #done
    if (activity is "running"):
        if (running_star_offered[-1] and not bored_with_stars and (cur_time[-1] == star_time[-1])):
            return True
    elif (activity is "textbooks"):
        if (textbooks_star_offered[-1] and not bored_with_stars and (cur_time[-1] == star_time[-1])):
            return True
    else:
        return False
    
def perform_activity(activity, duration_activity): #done
    global cur_health, cur_hedons, cur_time, tired, last_activity, last_activity_duration, resting_duration, has_run_text
    flag = False
    duration = duration_activity

    is_tired()
    
    if (activity is "running" or activity is "textbooks" or activity is "resting"):
        flag = True
        if (activity is not "resting"):
            has_run_text = True

    if (flag):
        if (activity is "resting"):
            cur_hedons += 0
        elif ((activity is "running") and tired):
            cur_hedons -= 2 * duration
        elif ((activity is "textbooks") and tired):
            cur_hedons -= 2 * duration
        
        if (not tired):
            if (activity is "running"):
                if (duration > 10):
                    cur_hedons += 2 * 10 - 2 * (duration - 10)
                else:
                    cur_hedons += 2 * duration
            if (activity is "textbooks"):
                if (duration > 20):
                    cur_hedons += 1 * 20 - 1 * (duration - 20)
                else:
                    cur_hedons += 1 * duration

        if ((activity is "running") and running_star_offered[-1] and not bored_with_stars):
            if (cur_time[-1] is star_time[-1]):
                if (duration > 10):
                    cur_hedons += 3 * 10
                else:
                    cur_hedons += 3 * duration
        elif ((activity is "textbooks") and textbooks_star_offered[-1] and not bored_with_stars):
            if (cur_time[-1] is star_time[-1]):
                if (duration > 10):
                    cur_hedons += 3 * 10
                else:
                    cur_hedons += 3 * duration

        if (activity is "running"):
            if (last_activity is "running"):
                if ((duration + last_activity_duration) > 180 and last_activity_duration <= 180):
                    cur_health += 3 * (180 - last_activity_duration) + (duration + last_activity_duration) - 180
                elif (last_activity_duration > 180):
                    cur_health += duration
                else:
                    duration
                    if (duration > 180):
                        cur_health += 2 * 180 + duration
                    else:
                        cur_health += 3 * duration
                duration += last_activity_duration
            elif (duration > 180):
                cur_health += 2 * 180 + duration
            else:
                cur_health += 3 * duration

        if (activity is "textbooks"):
            cur_health += 2 * duration
        
        if (activity is "resting"):
            resting_duration += duration_activity
        else:
            resting_duration = 0

        last_activity = activity
        last_activity_duration = duration 
        cur_time.append(cur_time[-1] + duration_activity) 
        running_star_offered.append(False)
        textbooks_star_offered.append(False)

def get_cur_hedons(): #done
    return cur_hedons
    
def get_cur_health(): #done
    return cur_health
    
def offer_star(activity): #done
    if (activity is "running"):
        running_star_offered.append(True)
        textbooks_star_offered.append(False)
    elif (activity is "textbooks"):
        textbooks_star_offered.append(True)
        running_star_offered.append(False)
    star_time.append(cur_time[-1])

    is_bored()

    if (bored_with_stars):
        running_star_offered.append(False)
        textbooks_star_offered.append(False)
        
def most_fun_activity_minute(): #done
    running_hedons, textbook_hedons = 0,0

    is_tired()

    if (tired):
        if (not running_star_offered[-1]):
            running_hedons -= 2 * 1
        if (not textbooks_star_offered[-1]):
            textbook_hedons -= 2 * 1
    else:
        running_hedons += 2
        textbook_hedons += 1

        if (not bored_with_stars):
            if (running_star_offered[-1] and cur_time[-1] is star_time[-1]): #if a star was taken for running
                running_hedons += 3
            elif (textbooks_star_offered[-1] and cur_time[-1] is star_time[-1]): #if a star was taken for textbooks
                textbook_hedons += 3

    if (textbook_hedons < 0 and running_hedons < 0):
        return "resting"
    elif (textbook_hedons > running_hedons): 
        return "textbooks"
    else:
        return "running"
        
if __name__ == '__main__':
    initialize()