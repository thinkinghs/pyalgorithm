# https://www.codewars.com/kata/format-a-string-of-names-like-bart-lisa-and-maggie/python
# there are more short solutions. I have to study. But my solution is easy to read

def namelist(names):
    if not names:
        return ''
    if len(names) == 1:
        return names[0]['name']
    name_list = ''
    for i in range(len(names)):
        if len(names) - i > 2:
            name_list += names[i]['name'] + ', '
        else:
            break
    name_list += names[-2]['name'] + ' & ' + names[-1]['name']
    return name_list
