import cv2
import numpy as np
from jsonargparse import CLI


def plot_hist(frame: np.ndarray) -> np.ndarray:
    """Plot brightness histogram."""

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Calculate histogram
    hist = cv2.calcHist([gray], [0], None, [256], [0, 256])
    hist_normalized = hist / hist.max()
    
    # Pright histogram
    hist_image = np.zeros((300, 256, 3), dtype=np.uint8)
    for i in range(255):
        cv2.line(hist_image, 
                (i, 300 - int(hist_normalized[i] * 300)),
                (i + 1, 300 - int(hist_normalized[i + 1] * 300)),
                (255, 255, 255), 1)
        
    return hist_normalized, hist_image


def update_moving_average(sliding_window: list, hist: np.ndarray):
    """Updates MA for brightness sliding window."""

    if len(sliding_window) >= 5:
        sliding_window = sliding_window[1:]

    sliding_window.append(hist)
    moving_average = np.hstack(sliding_window).mean(axis=1)

    brightness = np.argmax(moving_average)
    return sliding_window, brightness


def main(warning_limit: int=255):
    """Main function"""
    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        print("Ошибка: Не удалось открыть камеру")
        exit()

    print("Нажмите 'q' для выхода")

    sliding_window = []

    while True:
        ret, frame = cap.read()
        
        if not ret:
            print("Ошибка: Не удалось получить кадр")
            break
        
        # Get brightess histogram
        hist_normalized, hist_image = plot_hist(frame)

        # Update brightess MA
        sliding_window, brightness = update_moving_average(sliding_window, hist_normalized)

        # Pright info on an image
        cv2.putText(frame, f"Brightness: {brightness}", (100, 100), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255))
        if brightness > warning_limit:
            cv2.putText(frame, f"Warning! brightness is too high ({brightness} > {warning_limit})", (100, 50), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255))

        cv2.imshow('Original', frame)
        cv2.imshow('Histogram', hist_image)
        
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Release recources
    cap.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    CLI(main, as_positional=False)