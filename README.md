# Fitness_Planner
Fitness Planner assists your workout by
- generating a sensible and easily modifiable weightlifting plan
- determining ideal warmup weights and rest times (based off the research discussed in "Bigger, Leaner, Stronger").
- tracking your workout progress

This uses a CLI for now because I work out at home.

## Configuration

This uses two YAML files that you can easily modify to fit your needs:

routine.yaml -- creates a map from a muscle group to number of exercises to perform on it. In this example, Tuesdays are rest days
```
Sunday:
  chest: 3
  triceps: 2
Monday:
  back: 3
  biceps: 2
Wednesday:
  ...
```

exercises.yaml lists potential exercises for each muscle group.
```
chest:
- "push ups"
- "low-incline dumbbell bench press"
- "dumbbell pullovers"
- "= dumbbell bench press hold"
back:
- "pull-ups"
- "^ one-arm dumbbell row"
- "** deadlift"
- "dumbbell incline row"
- "reverse grip bent-over rows"
```

These exercises are selected randomly, based on routine.yaml and current day of week
Exercises can begin with an optional modifier for different treatment:
```
*  - an exercise that must be performed
** - the exercise must be done before the others (within that muscle group). Intended for compound exercises
^  - user-preferred exercise (higher probability of being selected)
=  - last exercise for that muscle group. Intended for isolation exercises
```

## How to Run:

```
pip install numpy pyYaml
git clone https://github.com/evliang/fitness_planner.git
cd fitness_planner
python fitness_planner.py
```