import os
import sys
import yaml
import json
import time
from datetime import date, datetime
import calendar
import random
from numpy.random import choice

def load_config(config):
    with open(config + '.yaml', 'r') as f:
        conf = yaml.load(f)
    return conf

def load_exercise_history():
    try:
        with open('data.json', 'r') as fp:
            data = json.load(fp)
        return data
    except IOError:
        return dict()

def add_exercise_dictionary(dic, exercise, weight, reps):
    # {"bench press": {today: [{weight: 150, reps: 6}, {weight: 150, reps: 6}, {weight: 150, reps: 6}]}}
    today = str(date.today())
    if dic.get(exercise):
        if dic[exercise].get(today):
            dic[exercise][today] = dic[exercise][today] + [{ 'weight': weight, 'reps': reps}]
        else:
            dic[exercise][today] = [{ 'weight': weight, 'reps': reps}]
    else:
        dic[exercise] = { today: [{ 'weight': weight, 'reps': reps}]}
    return dic

def save_exercise_history(data):
    with open('data.json', 'w') as fp:
        json.dump(data, fp)

def extract_int(s):
    return [int(x) for x in s.split() if x.isdigit()][0]

def convert_weight_string(s):
    """translates input to weight.
    "bar + 65" => 175 (lbs)
    not robust"""
    if "bar" in s:
        plate_weight = extract_int(s.split("bar")[1].split("+")[1]) # prettify
        return 45 + plate_weight * 2
    else:
        return extract_int(s)

def interact_with_user(exercise, num_sets, warmup=False):
    """Displays the current exercise and tracks number of reps performed"""
    exercise = random.choice([x.title().strip() for x in exercise.lstrip('*').lstrip('^').lstrip('=').split('OR')])
    exercise_history = load_exercise_history()

    prev_numbers = []
    if exercise_history.get(exercise):
        last_time = list(exercise_history[exercise].keys())[-1]
        #last_time_dow = calendar.day_name[datetime.strptime('2014-12-04', '%Y-%m-%d').date().weekday()]
        prev_numbers = exercise_history[exercise][last_time]

    print(f"===== {exercise} =====")
    
    if warmup:
        if not prev_numbers:
            inp = input("What's your best guess of your 4-6RM for {}?".format(exercise))
            weight = convert_weight_string(inp)
        else:
            weight = convert_weight_string(prev_numbers[0]["weight"])
        print("       ( warm up ) ")
        z = input(f"12 reps of {int(weight/2)}. Any key to continue...")
        countdown_for_rest(1)
        z = input(f"10 reps of {int(weight/2)}. Any key to continue...")
        countdown_for_rest(1)
        z = input(f"6 reps of {int(weight*0.7)}. Any key to continue...")
        countdown_for_rest(1)
        z = input(f"12 reps of {int(weight*0.9)}. Any key to continue...")
        countdown_for_rest(2)

    if exercise_history.get(exercise):
        prev_num_str = [x['weight'] + 'x' + x['reps'] for x in prev_numbers]
        print(" ----- {} -----\r\n{}: {}".format(exercise, last_time, ', '.join(prev_num_str)))

    for s in range(num_sets): # TODO: handle warmups
        while True:
            inp = input("Set " + str(s+1) + "! Enter weight, reps: ")
            weight = inp.split(',', 1)[0]
            reps = inp.split(',',1)[1].strip().replace('.','',1)
            if reps.strip().replace('.','',1).isdigit():
                break
            else:
                print("Invalid input.")
        exercise_history = add_exercise_dictionary(exercise_history, exercise, weight, reps)
        save_exercise_history(exercise_history)
        countdown_for_rest(2)
    None

def countdown_for_rest(min):
    def display_time(s):
        display_min = lambda m: str(m) + " min" if m > 0 else ""
        display_sec = lambda s: str(s) + " sec" if s > 0 else ""
        sys.stdout.write("Rest for {} {}      ".format(display_min(s//60),display_sec(s%60)))
    for remaining in range(int(min*60), 0, -1):
        sys.stdout.write("\r")
        display_time(remaining)
        sys.stdout.flush()
        time.sleep(1)
    sys.stdout.write("\r")

def shuffle(exercises, count):
    """Apply modifiers and then randomly shuffles list"""
    def build_weights(exercises):
        weights = list(map(lambda x: 0.0 if x.startswith('*') else (1.0 if x.startswith('^') else 0.5), exercises))
        sum_weights = sum(weights)
        weights = list(map(lambda x: x/sum_weights, weights))
        return weights

    top_priority = [x for x in exercises if x.startswith('**')]
    weights = build_weights(exercises)
    # random.choices can result in duplicates
    the_rest = []
    for _ in range(count - len(top_priority)):
        chosen = random.choices(exercises, weights=weights, k=1)[0]
        while chosen in the_rest:
            chosen = random.choices(exercises, weights=weights, k=1)[0]
        the_rest.append(chosen)

    # ensuring = is last exercise performed
    return top_priority + [x for x in the_rest if not x.startswith('=')] + [x for x in the_rest if x.startswith('=')]

def main():
    exercises = load_config("exercises")
    routine = load_config("routine")

    current_day = calendar.day_name[date.today().weekday()]
    todays_routine = routine.get(current_day, None)

    if todays_routine:
        for muscle_group in todays_routine:
            exercise_set_count = todays_routine[muscle_group]
            muscle_group_exercises = shuffle(exercises[muscle_group], exercise_set_count)
            for i in range(exercise_set_count):
                interact_with_user(muscle_group_exercises[i], 3, i==0) # hardcoding num_sets for now

    else:
        print("IT'S YOUR REST DAY!!!")
        # TODO check if value is actually a day of the week, or validate config?

if __name__ == '__main__':
    main()