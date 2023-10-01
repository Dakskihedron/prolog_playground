crime(X) :- nz(X), alcohol(Y), sells(X, Y, Z), minor(Z).
owns(lucy, b).
beers(b).
under17(lucy).
sells(david, X, lucy) :- beers(X), owns(lucy, X).
alcohol(X) :- beers(X).
minor(X) :- under17(X).
nz(david).
