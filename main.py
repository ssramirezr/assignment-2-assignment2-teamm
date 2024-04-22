def cky(G, x):
  n = len(x)
  tabla = [[set() for j in range(n + 1)] for i in range(n)]

  for i in range(n):
      for produccion, no_terminales in G.items():
          if x[i] in produccion:
              tabla[i][i+1].update(no_terminales)

  for l in range(2, n + 1):
      for i in range(n - l + 1):
          j = i + l
          for k in range(i + 1, j):
              for B in tabla[i][k]:
                  for C in tabla[k][j]:
                      BC = B + C
                      if BC in G:
                          tabla[i][j].update(G[BC])

  return 'S' in tabla[0][n]  

def main():
  try:
     
      casos = int(input("Ingrese el número de casos: "))

      for _ in range(casos):
          
          k, m = map(int, input().split())

          
          G = {}
          for _ in range(k):
              entrada = input().split()
              no_terminal = entrada[0]
              producciones = entrada[1:]

              for produccion in producciones:
                  if produccion not in G:
                      G[produccion] = []
                  G[produccion].append(no_terminal)

          
          resultados = []
          for _ in range(m):
              cadena = input()
              resultado = cky(G, cadena)
              resultados.append(resultado)

        
          for resultado in resultados:
              if resultado:
                  print('yes')
              else:
                  print('no')

  except ValueError:
      print("Error: Formato de entrada inválido")

if __name__ == "__main__":
  main()
