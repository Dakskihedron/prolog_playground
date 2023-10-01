natural(1).
natural(N) :- natural(M), N is M+1.
my_loop(N) :- natural(I), write(I), nl, I=N, !.
% nl is ’new line’ predicate