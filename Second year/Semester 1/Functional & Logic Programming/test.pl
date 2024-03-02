%Ciama Andreea Ciama
%grupa 921\2
%no:7

remove_k_occurences([], _, _, []) :- !.
remove_k_occurences(L, _, 0, L) :- !.
remove_k_occurences([H|T], E, K, R) :- H =:= E,
    K1 is K - 1,
    remove_k_occurences(T, E, K1, R).
remove_k_occurences([H|T], E, K, [H|R]) :- H =\= E,
     remove_k_occurences(T, E, K, R).


remove_3_occurences(L, E, R) :- remove_k_occurences(L, E, 3, R).
