import sys,re

expressions = [
    (r'[ \n\t]+',              None), # whitespace 
    (r'#[^\n]*',               None), # comments
	(r'\(',                    'T_LEFT'), #l_bracket##
	(r'\:',                    'T_COL'), #colon ##
    (r'\)',                    'T_RIGHT'), #r_bracket##
    (r';',                     'T_SEM'), #semicolon ##
	(r'\.',					   'T_DOT'), #dot ##
	(r',',                     'T_COMMA'), #comma##
    (r'\+',                    'T_PLUS'), #add ##
    (r'\-',                    'T_MINUS'), #subtract ##
    (r'\*',                    'T_MUL'), #multiply ##
    (r'/',                     'T_DIV'), #divide ##
	(r'\%',					   'T_MOD'), #MODULUS ##
	(r'&&',					   'T_AND'), #and ##
	(r'==',					   'T_EQQ'), #isequal ##
	(r'\|\|',				   'T_OR'), # or ##
    (r'<=',                    'T_LE'), #less then equal ##
    (r'>=',                    'T_GE'), #greater then equal ##
    (r'!=',                    'T_NE'), #not equal to ##
	(r'!',					   'T_NOT'), #not ##
	(r'=',	                   'T_EQ'), # assignment ##
	(r'<',                     'T_LT'), #lessthen ##
	(r'>',                     'T_GT'), #greater then ##
	(r'\[',                    'T_SQL'), #sql ##
	(r'\]',                    'T_SQR'), #sqr ##
    (r'return',                'T_RET'), #return ##
	(r'integer',               'T_NUM'), #integer ##
	(r'decimal',               'T_DEC'), #decimal ##
	(r'string',                'T_STRING'), #string ##
	(r'boolean',			   'T_BOOL`'), #boolean ##
	(r'record',                'T_REC'), #record ##
	(r'struct',                'T_STRUCT'), #structure ##
	(r'main',                  'T_MAIN'), #main ##
    (r'endif',                 'T_ENDIF'), #ENDIF ##
    (r'if',                    'T_IF'), #if ##
	(r'get',                   'T_GET'), #get ##
	(r'break',                 'T_BREAK'), #break ##
	(r'continue',              'T_CONTINUE'), #continue ##
    (r'end',                   'T_END'), #end ##
	(r'number',                'T_NUM'), #number ##
	(r'decimal',               'T_DEC'), #decimal ##
	(r'string',                'T_STRING'), #string ##
	(r'boolean',               'T_BOOL'), #boolean ##
	(r'function',              'T_FUN'), #function##
	(r'array',                 'T_ARR'), #array ##
	(r'call',                  'T_CALL'), #call ##
	(r'variable',              'T_VAR'), #variable ##
	(r'endWhile',              'T_ENDWHILE'), #endwhile ##
	(r'while',                 'T_WHILE'), #while  ##
	(r'true',                  'L_BOOL'), #while  ##
	(r'false',                 'L_BOOL'), #while  ##
	(r'".*?"',                 'L_STRING'), #string  ##
	(r'[0-9]+(\.[0-9][0-9]*)', 'L_DEC'), #decimal number
	(r'[0-9]+',                'L_NUM'),      #integer 
    (r'[A-Za-z][A-Za-z0-9_]*', 'T_ID'),       #variable names ##
]


def lexer(input, expressions):
    loc = 0
    tokens = []
    while loc < len(input):
        match = None
        for token_expr in expressions:
            pattern, tag = token_expr
            regex = re.compile(pattern)
            match = regex.match(input, loc)
            if match:
                text = match.group(0)
                if tag:
                    token = (text, tag)
                    tokens.append(token)
                break
        if not match:
            sys.stderr.write('Illegal character: %s\n' % input[loc])
            sys.exit(1)
        else:
            loc = match.end(0)
    return tokens
	

def run(name):
    filename = name
    file = open(filename)
    input = file.read()
    file.close()
    tokens = lexer(input,expressions)

    str=''
    for token in tokens:
        str = str + ' ' + token[1]
        
    #print str
    return str
    
if __name__ == '__main__':
    print 'TokenStream'
    print '-----------'
    print(run(sys.argv[1]))