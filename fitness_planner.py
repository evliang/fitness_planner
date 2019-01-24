import os
import yaml
import json
from datetime import date
import calendar
import random
from numpy.random import choice

def load_config(config):
    with open(config + '.yaml', 'r') as f:
        conf = yaml.load(f)
    return conf

def interact_with_user(exercise):
    """
    Displays current exercise w/ prev # of reps, then #
    """
    print(exercise)
    # for s in range(3): # hardcoding 3 sets & ignoring warmups for now
    #     input("Set " + str(s+1) + " number of reps: ")
    None

def shuffle(exercises, count):
    """Apply modifiers and then randomly shuffles list"""
    def build_weights(exercises):
        weights = list(map(lambda x: 0.0 if x.startswith('*') else (1.0 if x.startswith('^') else 0.5), exercises))
        sum_weights = sum(weights)
        weights = list(map(lambda x: x/sum_weights, weights))
        return weights

    top_priority = [x for x in exercises if x.startswith('*')]
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
                interact_with_user(muscle_group_exercises[i])
                #countdown()

    else:
        print("IT'S YOUR REST DAY!!!")
        # TODO check if value is actually a day of the week, or validate config?

if __name__ == '__main__':
    main()