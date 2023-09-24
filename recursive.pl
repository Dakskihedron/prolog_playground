in(hamilton,waikato).
in(waikato,northIs).
belong(X,Y) :- in(X,Y).
belong(X,Y) :- in(X,Z), belong(Z,Y).