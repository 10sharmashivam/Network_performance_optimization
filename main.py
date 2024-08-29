from src.data_collection.traffic_collector import collect_network_traffic
from src.data_collection.performance_metrics import get_snmp_data
from src.data_storage.database import add_metric
from src.data_storage.log_manager import log_info, log_error
from src.analysis.traffic_analysis import analyze_traffic
from src.analysis.bottleneck_identification import identify_bottlenecks
from src.optimization.recommendations import generate_recommendations
from src.optimization.automated_actions import apply_configuration_change
from src.reporting.visualization import create_dashboard
from src.reporting.alerts import send_alert

def main():
    # Data Collection
    interface = 'en0'  # Updated to the correct interface name
    count = 100
    packets = collect_network_traffic(interface, count)
    metrics = {'latency': 120}  # Example metrics

    # Data Storage
    add_metric('latency', metrics['latency'])
    log_info('Data collected and stored successfully.')

    # Analysis
    community = 'public'       # Example SNMP community string
    host = '192.168.1.1'      # Example SNMP host IP
    port = 161                # Example SNMP port
    oid = '1.3.6.1.2.1.1.1.0' # Example OID for system description

    # Call get_snmp_data directly without asyncio
    snmp_data = get_snmp_data(community, host, port, oid)
    print(f'SNMP Data: {snmp_data}')
    
    analyze_traffic(packets)
    bottleneck_status = identify_bottlenecks(metrics)
    log_info(f'Bottleneck status: {bottleneck_status}')

    # Optimization
    recommendations = generate_recommendations(metrics)
    apply_configuration_change('increase_bandwidth')
    log_info(f'Recommendations: {recommendations}')

    # Reporting
    image_paths = [
        'images/network_performance_plot.png',  # Example image path
        # Add paths to other images if applicable
    ]
    create_dashboard({'time': [1, 2, 3], 'value': [10, 20, 15]}, image_paths)
    send_alert('recipient@example.com', 'Network Alert', 'High latency detected.')

if __name__ == "__main__":
    main()