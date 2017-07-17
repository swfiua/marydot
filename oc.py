import music

oh_canada = ['g:4',  'a:3', 'a',  'e:5', 
    'f', 'g', 'a', 'b', 'c', 'f',
    'g:4', 'a#', 'c', 'b:5', 'c', 'd', 'd', 'c' , 'c', 'b']

#oh_canada2 = ['e', 'g', 'g', 'c']

oc = 'eggcdefgad' + 'ef'

oc = [x for x in oc]

oc += oh_canada

music.play(oc)
