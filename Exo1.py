import tensorflow as tf
import matplotlib.pyplot as plt
import numpy as np


# Charger le dataset Fashion-MNIST depuis TensorFlow/Keras
fashion_mnist = tf.keras.datasets.fashion_mnist

# Télécharger les ensembles d'entraînement et de test
(train_images, train_labels), (test_images, test_labels) = fashion_mnist.load_data()

# Afficher la forme des ensembles d'entraînement et de test
print(f"Ensemble d'entraînement : {train_images.shape}, {train_labels.shape}")
print(f"Ensemble de test : {test_images.shape}, {test_labels.shape}")

# Normaliser les images
train_images = train_images / 255.0
test_images = test_images / 255.0

# Créer un dictionnaire pour les classes (labels)
class_names = ['T-shirt/top', 'Trouser', 'Pullover', 'Dress', 'Coat',
               'Sandal', 'Shirt', 'Sneaker', 'Bag', 'Ankle boot']

# Afficher les 9 premières images de l'ensemble d'entraînement
plt.figure(figsize=(10, 10))
for i in range(9):
    plt.subplot(3, 3, i + 1)
    plt.xticks([])
    plt.yticks([])
    plt.grid(False)
    plt.imshow(train_images[i], cmap=plt.cm.binary)
    plt.xlabel(class_names[train_labels[i]])
plt.show()


# Reshape des images d'entraînement et de test
train_images = train_images.reshape((train_images.shape[0], 28, 28, 1))
test_images = test_images.reshape((test_images.shape[0], 28, 28, 1))

# Vérification des nouvelles formes des images
print(f"Nouvelle forme des images d'entraînement : {train_images.shape}")
print(f"Nouvelle forme des images de test : {test_images.shape}")

# Afficher une image après reshape pour vérifier
plt.imshow(train_images[0].reshape(28, 28), cmap=plt.cm.binary)
plt.title(f"Label : {train_labels[0]}")
plt.show()


from tensorflow.keras import layers, models

# Initialiser un modèle séquentiel
model = models.Sequential()

# Première couche de convolution et de pooling
model.add(layers.Conv2D(32, (3, 3), activation='relu', input_shape=(28, 28, 1)))
model.add(layers.MaxPooling2D((2, 2)))

# Deuxième couche de convolution et de pooling
model.add(layers.Conv2D(64, (3, 3), activation='relu'))
model.add(layers.MaxPooling2D((2, 2)))

# Troisième couche de convolution et de pooling
model.add(layers.Conv2D(128, (3, 3), activation='relu'))
model.add(layers.MaxPooling2D((2, 2)))

# Aplatir les caractéristiques pour les passer aux couches denses
model.add(layers.Flatten())

# Ajouter une couche dense avec activation ReLU
model.add(layers.Dense(128, activation='relu'))

# Dernière couche avec softmax pour la classification des 10 classes
model.add(layers.Dense(10, activation='softmax'))

# Afficher un résumé du modèle
model.summary()


# Compiler le modèle avec les paramètres clés
model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])


# Entraînement du modèle
history = model.fit(
    train_images,  
    train_labels,  
    epochs=10,     
    batch_size=64, 
    validation_data=(test_images, test_labels),  
    verbose=1      
)

# Évaluation du modèle sur l'ensemble de test
test_loss, test_acc = model.evaluate(test_images, test_labels)

print(f"Précision sur l'ensemble de test : {test_acc:.4f}")



# Fonction pour afficher l'image avec la prédiction et l'étiquette réelle
def plot_image(predictions_array, true_label, img):
    plt.grid(False)
    plt.xticks([])
    plt.yticks([])

    # Afficher l'image
    plt.imshow(img, cmap=plt.cm.binary)

    predicted_label = np.argmax(predictions_array)
    if predicted_label == true_label:
        color = 'blue'
    else:
        color = 'red'

    # Titre avec la prédiction et la véritable étiquette
    plt.xlabel(f"{class_names[predicted_label]} ({class_names[true_label]})", color=color)

# Fonction pour afficher le graphique des prédictions
def plot_value_array(predictions_array, true_label):
    plt.grid(False)
    plt.xticks(range(10), class_names, rotation=45)
    plt.yticks([])
    thisplot = plt.bar(range(10), predictions_array, color="#777777")
    plt.ylim([0, 1])
    predicted_label = np.argmax(predictions_array)

    thisplot[predicted_label].set_color('red')
    thisplot[true_label].set_color('blue')

# Prédictions sur les images de test
predictions = model.predict(test_images)

# Afficher quelques images de test avec leurs prédictions
num_rows = 5
num_cols = 3
num_images = num_rows * num_cols
plt.figure(figsize=(2*2*num_cols, 2*num_rows))
for i in range(num_images):
    plt.subplot(num_rows, 2*num_cols, 2*i+1)
    plot_image(predictions[i], test_labels[i], test_images[i].reshape(28, 28))
    plt.subplot(num_rows, 2*num_cols, 2*i+2)
    plot_value_array(predictions[i], test_labels[i])
plt.tight_layout()
plt.show()
