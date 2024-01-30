def executar(função, *args):
   return função(*args)

chamar = executar(lambda multiplicador: lambda numero: numero * multiplicador, 2)
print(chamar(4))