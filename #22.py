импорт  ОС
filename  =  "tom_sawyer.txt"
def  g_words ( имя файла ):
    с  открытым ( имя файла , кодировка = "utf8" ) как  файл :
        текст  =  файл . читать ()
    текст  =  текст . replace ( " \ n " , "" )
    текст  =  текст . replace ( "," , "" ). replace ( "." , "" ). replace ( "?" , "" ). replace ( "!" , "" )
    текст  =  текст . ниже ()
    слова  =  текст . разделить ()
    слова . sort ()
    ответные  слова
def  g_chars ( имя файла ):
    с  открытым ( имя файла , кодировка = "utf8" ) как  файл :
        chars  =  файл . читать ()
    chars  =  символы . replace ( " \ n " , "" )
    chars  =  символы . ниже ()
    вернуть  символы

def  chars_nospace ( имя файла ):
    с  открытым ( имя файла , кодировка = "utf8" ) как  файл :
        chars1  =  файл . читать ()
    chars1  =  chars1 . replace ( " \ n " , "" )
    chars1  =  chars1 . ниже ()
    chars1  =  chars1 . replace ( "" , "" )
    вернуть  символы1

def  g_words_dict ( слова ):
    words_dict  =  dict ()
 
    за  словом  в  словах :
        если  слово  в  words_dict :
            words_dict [ слово ] =  words_dict [ слово ] +  1
        еще :
            words_dict [ слово ] =  1
    вернуть  words_dict
 
 
def  main ():
    filename  =  "tom_sawyer.txt"
    слова  =  g_words ( имя файла )
    words_dict  =  g_words_dict ( слова )
    символы  =  g_chars ( имя файла )
    characters1  =  chars_nospace ( имя файла )
    print ( "Качество символов без пропусков:% d"  %  len ( characters1 ))
    print ( "Кількість символів:% d"  %  len ( символы ))
    print ( "Количество слів:% d"  %  len ( слова ))
    print ( "Кількість слів, що не повторються:% d"  %  len ( words_dict ))
    
если  __name__  ==  "__main__" :
        main ()
ввод ()