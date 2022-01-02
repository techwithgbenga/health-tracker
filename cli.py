import argparse
from datetime import datetime
from database import init_db, add_log, get_logs
from reports import generate_report
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer

# Ensure VADER lexicon is downloaded
nltk.download('vader_lexicon', quiet=True)
sia = SentimentIntensityAnalyzer()

def log_entry(args):
    init_db()  # Ensure database is set up
    date = datetime.now().strftime('%Y-%m-%d')
    sleep_hours = args.sleep
    exercise_minutes = args.exercise
    water_intake = args.water
    mood_rating = args.mood
    diary = args.diary if args.diary else ""
    
    # Analyze diary entry for sentiment
    sentiment = sia.polarity_scores(diary)['compound'] if diary.strip() else 0.0

    add_log(date, sleep_hours, exercise_minutes, water_intake, mood_rating, diary, sentiment)
    print("Daily log added successfully.")

def view_logs(args):
    logs = get_logs()
    if not logs:
        print("No logs found.")
        return

    for log in logs:
        print(f"ID: {log[0]}, Date: {log[1]}, Sleep: {log[2]}h, Exercise: {log[3]}min, "
              f"Water: {log[4]}L, Mood: {log[5]}, Sentiment: {log[7]:.2f}")
        if log[6]:
            print(f"Diary: {log[6]}")
        print("-" * 40)

def report(args):
    generate_report(period=args.period)

def main():
    parser = argparse.ArgumentParser(description="Health Tracker & Mood Analyzer")
    subparsers = parser.add_subparsers(dest='command')

    # Subparser for logging entry
    parser_log = subparsers.add_parser('log', help="Log today's health metrics")
    parser_log.add_argument('--sleep', type=float, required=True, help="Hours of sleep")
    parser_log.add_argument('--exercise', type=float, required=True, help="Exercise minutes")
    parser_log.add_argument('--water', type=float, required=True, help="Water intake in liters")
    parser_log.add_argument('--mood', type=int, choices=range(1, 11), required=True, help="Mood rating (1-10)")
    parser_log.add_argument('--diary', type=str, default="", help="Optional diary entry for the day")
    parser_log.set_defaults(func=log_entry)

    # Subparser for viewing logs
    parser_view = subparsers.add_parser('view', help="View all health logs")
    parser_view.set_defaults(func=view_logs)

    # Subparser for generating reports
    parser_report = subparsers.add_parser('report', help="Generate health report")
    parser_report.add_argument('--period', default='monthly', help="Report period: daily, weekly, or monthly")
    parser_report.set_defaults(func=report)

    args = parser.parse_args()
    if args.command:
        args.func(args)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
