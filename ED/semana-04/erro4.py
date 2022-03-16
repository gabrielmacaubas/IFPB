try:
    idade = int('25anos')
except Exception as e:
    print(e)
    print(e.__str__())