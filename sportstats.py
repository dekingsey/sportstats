import requests

def grab(id):
  reponse = requests.get(f"https://sportstats.one/fr/results/athlete/{id}")
  contenu = str(reponse.content)
  debut = contenu.find('"pdn":"')
  if debut != -1: 
    debut += len('"pdn":"')
    fin = contenu.find('"', debut)
    return (contenu[debut:fin])
  else:
    return ""

if __name__ == "__main__":
  for i in range(57040, 760000):
    with open("sportstats.dat", "a") as f:
      resultat = grab(i)
      if resultat:
        f.write(f"{i}\t{resultat}\n")
