def leaky_bucket(bucket_size, leak_rate, time_units, packets):
    bucket_content = 0

    print("\n--- Leaky Bucket Simulation ---")
    print(f"{'Time':<6}{'Packets Arrived':<18}{'Leaked':<10}{'Dropped':<10}{'Bucket Content'}")
    print("-" * 60)

    for t in range(time_units+1):
        incoming = packets[t] if t < len(packets) else 0
        dropped = 0

        # Step 1: Add incoming packets
        if bucket_content + incoming > bucket_size:
            dropped = (bucket_content + incoming) - bucket_size
            bucket_content = bucket_size
        else:
            bucket_content += incoming

        # Step 2: Leak (send out) packets at a fixed rate
        leaked = min(bucket_content, leak_rate)
        bucket_content -= leaked

        # Display the state at each time unit
        print(f"{t:<6}{incoming:<18}{leaked:<10}{dropped:<10}{bucket_content}")

    print("-" * 60)
    print("Simulation complete.\n")


# Example usage:
if __name__ == "__main__":
    bucket_size = int(input("Enter bucket size (packets): "))
    leak_rate = int(input("Enter leak rate (packets per time unit): "))
    time_units = int(input("Enter total number of time units: "))

    print(f"Enter packets arriving at each time unit (space-separated, {time_units} values):")
    packets = list(map(int, input().split()))

    leaky_bucket(bucket_size, leak_rate, time_units, packets)
