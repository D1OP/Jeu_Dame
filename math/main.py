import pandas as pd


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
        self.list_infras = list_infras

    def get_building_difficulty (self, other_infra):
        for list[Infra] in batiment_subdfs:
            if other_infra != 0:
                return sum(other_infra)
    
    def __lt__(self, other_object):
        if type(other_object) != Batiment:
            return Exception("Erreur")
        else:
            return self.list_infras < other_object.list_infras


def prepare_data(path_to_csv):
    network_df = pd.read_csv(path_to_csv).drop_duplicates()
    network_df = network_df[network_df["infra_type"] != "infra_intacte"]
    
    
    dict_infra = {}
    list_buildings = []
    
    infra_subdfs = network_df.groupby(by="infra_id")
    
    for infra_id, infra_subdfs in infra_subdfs:
        length = infra_subdfs["longueur"].iloc[0]
        infra_type = infra_subdfs["infra_type"].iloc[0]
        nb_houses = infra_subdfs["nb_maisons"].sum()
        dict_infra[infra_id] = Infra(infra_id, length, infra_type, nb_houses)
        
    building_subdfs = network_df.groupby(by="id_batiment")
    for id_bat, building_subdfs in building_subdfs:
        list_infra = []
        for infra_id in building_subdfs["infra_id"]:
            list_infra.append(dict_infra[infra_id])
        
        list_buildings.append(Batiment(id_bat, list_infra))
        
    return list_buildings


def plannification(list_buildings):
    sorted_buildings = []
    while list_buildings:
        current_building = min(list_buildings)
        sorted_buildings.append(current_building)
        for infra in current_building.list_infra:
            infra.repair_infra()
        list_buildings.remove(current_building)

    return sorted_buildings


if __name__ == "__main__":
    plannification(prepare_data(path_to_csv=".reseau_en_arbre.csv"))






