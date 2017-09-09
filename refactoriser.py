from redbaron import RedBaron

red = RedBaron("""def setSchemaDb(self):

        print("creation du schemas")
        REQ = ['creer_tables_datetimeexperimentalsqlite3',
               'creer_table_periodesTravaillees_datetimeexperimentalsqlite3',
               'creer_trig_aj_periode_trav_from_scission_poste',
               'creer_trig_aj_periode_trav_from_copy_poste',
               'vue_35_semaine',
               'vue_CP_semaine',
               'vue_35_semaine_hsup_sans_bonif',
               'plus_de_48_heures',
               'hs_dues_hebdo',
               'vue_heures_annu_janjan',
               'vue_cumul_annu_juin_a_mai'
               ]

        for tache in REQ:
            print("setSchemaDb : début tâche {}".format(tache))
            self.getCnx().execute(
                self.getBibliothecaireDba()
                .getRequeteCreaByName(tache)
                )

# 12
#         self.getCnx().execute(
#             self.getBibliothecaireDba()
#             .getRequeteCreaByName('creer_tables_datetimeexperimentalsqlite3')
#
#             )
##        self.getCnx().execute(
##            self.getBibliothecaireDba()
##            .getRequeteCreaByName('creer_table_joursTravailles')
##            )
#         self.getCnx().execute(
#             self.getBibliothecaireDba()
#             .getRequeteCreaByName('creer_table_periodesTravaillees_datetimeexperimentalsqlite3')
#             )

# 9
#         self.getCnx().execute(
#             self.getBibliothecaireDba()
#             .getRequeteCreaByName('creer_trig_aj_periode_trav_from_scission_poste')
#             )
#
#         self.getCnx().execute(
#             self.getBibliothecaireDba()
#             .getRequeteCreaByName('creer_trig_aj_periode_trav_from_copy_poste')
#             )
#         self.getCnx().execute(
#             self.getBibliothecaireDba()
#             .getRequeteCreaByName('vue_35_semaine')
#             )
#6
#         self.getCnx().execute(
#             self.getBibliothecaireDba()
#             .getRequeteCreaByName('vue_CP_semaine')
#             )
#         self.getCnx().execute(
#             self.getBibliothecaireDba()
#             .getRequeteCreaByName('vue_35_semaine_hsup_sans_bonif')
#             )
#         self.getCnx().execute(
#             self.getBibliothecaireDba()
#             .getRequeteCreaByName('plus_de_48_heures')
#             )


#  3
#         self.getCnx().execute(
#             self.getBibliothecaireDba()
#             .getRequeteCreaByName('hs_dues_hebdo')
#             )
#         self.getCnx().execute(
#             self.getBibliothecaireDba()
#             .getRequeteCreaByName('vue_heures_annu_janjan')
#             )
#         self.getCnx().execute(
#             self.getBibliothecaireDba()
#             .getRequeteCreaByName('vue_cumul_annu_juin_a_mai')
#             )


        log.debug("schemas doit maintenant etre cree")""")
		
		
#red.help()
REQ =  red.find("assignment").dumps()
red.find("assignment").replace("pass")
red.find("def", name="setSchemaDb").arguments.append(REQ)


print(red.dumps())



######
from redbaron import RedBaron
with open("db.py", "r") as source_code:
    red = RedBaron(source_code.read())
with open("code.py", "w") as source_code:
    source_code.write(red.dumps())	
	

# how to query the tree
red.find("def", name="setSchemaDb").arguments.append(red.find())
print(red.dumps())

# how to modify the tree
# how to play with list of things
# miscellaneous but useful stuff