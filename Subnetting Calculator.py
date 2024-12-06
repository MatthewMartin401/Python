#  Subnetting Calculator
#  Creator: ME

import re

# ip = "179.20.20.0/19"
# ip = "179.20.20.0.255.255.255.0"
# mask = re.search("/[0-9]+", ip)
# if mask == None:
#     submask = ".".join(ip.split(".")[4:])
#     print(submask)

# a = 10 if (30 < 20) else 20
# print(a)


# mask = re.search("/[0-9]+", ip)
# print(mask)
# sub = ".".join(ip.split(".")[4:]) if (mask == None) else mask
# print(sub)


class SubnettingCalculator():
    def __init__(self, ip):
        self.octet = [128, 64, 32, 16, 8, 4, 2, 1]
        mask = re.search("/[0-9]+", ip)  #  Used for the submask
        if mask == None:  # If full submask
            self.submask_octet = self.get_subnetmask_octet(".".join(ip.split(".")[4:]))
            self.host_bits = self.get_slash_notation(self.submask_octet)
        else:  #  If slash notation
            self.submask_octet = self.get_subnetmask_octet(self.slashNotationToFullSubnetMask(mask[0][1:]))
            self.host_bits = mask[0][1:]  #  removes /

        mask2 = re.search("[0-9]+.[0-9]+.[0-9]+.[0-9]+", ip)  # Used for the IP.
        self.ip = mask2[0]
        self.classful_ips = [8, 16, 24]  #  Class A, B, C are classful masks. They are 255.0.0.0, 255.255.0.0, 255.255.255.0
        self.ip_address_classes = [1, 128, 192, 224, 240]  #  Focusing on the first octet. Sorts into different classes. 127 is not included, as its a local host reference.
        self.loopback_address = 127  # Local Host reference number in first octet.

    def slashNotationToFullSubnetMask(self, mask):
        values = []
        for x in range(int(mask) // 8):
            values.append(255)
        
        borrowed = int(mask) % 8

        val = sum(self.octet[:borrowed])

        values.append(val)
        for x in range(4 - len(values)):
            values.append(0)
        
        return ".".join(str(x) for x in values)

    def get_subnetmask_octet(self, ip):
        # print(sum(self.octet))
        subnetmask = [int(x) for x in ip.split(".")]
        # print(subnetmask)
        bit_map = []
        for index, x in enumerate(subnetmask):
            part = []
            for val in self.octet:
                if x >= val:
                    part.append(int(x >= val))
                    x -= val
                else:
                    part.append(int(x >= val))
                # print(x)
            bit_map.append(part)
        return bit_map
    
    def get_slash_notation(self, subnetMaskBits):
        subnetmask = 0
        for list in subnetMaskBits:
            for index, bit in enumerate(list):
                if bit == 1:
                    subnetmask += 1
        return subnetmask

    def borrowed_bits(self):  #  Doesnt currently support Subnet values lower than Class A ( 8 )
        try:
            if int(self.host_bits) <= 8:
                raise ValueError
            for class_ip in self.classful_ips:
                if class_ip <= int(self.host_bits):
                    a = class_ip
            print(f"{int(self.host_bits)} - {a} = {int(self.host_bits) - a}")
            return int(self.host_bits) - a  # ip needs to be the provided IP network bit / subnet mask
        except ValueError:
            print("No borrowed bits.")

    def created_subnetmask(self):  # Gets the number of created subnets.
        bb = self.borrowed_bits()
        if bb == None:
            return 1
        return 2 ** bb
    
    def supported_hosts(self):  #  Gets the number of host bits 
        return 2 ** int(self.host_bits) - 2  #  First and last IP are taken as Broadcast IP and Subnet IP.

    def supported_local_hosts(self):  #  Gets the number of assignable IP addresses.
        return (2**(32 - int(self.host_bits))) - 2
    
    def address_ranges(self):
        full_subnetmask = [255]*(int(self.host_bits) // 8)
        if 8 % int(self.host_bits) != 0 and len(full_subnetmask) != 4:
            full_subnetmask.append((8 % int(self.host_bits)))
        for x in range(4 - len(full_subnetmask)):
            full_subnetmask.append(0)
        return full_subnetmask
    
    def get_interesting_octet(self):
        # full_octet = [[str(i) for i in x] for x in self.submask_octet]
        # full_octet = "a.a.a".split(".")
        # full_octet = [str(x) for x in self.submask_octet]
        # full_octet = [str(x) for x in self.submask_octet]

        full_octet = []
        for i in self.submask_octet:
            for x in i:
                full_octet.append(x)

        # full_octet.append([x for x in [i for i in self.submask_octet]])
        # full_octet.append([[x for x in i] for i in self.submask_octet])
        # full_octet.extend([x for x in [i for i in self.submask_octet]])

        # print(full_octet)
        # print(len(full_octet))

        interesting_index = [ind for ind, val in enumerate(full_octet) if val == 1]  #  Get all of the indexes for the value 1.
        #  Gets the last index for the value 1, and works out which classful IP it belongs to.
        return interesting_index[-1] // 8  #  #  Returns index. if <= 8 = 0; <= 16 = 1; <= 24 = 2; etc

    def IP_address_ranges(self):  #  Currently, it returns the address ranges within the IP class which contains the interesting IP.
        if int(self.host_bits) % 8 == 0:
            block_size = 1
            # print("Default", 8 % int(self.host_bits))
        else:
            block_size = 256 - sum([self.octet[index] for index, i in enumerate(self.submask_octet[self.get_interesting_octet()]) if i == 1])  #  If 1, add to list. Then work out sum. Subtract from 255 to get block size.
            # print("Not Default")
        # print(self.get_interesting_octet())
        # print(block_size, "_", 255 // block_size)

        temp, index = [int(val)for val in self.ip.split(".")], self.get_interesting_octet()  #  Converts IP from string
        ip_ranges = []
        for i in range(0, (255 // block_size) + 1, 1):  #  +1 or it ends too early.
            if temp[index] <= 255:  #  Only returns if the value is less than 255.
                # ip_ranges.append(temp[index])
                # ip_ranges += list(temp)
                print(temp)
                ip_ranges += temp
                temp[index] += (block_size)  # Adds onto class that the interesting octet is in. DON'T KNOW IF THIS IS HOW ITS DONE.

        complete_list = [ip_ranges[x:x+4] for x in range(0, len(ip_ranges)-1, 4)]
        return(complete_list)  #  Currently returning just the ranges, not full IPs.
    


ip = "179.20.20.0/27"
# ip = "179.20.20.0/24"
# ip = "179.20.20.0.192.0.0.0"
# ip = "179.20.20.0.255.255.255.0"

# print( [ x for x in ip.split(".")[4:]] )
# print( [ [ int(x)>int(val) for val in octet ] for x in ip.split(".")[4:]] )

# mask = []
# mask.append( [[ for val in octet if val<x else 0] for x in ip.split(".")[4:]] )
# print(mask)

calc = SubnettingCalculator(ip)
# print(calc.host_bits)
# print(calc.submask_octet)
# print("Borrowed bits: ", calc.borrowed_bits())
# print("Supported hosts: ", calc.supported_hosts())
# print("Number of subnets created:", calc.created_subnetmask())
# print("Assignable IP addresses:", calc.supported_local_hosts())

# print(calc.address_ranges())

print(calc.IP_address_ranges())
print(calc.get_interesting_octet())

# print(calc.borrowed_bits())
# print(calc.created_subnetmask())
# print(calc.address_ranges())
# print("hello"*2)
# print(19 // 8)