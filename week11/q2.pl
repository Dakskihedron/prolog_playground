% Need install from Python using:
% pip install problog
% To run the code:
% python3 -m problog q2.pl

0.75::rainy.
0.85::cloudy.
0.15::sunny.

0.99::umbrella :- rainy.
0.75::umbrella :- cloudy.
0.5::umbrella :- sunny.

query(umbrella).
