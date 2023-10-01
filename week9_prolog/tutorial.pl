% Q1. Greatest Common Divisor
gcd(N,1,1) :- 1 =< N, !.
gcd(1,N,1) :- 1 =< N, !.
% gcd(N,N,N) :- 1 =< N, !.
gcd(N,M,S) :- N =:= M, !, S=N.

gcd(N,M,S) :- N < M, gcd(M,N,S).
 % "M < N" ensures the 2 conditions above are false
gcd(N,M,S) :- M < N, T is N-M, gcd(T,M,S).


% Q2. Prime number: 2, 3, 5, 7, 11
nodivide(X,Y) :- Y<X. % eg. nodivide(8, 4)
nodivide(X,Y) :- X<Y, Z is Y-X, nodivide(X,Z), !.  
% eg. nodivide(4, 7) ->  % nodivide(4, 3)
% eg. nodivide(4, 8) ->  % nodivide(4, 4)

nofactor(X,1) :- 1<X.
nofactor(X,Y) :- nodivide(Y,X), Z is Y-1, nofactor(X,Z).

prime(X) :- 2=<X, Y is X-1, nofactor(X,Y), !.


% Q2. Prime number version 2
% def is_prime(p):
%     """Trail division algorithm."""
%     if p < 2 or (p % 2 == 0 and p != 2):
%         return False
%     s = math.floor(math.sqrt(p))
%     for i in range(3, s + 1, 2):
%         if p % i == 0:
%             return False
%     return True
has_factor(N, L) :- N mod L =:= 0.
has_factor(N, L) :- L * L < N, L2 is L + 2, has_factor(N, L2).

is_prime(2).
is_prime(3).
is_prime(P) :- P > 3, P mod 2 =\= 0, \+ has_factor(P, 3).


% Q3. Quick sort
append([], A, A).
append([H | T], A, [H | L]) :- append(T, A, L).

partition(A, [], [], []).
partition(A, [H | T], [H | P], S) :- A >= H, partition(A, T, P, S).
partition(A, [H | T], P, [H | S]) :- A =< H, partition(A, T, P, S).


quicksort([], []).
quicksort([A | L1], L2) :- partition(A, L1, P1, S1), 
    quicksort(P1, P2), 
    quicksort(S1, S2), 
    append(P2, [A | S2], L2).
% quicksort([1,2,3], Sorted).
% quicksort([3,1,2], Sorted).

