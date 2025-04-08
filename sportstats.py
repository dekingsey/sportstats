import requests

def grab(id):
  reponse = requests.get(f"https://sportstats.one/fr/results/athlete/{id}")
  contenu = str(reponse.content)
  debut = contenu.find('"pdn":"') + len('"pdn":"')
  fin = contenu.find('"', debut)
  return (contenu[debut:fin])

if __name__ == "__main__":
  for i in range(1, 760000):
    with open("sportstats.dat", "a") as f:
      f.write(f"{i}\t{grab(i)}\n")
