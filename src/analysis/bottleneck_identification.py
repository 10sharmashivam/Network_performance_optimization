def identify_bottlenecks(metrics):
    """Identify performance bottlenecks based on metrics."""
    if metrics['latency'] > 100:
        return 'High Latency Detected'
    return 'No Bottleneck'

if __name__ == "__main__":
    # Example usage
    metrics = {'latency': 120}
    print(identify_bottlenecks(metrics))