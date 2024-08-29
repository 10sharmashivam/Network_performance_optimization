from pysnmp.hlapi import bulkCmd, ObjectType, ObjectIdentity, SnmpEngine, CommunityData, UdpTransportTarget, ContextData, SnmpEngine

def get_snmp_data(community, host, port, oid):
    try:
        # Define the SNMP engine and community
        engine = SnmpEngine()
        community_data = CommunityData(community)
        transport_target = UdpTransportTarget((host, port))
        context_data = ContextData()
        
        # Create a list to store SNMP data
        snmp_data = []

        # Execute the SNMP GETBULK command
        iterator = bulkCmd(
            engine,
            community_data,
            transport_target,
            context_data,
            0, 25,  # Set non-repeaters and max-repetitions
            ObjectType(ObjectIdentity(oid))
        )

        # Process the results
        for errorIndication, errorStatus, errorIndex, varBinds in iterator:
            if errorIndication:
                print(f"Error: {errorIndication}")
                return []
            elif errorStatus:
                print(f"Error: {errorStatus.prettyPrint()}")
                return []
            else:
                for varBind in varBinds:
                    snmp_data.append(' = '.join([x.prettyPrint() for x in varBind]))
        
        return snmp_data
    except Exception as e:
        print(f"Exception occurred: {e}")
        return []