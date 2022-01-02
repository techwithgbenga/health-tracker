# Health Tracker & Mood Analyzer

A command-line Python application to track your daily health metrics and mood. Log your sleep, exercise, water intake, and mood, along with an optional diary entry that is analyzed for sentiment. Generate visual reports to monitor your trends over time.

## Features

- **Daily Logging:** Record sleep hours, exercise minutes, water intake, and mood rating.
- **Diary Analysis:** Optional diary entries analyzed using VADER sentiment analysis.
- **SQLite Database:** Data is stored locally for easy retrieval.
- **Reporting:** Visualize mood trends and other metrics with matplotlib.
- **CLI Interface:** Easy-to-use commands for logging data and generating reports.

---

## Setup & Installation

1. **Clone the Repository:**

```bash
   git clone https://github.com/yourusername/health_tracker.git
   cd health-tracker
```
2. **Install Dependencies:**
```bash
pip install -r requirements.txt
```

3. **Usage:**
- To log a new entry:
```bash
python health_tracker.py log --sleep 7.5 --exercise 45 --water 2.0 --mood 8 --diary "Felt great after the workout."
```

- To view logs:

```bash
python health_tracker.py view
```

- To generate a monthly report:
```bash
python health_tracker.py report --period monthly
```

---

## Future Enhancements
- Develop a web-based dashboard for live visualization.
- Add options for editing and deleting logs.
- Integrate notifications or reminders.
- Pull requests and contributions are welcome!


---

## Summary

The **Health Tracker & Mood Analyzer** is a complete Python project that assists users in tracking key health metrics and monitoring their mood over time. With a modular design, simple CLI commands, local data persistence, and visual reporting, this project makes it easier to understand and improve your daily well-being.

Would you like to add or modify any features, or need further adjustments to this project?



