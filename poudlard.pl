% suspects
suspect(drago).
suspect(neville).
suspect(ginny).

%règles logiques
declaration(drago) :- coupable(drago), innocent(neville).
declaration(neville) :- coupable(drago), innocent(ginny).
declaration(ginny) :- coupable(ginny), \+ coupable(drago), \+ coupable(neville).

%innocent inverse de coupable
innocent(X) :- \+ coupable(X).

%coupables
coupable(drago) :- declaration(drago).
coupable(neville) :- declaration(neville).
coupable(ginny) :- declaration(ginny).

% seul coupable
un_seul_coupable :-
    coupable(X),
    \+ (coupable(Y), X \= Y),
    suspect(X).
