def latinize(word_given):
    word = f' {word_given} ' 
    temp = ''
    for i in range(len(word)):
        if word[i] == 'F': temp += 'A'
        elif word[i] == 'f': temp += 'a'
        elif word[i] == '<': temp += 'B'
        elif word[i] == ',': temp += 'b'
        elif word[i] == 'D': temp += 'V'
        elif word[i] == 'd': temp += 'v'
        elif word[i] == 'U': temp += 'H'
        elif word[i] == 'u': temp += 'h'
        elif word[i] == 'L': temp += 'D'
        elif word[i] == 'l': temp += 'd'
        elif (
            word[i] == 'T' and
            word[i-1].lower() in [' ', "'", 't', '`', '.', 'z', 'b', 's', 'j', 'e', 'f', "}", 'o'] ): temp += 'Je'
        elif word[i] == 'T': temp += 'Ie'
        elif (
            word[i] == 't' and
            word[i-1].lower() in [' ', "'", 't', '`', '.', 'z', 'b', 's', 'j', 'e', 'f', "}", 'o'] ): temp += 'je'
        elif word[i] == 't': temp += 'ie'
        elif word[i] == ':': temp += 'Ž'
        elif word[i] == ';': temp += 'ž'
        elif (
            word[i] == 'P' and
            word[i+1].lower() in ['t', '`', '.', 'z', 'b', 'm']): temp += 'Ź'
        elif (
            word[i] == 'p' and
            word[i+1].lower() in ['t', '`', '.', 'z', 'b', 'm']): temp += 'ź'
        elif word[i] == 'P': temp += 'Z'
        elif word[i] == 'p': temp += 'z'
        elif word[i] == 'B': temp += 'I'
        elif word[i] == 'b': temp += 'i'
        elif word[i] == 'Q': temp += 'J'
        elif word[i] == 'q': temp += 'j'
        elif word[i] == 'R': temp += 'K'
        elif word[i] == 'r': temp += 'k'
        elif word[i] == 'P': temp += 'Z'
        elif word[i] == 'p': temp += 'z'
        elif (
            word[i] == 'K' and
            word[i+1].lower() in ['t', '`', '.', 'z', 'b', 'm'] ): temp += 'L'
        elif word[i] == 'K': temp += 'Ł'
        elif (
            word[i] == 'k' and
            word[i+1].lower() in ['t', '`', '.', 'z', 'b', 'm'] ): temp += 'l'
        elif word[i] == 'k': temp += 'ł'
        elif word[i] == 'V': temp += 'M'
        elif word[i] == 'v': temp += 'm'
        elif (
            word[i] == 'Y' and
            word[i+1].lower() in ['t', '`', '.', 'z', 'b', 'm'] ): temp += 'Ń'
        elif word[i] == 'Y': temp += 'N'
        elif (
            word[i] == 'y' and
            word[i+1].lower() in ['t', '`', '.', 'z', 'b', 'm'] ): temp += 'ń'
        elif word[i] == 'y': temp += 'n'
        elif word[i] == 'J': temp += 'O'
        elif word[i] == 'j': temp += 'o'
        elif word[i] == 'G': temp += 'P'
        elif word[i] == 'g': temp += 'p'
        elif word[i] == 'H': temp += 'R'
        elif word[i] == 'h': temp += 'r'
        elif (
            word[i] == 'C' and
            word[i+1].lower() in ['t', '`', '.', 'z', 'b', 'm'] ): temp += 'Ś'
        elif word[i] == 'C': temp += 'S'
        elif (
            word[i] == 'c' and
            word[i+1].lower() in ['t', '`', '.', 'z', 'b', 'm'] ): temp += 'ś'
        elif word[i] == 'c': temp += 's'
        elif word[i] == 'N': temp += 'T'
        elif word[i] == 'n': temp += 't'
        elif word[i] == 'E': temp += 'U'
        elif word[i] == 'e': temp += 'u'
        elif word[i] == 'O': temp += 'Ŭ'
        elif word[i] == 'o': temp += 'ŭ'
        elif word[i] == 'A': temp += 'F'
        elif word[i] == 'a': temp += 'f'
        elif word[i] == '{': temp += 'Ch'
        elif word[i] == '[': temp += 'ch'
        elif (
            word[i] == 'W' and
            word[i+1].lower() in ['t', '`', '.', 'z', 'b', 'm'] ): temp += 'Ć'
        elif word[i] == 'W': temp += 'C'
        elif (
            word[i] == 'w' and
            word[i+1].lower() in ['t', '`', '.', 'z', 'b', 'm'] ): temp += 'ć'
        elif word[i] == 'w': temp += 'c'
        elif word[i] == 'X': temp += 'Č'
        elif word[i] == 'x': temp += 'č'
        elif word[i] == 'I': temp += 'Š'
        elif word[i] == 'i': temp += 'š'
        elif word[i] == 'S': temp += 'Y'
        elif word[i] == 's': temp += 'y'
        elif word[i] == '"': temp += 'E'
        elif word[i] == "'": temp += 'e'
        elif (
            word[i] == '>' and
            word[i-1].lower() in [' ', "'", 't', '`', '.', 'z', 'b', 's', 'j', 'e', 'f', "}", 'o'] ): temp += 'Ju'
        elif word[i] == '>': temp += 'Iu'
        elif (
            word[i] == '.' and
            word[i-1].lower() in [' ', "'", 't', '`', '.', 'z', 'b', 's', 'j', 'e', 'f', "}", 'o'] ): temp += 'ju'
        elif word[i] == '.': temp += 'iu'
        elif (
            word[i] == 'Z' and
            word[i-1].lower() in [' ', "'", 't', '`', '.', 'z', 'b', 's', 'j', 'e', 'f', "}", 'o'] ): temp += 'Ja'
        elif word[i] == 'Z': temp += 'Ia'
        elif (
            word[i] == 'z' and
            word[i-1].lower() in [' ', "'", 't', '`', '.', 'z', 'b', 's', 'j', 'e', 'f', "}", 'o'] ): temp += 'ja'
        elif word[i] == 'z': temp += 'ia'
        elif word[i] == '?': temp += ','
        elif word[i] == '/': temp += '.'
        else: temp += word[i]
    return temp.strip()