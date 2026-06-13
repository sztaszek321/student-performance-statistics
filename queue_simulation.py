import numpy as np
import pandas as pd


def simulate_ticket_machine(
    simulation_time,
    mean_interarrival_time,
    service_min,
    service_mode,
    service_max,
    seed=None,
):
    rng = np.random.default_rng(seed)

    time = 0
    last_event_time = 0
    queue = []
    server_busy = False

    next_arrival = rng.exponential(mean_interarrival_time)
    next_departure = np.inf

    waiting_times = []
    queue_area = 0
    busy_area = 0
    served_passengers = 0
    max_queue_length = 0

    while True:
        next_event_time = min(next_arrival, next_departure)

        if next_event_time > simulation_time:
            time_delta = simulation_time - last_event_time
            queue_area += len(queue) * time_delta

            if server_busy:
                busy_area += time_delta

            break

        time = next_event_time
        time_delta = time - last_event_time

        queue_area += len(queue) * time_delta

        if server_busy:
            busy_area += time_delta

        last_event_time = time

        if next_arrival <= next_departure:
            next_arrival = time + rng.exponential(mean_interarrival_time)

            if not server_busy:
                server_busy = True
                waiting_times.append(0)
                service_time = rng.triangular(service_min, service_mode, service_max)
                next_departure = time + service_time
            else:
                queue.append(time)
                max_queue_length = max(max_queue_length, len(queue))
        else:
            served_passengers += 1

            if len(queue) > 0:
                arrival_time = queue.pop(0)
                waiting_time = time - arrival_time
                waiting_times.append(waiting_time)
                service_time = rng.triangular(service_min, service_mode, service_max)
                next_departure = time + service_time
            else:
                server_busy = False
                next_departure = np.inf

    mean_waiting_time = np.mean(waiting_times) if waiting_times else 0
    max_waiting_time = np.max(waiting_times) if waiting_times else 0

    return {
        "served_passengers": served_passengers,
        "mean_waiting_time": mean_waiting_time,
        "max_waiting_time": max_waiting_time,
        "mean_queue_length": queue_area / simulation_time,
        "max_queue_length": max_queue_length,
        "server_utilization": busy_area / simulation_time,
        "passengers_left_in_queue": len(queue),
    }


def run_simulation_experiments(
    repetitions,
    simulation_time,
    mean_interarrival_time,
    service_min,
    service_mode,
    service_max,
):
    results = []

    for i in range(repetitions):
        result = simulate_ticket_machine(
            simulation_time=simulation_time,
            mean_interarrival_time=mean_interarrival_time,
            service_min=service_min,
            service_mode=service_mode,
            service_max=service_max,
            seed=i,
        )
        result["simulation_number"] = i + 1
        results.append(result)

    columns = ["simulation_number"] + [
        column for column in results[0].keys() if column != "simulation_number"
    ]
    return pd.DataFrame(results)[columns]


def summarize_simulation_results(results):
    columns = [
        "served_passengers",
        "mean_waiting_time",
        "max_waiting_time",
        "mean_queue_length",
        "max_queue_length",
        "server_utilization",
        "passengers_left_in_queue",
    ]

    return results[columns].describe().round(3)


def plot_mean_waiting_time_histogram(results, bins=15):
    import matplotlib.pyplot as plt

    ax = results["mean_waiting_time"].hist(bins=bins)
    ax.set_title("Rozkład średniego czasu oczekiwania")
    ax.set_xlabel("Średni czas oczekiwania [min]")
    ax.set_ylabel("Liczba symulacji")
    plt.show()