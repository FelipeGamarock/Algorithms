def study_schedule(permanence_period, target_time):
    students_on_target_time = 0

    for sign_in, sign_out in permanence_period:
        if (
            type(sign_in) is not int
            or type(sign_out) is not int
            or type(target_time) is not int
        ):
            return None
        if sign_in <= target_time <= sign_out:
            students_on_target_time += 1

    return students_on_target_time
