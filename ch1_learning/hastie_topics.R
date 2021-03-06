library(mallet) 
library(tm)
writeLines(stopwords(), 'en.txt')
system('pdftotext -f 1 -l 716 ../ml_lit/data/hastie_elem/hastie_elements_2009.pdf hastie_main.txt')
main_text = readLines('hastie_main.txt')
main_text_clean = paste(main_text, ' ', collapse=' ')
words = unlist(strsplit(main_text_clean, ' '))
words = tolower(words)
words = words[!words == '']
words = words[!words == '.']
length(words)
hastie_chunks = split(words, ceiling(seq_along(words)/1000))

ids = 1:length(hastie_chunks)
length(hastie_chunks)
df = data.frame(ids = ids, text = hastie_chunks, stringsAsFactors = FALSE )
mall = mallet.import(ids, hastie_chunks,'en.txt') 
topic.model = MalletLDA(20)
topic.model$loadDocuments(mall)
