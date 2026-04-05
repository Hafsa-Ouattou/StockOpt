# tools.py
# Ce fichier contient les outils que l'agent peut utiliser
# Ici, un seul outil : appeler le fournisseur

def appeler_fournisseur(produit, quantite):
    # Ce print s'affiche dans le terminal (pas dans l'interface)
    print(f"Appel du fournisseur pour {produit} : {quantite} unités")
    
    # On construit une réponse simulée (comme si le fournisseur répondait)
    reponse = {
        "status": "acceptee",           # La commande est acceptée
        "commande_id": 12345,           # Numéro de commande unique
        "produit": produit,             # Le produit commandé
        "quantite": quantite,           # La quantité commandée
        "message": f"Commande de {quantite} {produit} acceptée"  # Message pour l'utilisateur
    }
    
    # On retourne la réponse à l'agent
    return reponse