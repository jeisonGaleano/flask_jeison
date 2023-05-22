from api.database.db import get_connection
from .entities.Cmc import Cmc

class CmcModel():
    
    
    @classmethod
    def get_data_cmc(self):
        try:
            connection = get_connection()
            cmcList = []

            with connection.cursor() as cursor:
                cursor.execute("select \"Edad_esposa\" , educ_de_la_esposa ,educ_del_esposo,  num_de_hijos_nacidos ,     religion_de_la_esposa , la_esposa_trabaja_ahora ,ocupa_del_esposo , indice_de_nivel_de_vida , exposicion_a_los_medios , metodo_anticonceptivo_utilizado  from cmc")
                resultset = cursor.fetchall()

                for row in resultset:
                    cmcData = Cmc(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9])
                    cmcList.append(cmcData.to_JSON())

            connection.close()
            return cmcList
        except Exception as ex:
            raise Exception(ex)
    
    @classmethod
    def add_data_cmc(self, cmc):
        try:
            connection = get_connection()

            with connection.cursor() as cursor:
                cursor.execute("""INSERT INTO public.cmc
                                    (edad_esposa, educ_de_la_esposa, educ_del_esposo, num_de_hijos_nacidos, religion_de_la_esposa, 
                                    la_esposa_trabaja_ahora, ocupa_del_esposo, indice_de_nivel_de_vida, exposicion_a_los_medios, 
                                    metodo_anticonceptivo_utilizado)
                                    VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s);""", (cmc.edad_esposa, cmc.educ_de_la_esposa, cmc.educ_del_esposo, cmc.num_de_hijos_nacidos
                                    , cmc.religion_de_la_esposa, cmc.la_esposa_trabaja_ahora, cmc.ocupa_del_esposo, cmc.indice_de_nivel_de_vida, cmc.exposicion_a_los_medios, cmc.metodo_anticonceptivo_utilizado))
                affected_rows = cursor.rowcount
                connection.commit()

            connection.close()
            return affected_rows
        except Exception as ex:
            raise Exception(ex)