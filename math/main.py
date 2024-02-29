import pandas as pd


network_df = pd.read_csv("./data/reseau_en_arbre.csv")

network_origanl_df = pd.DataFrame(network_df) 

network_duplicate_df = network_origanl_df.copy()

network_duplicate_df.drop()


batiment_subdfs = network_duplicate_df.groupby(by="id_batiment")
for id_batment, batiment_subdfs in batiment_subdfs:
    print(id_batment)
    print(batiment_subdfs)
    print("_"*30)


infra_subdfs = network_duplicate_df.groupby(by="infra_id")
for infra_id, infra_subdfs in infra_subdfs:
    print(infra_id)
    print(infra_subdfs)
    print("_"*30)


class Infra:
    def __init__(self, infra_id, length, infra_type, nb_houses ):
        self.infra_id = infra_id
        self.length = length
        self.infra_type = infra_type
        self.nb_houses = nb_houses
    
    def repair_infra(self, type_infra):
        for i in infra_subdfs(len(type_infra)):
            if type_infra[i] == "à remplacer":
                type_infra[i] = "intacte"
                return type_infra
    
    def get_infra_difficulty(self, length, infra_type, nb_houses):
        for length, infra_type in infra_subdfs:
            if infra_type == "intacte" :
                return 0
            else :
                return length / nb_houses
    
    def __radd__(self, other_infra):
        return self.get_infra_difficulty + other_infra


class Batiment:
    def __init__(self, id_building, list_infras):
        self.id_building = id_building
        self.list_infras = list[Infra]    

    def get_building_difficulty (self, other_infra):
        for list[Infra] in batiment_subdfs:
            if other_infra != 0:
                return sum(other_infra)
    
    def __lt__(self, other_object):
        if type(other_object) != Batiment:
            return Exception("Erreur")
        else:
            return self.list_infras < other_object.list_infras


#L'algorythme        
def find_building(list_infras):
    return min(list_infras, key=lambda x: x.get_infra_difficulty)


def reparer_bat(list_infras):
    print("Réparation des infrastructures pour le bâtiment :", list_infras.id_building)


batiment_impactes = list[Infra]

batiment_repares =[]


while batiment_impactes:
    batiment_a_reparer = find_building(batiment_impactes)
    
    reparer_bat(batiment_repares)
    
    batiment_repares.append(batiment_repares)
    
    batiment_impactes.remove(batiment_repares)

print("Tout est réparé.")





