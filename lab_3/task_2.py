def find_common_participants(firstgroup, secondgroup, sep=','):
    newfirstgroup = set(firstgroup.split(sep))
    newsecondgroup = set(secondgroup.split(sep))
    newgroup = newfirstgroup.intersection(newsecondgroup)
    a = list(newgroup)
    return sorted(a)


participants_first_group = "Иванов|Петров|Сидоров|Афин"
participants_second_group = "Петров|Сидоров|Смирнов|Афин"

print('Участники:', find_common_participants(participants_first_group, participants_second_group, '|'))

