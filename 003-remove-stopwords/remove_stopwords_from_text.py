# -*- encoding: utf-8 -*-

import string

from indicnlp.tokenize import sentence_tokenize
from indicnlp.tokenize import indic_tokenize

from nltk.corpus import stopwords

te_text = """
పరీక్షిత్తు మహారాజులా తాను కూడా ఏడు రోజులపాటు భాగవతం విని మోక్షం పొందాలనుకున్నాడో రాజు. 
పండితుణ్ణి పిలిచి భాగవతం చదివించుకుని విన్నాడు. 
వారం గడిచినా... ఇంకా తనకు మోక్షం ఎందుకు సిద్ధించలేదని అడిగాడు. 
ఆ మాటలు విన్న పండితుడు- 'రాజా! నా పని భాగవతాన్ని వినిపించడం వరకే. మోక్షం ఇప్పిస్తానని నేను చెప్పలేదు కదా! అయితే మీ ప్రశ్నకు మా గురువు సరైన సమాధానం ఇవ్వగలరు. ఆయన్ని పిలిపించండి' అన్నాడు. 
గురువు వచ్చాడు. 
పండితుణ్ణి అడిగిన ప్రశ్నే అతణ్ణీ అడిగాడు రాజు. 
'ఒక్క పావుగంట పాటు నన్ను ఈ రాజ్యానికి రాజును చేస్తే.. మీ సందేహం తీరుస్తాను మహారాజా' అన్నాడతను. 
అలాగేనన్నాడు రాజు. గురువు సింహాసనం అధిరోహించగానే.. పండితుణ్ణి, రాజునూ ఇద్దరినీ బంధించమన్నాడు. 
కొన్ని నిమిషాల తర్వాత గురువు పండితుడి వంక చూసి 'రాజును బంధ విముక్తుణ్ణి చెయ్యి' అన్నాడు. 
దానికి పండితుడు 'నా కట్లు విప్పకుండా నేనెలా విడిపించగలను?’ అన్నాడు. 'రాజా! ఇప్పుడు మీ సందేహం తీరిందా? బందీ అయిన వ్యక్తి మరొకరి బంధనాలను తొలగించలేనట్లే.. ముక్తుడు కాని వ్యక్తి మరొకరికి ముక్తి కలిగించలేడు. శుకమహర్షి వంటి యోగి లభించి, పరీక్షిత్తు అంతటి శ్రద్ధాసక్తులు ఉన్నప్పుడే మోక్షం సిద్ధిస్తుంది. అంటే బోధించే గురువు మహాజ్ఞాని అయ్యుండాలి. అలాగే అది వినే వ్యక్తికి అర్థం చేసుకునే గొప్ప విజ్ఞత ఉండాలి' అంటూ వివరించాడు గురువు. 
మోక్షసిద్ధి గురించి ఒక శిష్యుడు అడిగిన ప్రశ్నకు రామకృష్ణ పరమహంస చెప్పిన కథ ఇది.
"""

telugu_stopwords = [
    "ఆ",
    "ఈ",
    "నా",
    "మీ",
    "మా",
    "మీరు",
    "అందు",
    "అందులో",
    "చేత",
    "ఓరీ",
    "ఓయీ",
    "ఓసీ",
    "నుంచి",
    "నుండి",
    "తన",
    "తాను",
    "కూడా",
    "ఇంకా",
    "అన్ని",
    "అన్నింటిని",
    "అన్నింటినీ",
]


def get_telugu_stop_words():
    stop_words = stopwords.words('english')
    for word in telugu_stopwords:
        stop_words.append(word)
    return stop_words


def remove_punctuation(text_with_punctuation):
  trans_table = str.maketrans('', '', string.punctuation)
  return text_with_punctuation.translate(trans_table)


def remove_stopwords_from_sentence(sentence):
    stop_words = get_telugu_stop_words()
    word_tokens = indic_tokenize.trivial_tokenize(remove_punctuation(sentence))

    if not word_tokens:
        return ""

    words_without_stopwords = list(filter(bool, [w for w in word_tokens if w not in stop_words]))
    return " ".join(words_without_stopwords)


print("====================================")

print("\n\nOriginal Text:\n")

print(te_text)

print("\n\nSentences before removing stop words:\n")

sentences = sentence_tokenize.sentence_split(te_text, lang='te')

print("\n".join(sentences))

print("\n\nSentences after removing stopwords:\n")

sentences_without_stopwords = list(filter(bool, [remove_stopwords_from_sentence(s) for s in sentences]))

print("\n".join(sentences_without_stopwords))

print("====================================")
