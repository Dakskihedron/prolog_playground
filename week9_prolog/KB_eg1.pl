parent(ann,bob).
parent(abe,bob).
parent(bob,dan).
parent(cat,dan).
parent(ann,ema).
parent(dan,fay).
male(abe).
male(bob).
male(dan).
female(X) :- \+(male(X)).
father(X,Y) :- parent(X,Y), male(X).
mother(X,Y) :- parent(X,Y), female(X).
son(X,Y) :- parent(Y,X), male(X).
sister(X,Z) :- parent(Y,X), parent(Y,Z), female(X).
aunt(X,Z) :- sister(X,Y), parent(Y,Z).
grandfather(X,Z) :- father(X,Y), parent(Y,Z).
ancestor(X,Y) :- parent(X,Y).
ancestor(X,Z) :- parent(X,Y), ancestor(Y,Z).