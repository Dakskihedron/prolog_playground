food(muesli).
food(juice).

0.75::rainy.
0.85::cloudy.
0.15::sunny.

0.99::umbrella :- rainy.
0.75::umbrella :- cloudy.
0.5::umbrella :- sunny.

0.8::breakfast(X) :- umbrella, food(X).
0.3::breakfast(X) :- \+umbrella, food(X).

evidence(breakfast(muesli), true).
evidence(breakfast(juice), true).

query(umbrella).