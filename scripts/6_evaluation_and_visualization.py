# Script 6: Evaluation and Visualization
import matplotlib.pyplot as plt
import numpy as np

def plot_training_curves(history):
    plt.figure(figsize=(12, 6))
    plt.subplot(1, 2, 1)
    plt.plot(history.history['accuracy'], label='Training Accuracy')
    plt.plot(history.history['val_accuracy'], label='Validation Accuracy')
    plt.xlabel('Epochs')
    plt.ylabel('Accuracy')
    plt.title('Training and Validation Accuracy')
    plt.legend()
    plt.grid(True)

    best_epoch = np.argmax(history.history['val_accuracy'])
    plt.annotate(f"Best Epoch: {best_epoch+1}",
                 (best_epoch, history.history['val_accuracy'][best_epoch]),
                 xytext=(best_epoch+1, history.history['val_accuracy'][best_epoch]+0.05),
                 arrowprops=dict(facecolor='black', arrowstyle='->'))

    plt.subplot(1, 2, 2)
    plt.plot(history.history['loss'], label='Training Loss')
    plt.plot(history.history['val_loss'], label='Validation Loss')
    plt.xlabel('Epochs')
    plt.ylabel('Loss')
    plt.title('Training and Validation Loss')
    plt.legend()
    plt.grid(True)

    plt.tight_layout()
    plt.show()

# Example usage (assuming X_test, y_test, model, and history from previous scripts):
# test_loss, test_acc = model.evaluate(X_test, y_test)
# print(f"Test Accuracy: {test_acc:.3f}, Test Loss: {test_loss:.3f}")

# plot_training_curves(history)
