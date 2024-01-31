import ipaddress
import yaml

def generate_yaml_config(num_leaves, dc_name, spine1_p2p_subnet, spine2_p2p_subnet, loopback_subnet):
    spine1_p2p_subnets = list(ipaddress.ip_network(spine1_p2p_subnet).subnets(new_prefix=31))
    spine2_p2p_subnets = list(ipaddress.ip_network(spine2_p2p_subnet).subnets(new_prefix=31))

    config = {
        "global": {
            "spine_ASN": 65000,
            "lo0": loopback_subnet,
            "MTU": 9214
        }
    }

    # Spine Configuration
    for i in range(1, 3):  # Hardcoded for 2 spines
        spine_name = f"{dc_name}-spine{i}"
        spine_ip = str(ipaddress.ip_network(loopback_subnet)[0]) if i == 1 else str(ipaddress.ip_network(loopback_subnet)[-1])
        config[spine_name] = {
            "interfaces": {
                "loopback0": {"ipv4": spine_ip, "mask": 32}
            },
            "BGP": {"ASN": 65000}
        }

        p2p_subnets = spine1_p2p_subnets if i == 1 else spine2_p2p_subnets
        for j in range(num_leaves + 2):  # Including borderleafs
            leaf_ip = str(p2p_subnets[j].network_address)
            config[spine_name]["interfaces"][f"Ethernet{j+1}"] = {"ipv4": leaf_ip, "mask": 31}

    # Leaf and Borderleaf Configuration
    leaf_ASN = 65002
    for i in range(1, num_leaves + 3):  # Including borderleafs
        leaf_name = f"{dc_name}-leaf{i}" if i <= num_leaves else f"{dc_name}-borderleaf{i - num_leaves}"
        leaf_ip = str(ipaddress.ip_network(loopback_subnet)[252 + i - num_leaves]) if i > num_leaves else None
        config[leaf_name] = {
            "interfaces": {
                "loopback0": {"ipv4": leaf_ip, "mask": 32} if leaf_ip else {},
                "Ethernet1": {"ipv4": str(spine1_p2p_subnets[i-1].network_address), "mask": 31},
                "Ethernet2": {"ipv4": str(spine2_p2p_subnets[i-1].network_address), "mask": 31}
            },
            "BGP": {"ASN": leaf_ASN if i <= num_leaves else 65001},
            "MLAG": "Odd" if i % 2 != 0 else "Even"
        }
        if i <= num_leaves: leaf_ASN += 1

    return config

def main():
    dc_name = input("Enter the data center name: ")
    num_leaves = int(input("Enter the number of leaves: "))
    spine1_p2p_subnet = input("Enter the point-to-point subnet for spine1 (e.g., '172.16.80.0/24'): ")
    spine2_p2p_subnet = input("Enter the point-to-point subnet for spine2 (e.g., '172.16.81.0/24'): ")
    loopback_subnet = input("Enter the loopback subnet (e.g., '10.255.255.0/24'): ")

    config = generate_yaml_config(num_leaves, dc_name, spine1_p2p_subnet, spine2_p2p_subnet, loopback_subnet)
    filename = f'{dc_name}_network_config.yaml'
    with open(filename, 'w') as file:
        yaml.dump(config, file, default_flow_style=False, sort_keys=False)

    print(f"Network configuration for {dc_name} generated successfully.")

if __name__ == "__main__":
    main()