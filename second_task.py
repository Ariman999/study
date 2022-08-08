primus_seconds = int(input('Ввведите колличество секунд: '))
hours = primus_seconds // 3600
minutes = (primus_seconds % 3600) // 60
seconds = primus_seconds % 60
print(f'время: {hours}:{minutes}:{seconds}')