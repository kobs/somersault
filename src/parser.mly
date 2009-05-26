%token EOF

%token T_BOOL
%token T_DUMMY
%token T_INT
%token T_NIL
%token T_STRING

%token IDENTIFIER

%token LPAREN
%token RPAREN

/* reserved */
%token ARROW
%token DUMMY
%token FALSE
%token FUN
%token LET
%token NIL
%token REC
%token TRUE
%token WHERE
%token WITHIN


/* operators */
%token NEG
%token PLUS MINUS TIMES DIV
%token EQUAL LESS GREAT LESS_E GREAT_E
%token AT

%start expr
%type unit
%%

expr:
   EOF                { () }

%%
