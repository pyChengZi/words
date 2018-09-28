import os
import random

path = os.path.dirname(__file__) + '/word.txt'

words = [
    'lethargic', 'fungible', 'solicitous', 'conjecture', 'venerate', 'mendacious',
    'discern', 'disguise', 'far-fatched', 'eclipse', 'impulsive', 'obfuscate', 'droll',
    'inevitable', 'intransigent', 'ameliorate', 'mitigate', 'extenuate', 'shackle',
    'concrete', 'elicit', 'exaggerate', 'unwitting', 'inclusive', 'ebullient', 'bolster',
    'coddle', 'nuance', 'peculiar', 'egalitarian', 'propitiate', 'amicable', 'clamorous',
    'futile', 'tenacious', 'skullduggery', 'ambivalent', 'ingenuous', 'capricious',
    'disdain', 'deteriorate', 'sardonic', 'expedite', 'arduous', 'vexation', 'encomium',
    'propaganda', 'courteous', 'insular', 'unyielding', 'covert', 'indict', 'insult',
    'promulgate', 'grudge', 'corroborate', 'unassuming', 'apocalypse', 'integrity',
    'comprehensive', 'surreptitious', 'soft-pedal', 'entangle', 'compliant', 'dispassionate',
    'transient', 'pervasive', 'opulent', 'feign', 'daunting', 'dilatory', 'sensational',
    'penance', 'explicable', 'pernicious', 'convoluted', 'trifling', 'compunction',
    'cynical', 'pretentious', 'vilify', 'fractious', 'stifle', 'authenticate', 'palliate',
    'trivial', 'impeccable', 'astute', 'presage', 'cordial', 'querulous', 'stalwart',
    'unconscionable', 'predilection', 'outrage', 'episodic', 'bemuse', 'intuition',
    'observant', 'salient', 'accede', 'tribute', 'camaraderie', 'pensive', 'culmination',
    'sober', 'seditious', 'diligent', 'punctilious', 'dissent', 'betoken', 'affirmative',
    'obligatory', 'commensurate', 'synopsis', 'snobbish', 'salutary', 'incendiary', 'rile',
    'devious', 'vacillate', 'abstemious', 'pragmatic', 'didactic', 'versatile', 'rudimentary',
    'elude', 'mawkish', 'pertinacious', 'paucity', 'debilitate', 'nominal', 'erudite', 'dilute',
    'complacent', 'quixotic', 'invidious', 'scarce', 'dejected', 'resent', 'manifest', 'gambit',
    'palatable', 'impenetrable', 'mockery', 'austere', 'impertinent', 'annex', 'vivacious',
    'deliberate', 'obtrude', 'subsidize', 'chicanery', 'concoct', 'ephemeral', 'stratify',
    'affinity', 'umbrage', 'ramification', 'adjuration', 'dreary', 'thwart', 'impugn',
    'pejorative', 'blithe', 'enervate', 'excoriate', 'esteem', 'delegate', 'blatant', 'alarmism',
    'torpor', 'indolent', 'impetuous', 'disparate', 'respite', 'acquiesce', 'overwrought',
    'malleable', 'encumber', 'repugnant', 'dissemble', 'scintillating', 'lugubrious', 'parochial',
    'encyclopedic', 'nondescript', 'churlish', 'deceive', 'credential', 'scandalous', 'flabbergast',
    'palpable', 'sluggish', 'sway', 'inflammatory', 'delude', 'volatile', 'conundrum', 'contrive',
    'unimpeachable', 'tortuous', 'perturb', 'fraudulent', 'perilous', 'multitudinous', 'mediocre',
    'irritate', 'erratic', 'endorse', 'malign', 'imperative', 'perpetuate', 'anathema'
]
words.sort()  # 正序排列
words.sort(key=lambda a: a[-1])
# random.shuffle(words)  # 乱序排列
output_words = [words[i:i+3] for i in range(0, len(words), 3)]
f = open(path, 'w')
for word in output_words:
    for single_word in word:
        f.write(single_word + ' ' * (30 - len(single_word)))
    f.write('\n')
f.close()
