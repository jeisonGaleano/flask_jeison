class Cmc():


    def __init__(self, edad_esposa, educ_de_la_esposa = None,
                    educ_del_esposo  = None, num_de_hijos_nacidos  = None, religion_de_la_esposa  = None,
                    la_esposa_trabaja_ahora = None , ocupa_del_esposo = None, indice_de_nivel_de_vida = None,
                    exposicion_a_los_medios = None, metodo_anticonceptivo_utilizado = None) -> None:
        self.edad_esposa = edad_esposa
        self.educ_de_la_esposa = educ_de_la_esposa
        self.educ_del_esposo = educ_del_esposo
        self.num_de_hijos_nacidos = num_de_hijos_nacidos
        self.religion_de_la_esposa = religion_de_la_esposa
        self.la_esposa_trabaja_ahora = la_esposa_trabaja_ahora
        self.ocupa_del_esposo = ocupa_del_esposo
        self.indice_de_nivel_de_vida = indice_de_nivel_de_vida
        self.exposicion_a_los_medios = exposicion_a_los_medios
        self.metodo_anticonceptivo_utilizado = metodo_anticonceptivo_utilizado

    def to_JSON(self):
        return {
            'edad_esposa': self.edad_esposa,
            'educ_de_la_esposa': self.educ_de_la_esposa,
            'educ_del_esposo': self.educ_del_esposo,
            'num_de_hijos_nacidos': self.num_de_hijos_nacidos,
            'religion_de_la_esposa': self.religion_de_la_esposa,
            'la_esposa_trabaja_ahora': self.la_esposa_trabaja_ahora,
            'ocupa_del_esposo': self.ocupa_del_esposo,
            'indice_de_nivel_de_vida': self.indice_de_nivel_de_vida,
            'exposicion_a_los_medios': self.exposicion_a_los_medios,
            'metodo_anticonceptivo_utilizado': self.metodo_anticonceptivo_utilizado
        }