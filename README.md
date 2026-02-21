# Images to PDF Converter (Fullstack)

Application web Fullstack permettant de convertir plusieurs images en un fichier PDF unique, inspirée du service PDF24 - Images en PDF.

---
##  Structure du projet


##  Fonctionnalités

- Sélection multiple d’images
- Glisser-déposer (Drag & Drop)
- Prévisualisation des images
- Suppression d’images sélectionnées
- Barre de progression réelle (%)
- Génération PDF côté serveur
- Téléchargement automatique du PDF

---

## 🛠 Technologies utilisées

### Frontend
- Angular
- TypeScript
- HTML / CSS

### Backend
- Python
- FastAPI
- Pillow (traitement image)
- Uvicorn (serveur ASGI)

---


#  Installation Backend (FastAPI)

### 1️ Aller dans le dossier backend
C:\Users\Worshipper\Documents\Dev\images-to-pdf> 
cd backend

### 2 Créer un environnement virtuel
py -m venv venv

### 3 Activer l'environnement virtuel
venv\Scripts\activate

### 4 Installer les dépendances
Installer les dépendances

### 5 Lancer le serveur FastAPI
py -m uvicorn main:app --reload

# Backend disponible sur :
http://127.0.0.1:8000
# Documentation interactive :
http://127.0.0.1:8000/docs


# Installation Frontend (Angular)
### 1️ Aller dans le dossier images-to-pdf
cd images-to-pdf C:\Users\Worshipper\Documents\Dev\images-to-pdf>

### 2 Installer les dépendances
npm install

### 3 Lancer le serveur Angular
ng serve

# Frontend disponible sur :
http://localhost:4200


# Fonctionnement global

1- L’utilisateur sélectionne ou glisse des images
2- Les images sont prévisualisées côté navigateur
3- Le bouton "Générer le PDF" envoie les images au backend FastAPI
4- Le serveur fusionne les images en PDF
5- Le PDF est renvoyé au frontend
6- Le navigateur télécharge automatiquement le fichier PDF


# API Endpoint
POST /convert

Type : Multipart/Form-Data
Paramètre :
files : List[UploadFile]
Réponse :
Fichier PDF téléchargeable

Auteur

 # Projet réalisé par :

Exaucé Dounga TOHOUN
Étudiant en Génie Logiciel
Projet académique Fullstack Angular + FastAPI

