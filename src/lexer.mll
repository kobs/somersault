{
  open Parser
  open Printf
} 


let digit = ['0'-'9']
let identifier = ['a'-'z'] ['a'-'z' 'A'-'Z' '_']*

rule tokenize = parse
    [' ' '\t' '\r' '\n'] { tokenize lexbuf }
  | digit+ as number 
      { printf "(NUMBER, %i)\n" (int_of_string number);
        tokenize lexbuf
      }
  | identifier as id 
      { printf "(IDENTIFIER, %s)\n" id;
        tokenize lexbuf
      }
  | _ as c
      { printf "Unrecognized token: %c\n" c;
        tokenize lexbuf
      } 

  | eof { }


{
    let main () = 
      let cin = 
        if Array.length Sys.argv > 1 then
          open_in Sys.argv.(1)
        else
          stdin
      in
      let lexbuf = Lexing.from_channel cin in
      tokenize lexbuf

let _ = Printexc.print main ()
} 
