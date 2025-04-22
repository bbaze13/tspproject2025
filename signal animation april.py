import time

signal_timing = [
    {'phase': 'East-West Through', 'duration': 34},
    {'phase': 'East-West Through Yellow', 'duration': 3.8},
    {'phase': 'East-West Through Red Clearance', 'duration': 2.2},
    {'phase': 'North-South Left', 'duration': 5},
    {'phase': 'North-South Left Yellow', 'duration': 3.6},
    {'phase': 'North-South Left Red Clearance', 'duration': 1.2},
    {'phase': 'North-South Through', 'duration': 34.5},
    {'phase': 'North-South Through Yellow', 'duration': 3.6},
    {'phase': 'North-South Through Red Clearance', 'duration': 1.9},
    {'phase': 'East-West Left', 'duration': 5},
    {'phase': 'East-West Left Yellow', 'duration': 3.8},
    {'phase': 'East-West Left Red Clearance', 'duration': 1.2},
]

# Run the signal timing plan for 3 cycles
for cycle in range(3):
    print(f"\n--- Starting Cycle {cycle + 1} ---\n")
    
    current_time = 0  # Reset the current time for each cycle

    # Iterate over each phase and update the timer
    for phase in signal_timing:
        print(f"Phase: {phase['phase']}")
        
        # Reset the current time at the start of each phase
        phase_current_time = 0

        # Simulate the passing of time for each phase in seconds
        for second in range(int(phase['duration'])):
            phase_current_time += 1
            current_time += 1
            # Print current time and elapsed time during each second
            print(f"Phase Current Time: {phase_current_time} seconds | Total Elapsed Time: {current_time} seconds")
            time.sleep(1)  # Sleep for 1 second to simulate real-time update

        # Handle the remaining fraction of the duration (if phase duration is not an integer)
        remaining_time = phase['duration'] - int(phase['duration'])
        if remaining_time > 0:
            phase_current_time += remaining_time
            current_time += remaining_time
            print(f"Phase Current Time: {phase_current_time:.1f} seconds | Total Elapsed Time: {current_time:.1f} seconds")
            time.sleep(remaining_time)  # Sleep for the remaining fraction of the time

        print(f"Total Elapsed Time after {phase['phase']}: {current_time} seconds\n")

    print(f"--- Cycle {cycle + 1} Complete ---\n")
