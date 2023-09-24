% if X >= Y, then Max := X
% if X < Y, then Max := Y
max(X,Y,X) :- X >= Y,!.
max(X,Y,Y) :- X < Y.

% Using `cut !` to write if else:
max_find(X,Y,Max) :- X >= Y,!, Max = X; Max = Y.

list_member(X,[X|_]) :- !.
list_member(X,[_|TAIL]) :- list_member(X,TAIL).

list_append(A,T,T) :- list_member(A,T),!.
list_append(A,T,[A|T]).
