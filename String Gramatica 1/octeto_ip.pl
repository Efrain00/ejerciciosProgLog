% Desarrolle un predicado que permita validar un octeto de una ip
% Responde a la siguiente gramatica
% Octeto ::= '2'<R5><R5> | '1'<Digito><Digito> | <Digito><Digito> | <Digito>
% R5 ::= 0 | 1 | 2 | 3 | 4 | 5
% Digito ::= 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9
%nip("255").
%true.
%nip("256").
%false

latom_lstring([], []).
latom_lstring([F|C],R) :- latom_lstring(C,S), atom_string(F,SF), append([SF],S,R).
preparar_string(Term, LS) :-
		atom(Term),
		atom_string(Term,Str),
		preparar_string(Str,LS).

preparar_string(Str,LS) :-
		string(Str),
		string_chars(Str,LAC),
		latom_lstring(LAC, LS).



r5(N) :-
        N == "0"; N == "1"; N == "2"; N == "3"; N == "4";
        N == "5".
octeto(X) :- string_length(X,R), R == 3 , preparar_string(X,Y), val_inicio(Y);
                string_length(X,R), R == 2 , preparar_string(X,Y), oct1(Y);
                string_length(X,R), R == 1 , preparar_string(X,Y), oct1(Y).
val_inicio([F|C]) :- F == "2", oct2([F|C]); F == "1" , oct1([F|C]).
% Octeto inicial con 2
oct2([Y|[]]) :- r5(Y).
oct2([Y|C]) :- r5(Y), oct2(C).
% Octeto inicial con 1 y el octeto con dos y un digito
oct1([Y|[]]) :- digito(Y).
oct1([Y|C]) :- digito(Y), oct1(C).
