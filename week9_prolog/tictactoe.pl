ordered_line(1, 2, 3). ordered_line(4, 5, 6). ordered_line(7, 8, 9).
ordered_line(1, 4, 7). ordered_line(2, 5, 8). ordered_line(3, 6, 9).
ordered_line(1, 5, 9). ordered_line(3, 5, 7).

line(A, B, C) :- ordered_line(A, B, C). 
line(A, B, C) :- ordered_line(A, C, B).

line(A, B, C) :- ordered_line(B, A, C). 
line(A, B, C) :- ordered_line(B, C, A).

line(A, B, C) :- ordered_line(C, A, B). 
line(A, B, C) :- ordered_line(C, B, A).

% 2-players game. If any player (x or o) move to a location "A", "A" is full.
full(A) :- x(A). 
full(A) :- o(A). 
empty(A) :- \+(full(A)).

% NB: empty must be called with an already-instantiated A.
same(A, A). 

different(A, B) :- \+(same(A, B)).

move(A) :- good(A), empty(A), !.

% strategy:
good(A) :- win(A). 
good(A) :- block_win(A). 
good(A) :- splitt(A).
good(A) :- strong_build(A). 
good(A) :- weak_build(A).
good(5). 
good(1). 
good(3). 
good(7). 
good(9). 
good(2). 
good(4). 
good(6). 
good(8).

win(A) :- x(B), x(C), line(A, B, C), write('win'),nl.

block_win(A) :- o(B), o(C), line(A, B, C), write('block_win'),nl.

splitt(A) :- x(B), x(C), different(B, C), line(A, B, D), line(A, C, E), empty(D), empty(E), write('splitt'),nl.

strong_build(A) :- x(B), line(A, B, C), empty(C), \+(risky(C)), write('strong_build'),nl.

weak_build(A) :- x(B), line(A, B, C), empty(C), \+(double_risky(C)), write('weak_build'),nl.

risky(C) :- o(D), line(C, D, E), empty(E), write('risky'),nl.

double_risky(C) :- o(D), o(E), different(D, E), line(C, D, F), line(C,E,G),empty(F),empty(G), write('double_risky'),nl.

all_full :- full(1), full(2), full(3), full(4), full(5), full(6), full(7), full(8), full(9).

done :- ordered_line(A, B, C), x(A), x(B), x(C), write('I won.'), nl.

done :- all_full, write('Draw.'), nl.

getmove :- repeat, write('Please enter a move: '), read(X), empty(X), assert(o(X)).

makemove :- move(X), !, assert(x(X)).

makemove :- all_full.

printsquare(N) :- o(N), write('o').

printsquare(N) :- x(N), write('x').

printsquare(N) :- empty(N), write(' ').



printboard :- write('      -------'),nl,
write('      |'),printsquare(1), write('|'),printsquare(2), write('|'),printsquare(3), write('|'),nl,
write('      -------'),nl,
write('      |'),printsquare(4),write('|'), printsquare(5),write('|'), printsquare(6), write('|'),nl,
write('      -------'),nl,
write('      |'),printsquare(7), write('|'),printsquare(8), write('|'),printsquare(9),write('|'),nl,
write('      -------'),nl. 

clear :- retractall(x(_)), retractall(o(_)).

% main goal:
play :- clear, repeat, getmove, respond.
% Staring the game by calling function "play".

respond :- ordered_line(A, B, C), o(A), o(B), o(C), printboard, write('You won.'), nl. % shouldn't ever happen!

respond :- makemove, printboard, done.