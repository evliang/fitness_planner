# Fitness_Planner
Fitness Planner generates an exercise plan and tracks your workout progress over time.

## Configuration

Fitness_planner requires one config file for a routine and another for a list of exercises.

For each day of the week in routine.yaml, there needs to be a mapping of the muscle group to number of sets
```
Sunday:
  chest: 3
  triceps: 2
Monday:
  back: 3
  biceps: 2
```

exercises.yaml lists exercises for each muscle group
```
chest:
- "*medium-grip barbell bench press OR wide-grip barbell bench press"
- "push ups"
- "low-incline dumbbell bench press"
- "dumbbell pullovers"
- "=dumbbell bench press hold"
- "=dumbbell flyes OR decline dumbbell flyes"
back:
- "*negative pull-ups"
- "^one-arm dumbbell row"
- "^deadlift"
- "dumbbell incline row"
- "reverse grip bent-over rows"
```

An optional modifier may appear in the beginning:
```
*  - an exercise that must be performed
** - the exercise must be done first (for that muscle group)
^  - preferred exercise (higher probability of being selected)
=  - last exercise (for that muscle group). Meant for isolation exercises
```

## How to Run:

```
pip install pyYaml numpy
git clone https://github.com/evliang/fitness_planner.git
cd fitness_planner
python fitness_planner.py
```
