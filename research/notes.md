question: maybe it's better to filter prices by a given exchange instead of the use of trades aggegated across all
exchanges. especially if the all trades flat files contain something that was traded OTC. because OTC trades might be
far from best bid/ask on a given exchange at the moment. such OTC deals will be creating spikes in volume and jumps in price.

answer: ???

q1: how many unique patterns?
a: tSNE in results_analysis.ipynb

q2: if a is close to b and c, is c close to b?
a: https://chatgpt.com/c/6892ec33-8b48-832b-a2a4-927ce84e3d67

q3: how rmse is related to correlation?
a: https://chatgpt.com/c/6890f9c5-5874-8331-a846-2dda502b541e
correlation_intuition.ipynb

q4: we rescale only prices (y-axe). shall we rescale the time (x-axe)?

--

research: 

+ first test then analyze all points

- update results_analysis after recalculation of find_similar
- draw patterns by hand

- add sl levels to trades on price chart
- add exits, duration

- all similar on one chart with extended endings
- endings histogram
- exit stragegy based on deviations

- RTH
- use ATR
- prev year
- next year

- multithreading
