import click
from pip import main



def ips(start, end):
    import socket, struct
    start = struct.unpack('>I', socket.inet_aton(start))[0]
    end = struct.unpack('>I', socket.inet_aton(end))[0]
    return [socket.inet_ntoa(struct.pack('>I', i)) for i in range(start, end)]

@click.command()
@click.option('--ranges','-r',help='Veuillez rentrer une range d\'IP sous la forme"x.x.x.x-y.y.y.y"')

def main(ranges):
    f =open("ip.txt","w")   
    all_ips = []
    all_ranges = []
    all_ranges.append(ranges)
    for one_range in all_ranges:
        ip_in_range = ips(one_range.split("-")[0].replace(" ",""),one_range.split("-")[1].replace(" ","").strip())
        for ip in ip_in_range:
            all_ips.append(ip)
    for ip in all_ips:
        f.write(ip+"\n")
    f.close()

if __name__ == "__main__":
    main()