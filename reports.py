import matplotlib.pyplot as plt
from datetime import datetime
from database import get_logs

def generate_report(period='monthly'):
    logs = get_logs()
    if not logs:
        print("No logs available. Add some data first!")
        return

    dates = []
    mood_ratings = []
    sentiment_scores = []
    sleep_hours = []
    exercise_minutes = []
    water_intakes = []

    for log in logs:
        # Log indices: 0: id, 1: date, 2: sleep_hours, 3: exercise_minutes, 4: water_intake,
        # 5: mood_rating, 6: diary, 7: sentiment
        try:
            log_date = datetime.strptime(log[1], '%Y-%m-%d')
        except Exception as e:
            continue  # skip invalid date formats
        dates.append(log_date)
        mood_ratings.append(log[5])
        sentiment_scores.append(log[7] if log[7] is not None else 0)
        sleep_hours.append(log[2] if log[2] is not None else 0)
        exercise_minutes.append(log[3] if log[3] is not None else 0)
        water_intakes.append(log[4] if log[4] is not None else 0)

    # Plot mood ratings
    plt.figure(figsize=(10, 6))
    plt.plot(dates, mood_ratings, marker='o', label='Mood Rating')
    plt.xlabel('Date')
    plt.ylabel('Mood Rating')
    plt.title(f'Mood Trend ({period.title()})')
    plt.legend()
    plt.grid(True)
    plt.show()

    # Plot sentiment scores
    plt.figure(figsize=(10, 6))
    plt.plot(dates, sentiment_scores, marker='o', color='magenta', label='Diary Sentiment')
    plt.xlabel('Date')
    plt.ylabel('Sentiment Score')
    plt.title(f'Diary Sentiment Trend ({period.title()})')
    plt.legend()
    plt.grid(True)
    plt.show()

    # You can similarly plot other health metrics such as sleep, exercise, and water intake.
