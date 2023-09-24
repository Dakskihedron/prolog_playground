append([], A, A).
append([H | T], A, [H | L]) :- append(T, A, L).

% ?- append([a, b, c], [d, e], L).
% ?- append(X, [d, e], [a, b, c, d, e]).