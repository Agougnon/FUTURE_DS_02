# Importation des librairies
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

# Configuration esthétique des graphiques
sns.set_theme(style="whitegrid")
plt.rcParams["figure.figsize"] = (12, 6)

# 1. Chargement du jeu de données
df = pd.read_csv("WA_Fn-UseC_-Telco-Customer-Churn.csv")

print("--- APERÇU DES DONNÉES CLIENTS ---")
print(df.head(3))
print(f"\nNombre total de clients analysés : {df.shape[0]:,}")

# 2. Nettoyage de la colonne TotalCharges (convertie en numérique propre)
df["TotalCharges"] = pd.to_numeric(df["TotalCharges"], errors="coerce")
df["TotalCharges"] = df["TotalCharges"].fillna(df["TotalCharges"].median())

# 3. Calcul des KPI de Rétention et de Churn
total_clients = len(df)
churn_rate = (df["Churn"] == "Yes").mean() * 100
retention_rate = 100 - churn_rate

print("\n" + "=" * 40)
print("RAPPORT DE RÉTENTION ET DE CHURN")
print("=" * 40)
print(f"Taux de Rétention Global : {retention_rate:.2f}%")
print(f"Taux de Churn (Désabonnement) Global : {churn_rate:.2f}%")

# 4. Analyse du Churn par Type de Contrat
churn_by_contract = (
    df.groupby("Contract")["Churn"]
    .apply(lambda x: (x == "Yes").mean() * 100)
    .reset_index(name="Churn_Rate_Percent")
)
print("\n--- Taux de Churn par Type de Contrat (%) ---")
print(churn_by_contract)

# 5. Génération des visualisations graphiques

# Graphique 1 : Répartition globale du Churn
plt.figure(figsize=(6, 4))
sns.countplot(
    data=df,
    x="Churn",
    palette=["#2b5c8f", "#d9534f"],
    hue="Churn",
    legend=False,
)
plt.title(
    "Répartition Globale des Clients (Restés vs Partie)",
    fontsize=13,
    fontweight="bold",
)
plt.xlabel("Statut du Client (Churn)", fontsize=11)
plt.ylabel("Nombre de clients", fontsize=11)
plt.tight_layout()
plt.show()

# Graphique 2 : Taux de Churn selon le Type de Contrat
plt.figure(figsize=(8, 4))
sns.barplot(
    data=churn_by_contract,
    x="Contract",
    y="Churn_Rate_Percent",
    palette="Blues_r",
    hue="Contract",
    legend=False,
)
plt.title(
    "Taux de Désabonnement par Type de Contrat", fontsize=13, fontweight="bold"
)
plt.xlabel("Type de Contrat", fontsize=11)
plt.ylabel("Taux de Churn (%)", fontsize=11)
plt.tight_layout()
plt.show()
