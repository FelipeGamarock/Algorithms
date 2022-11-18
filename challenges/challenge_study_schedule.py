def study_schedule(permanence_period, target_time):
    if target_time == None:
        return None

    students_on_target_time = 0
    try:
        for sign_in, sign_out in permanence_period:
            if type(sign_in) != int or type(sign_out) != int:
                return None
            if sign_in <= target_time <= sign_out:
                students_on_target_time += 1
    except TypeError:
        return None

    return students_on_target_time            
