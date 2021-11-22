импорт ре
 строка импорта
частота  = {}
document_text  =  open ( 'tom_sawyer.txt' , 'r' )
text_string  =  document_text . читать (). ниже ()
match_pattern  =  re . findall ( r '\ b [az] {3,15} \ b' , текстовая_строка )

для  слова  в  match_pattern :
    count  =  частота . получить ( слово , 0 )
    частота [ слово ] =  количество  +  1
    
frequency_list  =  частота . ключи ()

для слов  в  списке frequency_list :
    печать ( слова , частота [ слова ])