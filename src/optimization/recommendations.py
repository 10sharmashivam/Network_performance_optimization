def generate_recommendations(metrics):
    """Generate recommendations for network optimization."""
    if metrics['latency'] > 100:
        return 'Consider increasing bandwidth'
    return 'Network performance is optimal'

if __name__ == "__main__":
    # Example usage
    metrics = {'latency': 120}
    print(generate_recommendations(metrics))