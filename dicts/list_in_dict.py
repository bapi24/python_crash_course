fav_lang = {
    'tony': ['python', 'ruby'],
    'sarah': ['haskell'],
    'spidy': ['javascript', 'python'],
    'marcus': ['c', 'ruby'],
    'steve': ['go', 'c++'],
}

for name, languages in fav_lang.items():
    if len(languages) == 1:
        print('\n' + name + "'s favorite languages is:")
    else:
        print('\n' + name + "'s favorite languages are:")
    for language in languages:
        print("\t" + language.title())
