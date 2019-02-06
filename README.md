# Fitness_Planner
Fitness Planner assists your workout by generating a sensible weightlifting plan, tracking your workout progress, and determining ideal warmup weights and rest times (based off the research discussed in "Bigger, Leaner, Stronger").

Command line program for now because I work out at home.

## Configuration

This uses two files that you can easily modify to fit your needs:

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

exercises.yaml lists potential exercises to do for each muscle group
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

These exercises are selected randomly, based on the current date and routine.yaml
They can start with an optional modifier to be treated differently:
```
*  - an exercise that must be performed
** - the exercise must be done before the others (within that muscle group)
^  - user-preferred exercise (higher probability of being selected)
=  - last exercise for that muscle group (intended for isolation exercises)
```

## How to Run:

```
pip install numpy pyYaml
git clone https://github.com/evliang/fitness_planner.git
cd fitness_planner
python fitness_planner.py
```