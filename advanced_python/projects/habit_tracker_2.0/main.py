# Contains the main entry point for the Habit Tracker application.

# Import all necessary functions from modules
from habit_engine.__init__ import __version__, __app_name__, __copyright__
from habit_engine.habit_setup import setup_habits
from habit_engine.habit_io import (
    load_habits,
    save_habits,
    load_habit_streaks,
    load_daily_logs,
    save_daily_logs,
    initialize_data_files,
    make_files_writable,
    make_files_readonly,
    reset_app_data,
    clear_tracking_data
)
from habit_engine.habit_logic import (
    update_streaks,
    log_habits
)
from habit_engine.habit_display import (
    display_logs,
    display_app_info
)
from habit_engine.habit_visualization import visualize_habit_streak
import sys

def debug_print(message):
    print(f"[DEBUG]: {message}")

def handle_program_exit(exit_code=0, message=None):
    """Handle program exit with optional message."""
    if message:
        print(message)
    sys.exit(exit_code)

debug_print(f"{__app_name__} v{__version__} is running...")
debug_print(f"{__copyright__}")

if __name__ == "__main__": 
    try:
        # Initialize data storage
        if not initialize_data_files():
            handle_program_exit(1, "\nError: Failed to initialize data storage")
            
        # Load habits and streaks
        habits = load_habits()
        habit_streaks = load_habit_streaks()
        daily_logs = load_daily_logs()

        # Update streaks based on existing logs
        if daily_logs:
            update_streaks(daily_logs, habits, habit_streaks)
        
        # Handle command line arguments
        if len(sys.argv) > 1:
            if sys.argv[1] in ['-v-logs', '--view-logs']:
                display_logs(daily_logs, habit_streaks)
                handle_program_exit()
            elif sys.argv[1] in ['-c-logs', '--clear-logs']:
                if clear_tracking_data():
                    handle_program_exit(message="\nAll tracking data (logs, streaks, and plots) cleared successfully!")
                handle_program_exit(1, "\nError: Failed to clear tracking data")
            elif sys.argv[1] in ['-r', '--reset']:
                if reset_app_data():
                    handle_program_exit(message="\nProgram has been reset. All data and plots cleared. Run without arguments to start fresh.")
                handle_program_exit(1, "\nError: Failed to reset program data")
            elif sys.argv[1] in ['-i', '--info']:
                display_app_info()
                handle_program_exit()
            elif sys.argv[1] in ['--dev']:
                if make_files_writable():
                    handle_program_exit(message="\nCore files are now writable for development.")
                handle_program_exit(1, "\nError: Failed to make files writable")
            elif sys.argv[1] in ['--lock']:
                if make_files_readonly():
                    handle_program_exit(message="\nCore files are now read-only and protected.")
                handle_program_exit(1, "\nError: Failed to make files read-only")
            elif sys.argv[1] in ['-p', '--plot']:
                if not habits:
                    handle_program_exit(1, "\nNo habits found. Please set up habits first.")
                print("\nAvailable habits:")
                for i, habit in enumerate(habits, 1):
                    print(f"{i}. {habit}")
                try:
                    choice = input("\nEnter the number of the habit to visualize: ").strip()
                    idx = int(choice) - 1
                    if 0 <= idx < len(habits):
                        if visualize_habit_streak(daily_logs, habits[idx]):
                            handle_program_exit(message="\nVisualization created successfully!")
                    else:
                        handle_program_exit(1, "\nInvalid habit number selected.")
                except (ValueError, IndexError):
                    handle_program_exit(1, "\nInvalid input. Please enter a valid number.")
                handle_program_exit(1, "\nFailed to create visualization.")
            else:
                print("Invalid option. Use:")
                print("  -i or --info to display application information")
                print("  -v-logs or --view-logs to view logs")
                print("  -c-logs or --clear-logs to clear all logs")
                print("  -r or --reset to reset everything (habits, logs, and streaks)")
                print("  -p or --plot to visualize habit streaks")
                print("  --dev to make core files writable for development")
                print("  --lock to make core files read-only again")
                handle_program_exit(1)
        
        # Regular program flow - check if habits need to be set up
        if not habits:
            print("No habits found! Let's set up your daily habits first.")
            habits = setup_habits()
            if not habits:  # If setup was cancelled or failed
                handle_program_exit(1, "\nError: Failed to set up habits")
                
            if save_habits(habits):
                print("\nHabits saved successfully!")
            else:
                handle_program_exit(1, "\nError: Failed to save habits")

        # Normal daily check-in flow
        new_logs = log_habits(habits)
        if not new_logs:  # If logging was cancelled or failed
            handle_program_exit(1, "\nHabit logging cancelled or failed")
            
        daily_logs.extend(new_logs)
        update_streaks(daily_logs, habits, habit_streaks)
        
        if save_daily_logs(daily_logs, habit_streaks):
            print("\nToday's logs have been recorded successfully!")
            display_logs(daily_logs, habit_streaks)
        else:
            handle_program_exit(1, "\nError: Failed to save logs")
            
    except KeyboardInterrupt:
        handle_program_exit(message="\nProgram interrupted by user.")
    except Exception as e:
        handle_program_exit(1, f"\nUnexpected error: {str(e)}")