import streamlit as st
import pandas as pd
from agent import AgentStockOpt

# Configuration de la page
st.set_page_config(page_title="StockOpt", page_icon="🏭")

# Titre
st.title("🏭 StockOpt - Agent Autonome")

# Charger les stocks
stocks = pd.read_csv("stocks.csv")

# Créer l'agent
if "agent" not in st.session_state:
    st.session_state.agent = AgentStockOpt()
if "resultats" not in st.session_state:
    st.session_state.resultats = []

# Afficher le tableau des stocks
st.subheader("📊 État des stocks")
st.dataframe(stocks)

# Bouton pour lancer l'agent
if st.button("🚀 Lancer l'agent"):
    st.session_state.resultats = []
    
    # L'agent vérifie chaque produit
    for i in range(len(stocks)):
        produit = stocks.loc[i, "produit"]
        quantite = stocks.loc[i, "quantite"]
        seuil = stocks.loc[i, "seuil"]
        
        resultat = st.session_state.agent.verifier_stock(produit, quantite, seuil)
        st.session_state.resultats.append(resultat)

# Afficher les décisions de l'agent
st.subheader("📝 Décisions de l'agent")

if st.session_state.resultats:
    for r in st.session_state.resultats:
        if r.get("status") == "acceptee":
            st.success(f"✅ {r['message']}")
        elif r.get("status") == "rien_a_faire":
            st.info(f"ℹ️ {r.get('produit')}: stock OK")
        else:
            st.write(f"📌 {r}")
else:
    st.info("Cliquez sur 'Lancer l'agent'")

# Pied de page
st.caption("StockOpt - Équipe Phoenix")