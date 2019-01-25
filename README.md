# Fitness_Planner
Fitness Planner generates an exercise plan and tracks your workout progress over time.

## Configuration

There are two config files for setting up routine and list of exercises to choose from.

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
- "push ups"
- "low-incline dumbbell bench press"
- "dumbbell pullovers"
- "=dumbbell bench press hold"
back:
- "pull-ups"
- "^one-arm dumbbell row"
- "**deadlift"
- "dumbbell incline row"
- "reverse grip bent-over rows"
```

An optional modifier may appear in the beginning:
```
*  - an exercise that must be performed
** - the exercise must be done before the others (within that muscle group)
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
