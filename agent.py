from tools import appeler_fournisseur  # On importe l'outil qu'on a créé

class AgentStockOpt:
    def __init__(self):
        self.historique = []  # Liste vide qui va stocker toutes les décisions
    def verifier_stock(self, produit, quantite, seuil, stock_max=None):
        # ÉTAPE 1 : RAISONNEMENT - L'agent analyse la situation
        
        # CAS 1 : STOCK BAS (quantité < seuil)
        if quantite < seuil:
            print(f" ALERTE BAS STOCK ! {produit} = {quantite} (seuil = {seuil})")
            
            # ÉTAPE 2 : PLANIFICATION - L'agent décide quoi faire
            # On commande pour remonter au-dessus du seuil
            quantite_a_commander = (seuil - quantite) + seuil
            print(f" DÉCISION : commander {quantite_a_commander} {produit} (stock bas)")
            
            # ÉTAPE 3 : EXÉCUTION - L'agent utilise l'outil
            resultat = appeler_fournisseur(produit, quantite_a_commander)
            
            # ÉTAPE 4 : MÉMOIRE - L'agent enregistre ce qu'il a fait
            self.historique.append({
                "produit": produit,
                "action": "commande_urgence",
                "quantite": quantite_a_commander,
                "raison": "stock_bas",
                "status": resultat["status"],
                "message": resultat["message"]
            })
            
            return resultat
        
        # CAS 2 : SURSTOCK (si stock_max est défini ET quantite > stock_max)
        elif stock_max is not None and quantite > stock_max:
            print(f" ALERTE SURSTOCK ! {produit} = {quantite} (max = {stock_max})")
            
            # ÉTAPE 2 : PLANIFICATION - L'agent décide d'arrêter les commandes
            print(f" DÉCISION : stopper les commandes pour {produit} (surstock)")
            
            # Ici l'agent ne commande pas, il alerte juste
            resultat = {
                "status": "surstock",
                "produit": produit,
                "quantite_actuelle": quantite,
                "stock_max": stock_max,
                "message": f" SURSTOCK : {produit} dépasse {stock_max} unités. Arrêt des commandes."
            }
            
            # MÉMOIRE
            self.historique.append({
                "produit": produit,
                "action": "alerte_surstock",
                "quantite": quantite,
                "raison": "surstock",
                "status": "surstock"
            })
            
            return resultat
        
        # CAS 3 : STOCK OK (entre seuil et stock_max)
        else:
            print(f" Stock OK pour {produit} = {quantite} (seuil = {seuil})")
            
            self.historique.append({
                "produit": produit,
                "action": "rien",
                "quantite": 0,
                "status": "ok"
            })
            
            return {"status": "rien_a_faire", "produit": produit}
    
    def get_historique(self):
        return self.historique