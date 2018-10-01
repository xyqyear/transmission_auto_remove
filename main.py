# -*- encoding:utf-8 -*-

import transmissionrpc

ip_address = '192.168.10.125'
port = 9091
username = ''
password = ''

def main():
    if username and password:
        client = transmissionrpc.Client(ip_address, port, username, password)
    else:
        client = transmissionrpc.Client(ip_address, port)
    for torrent in client.get_torrents():
        if torrent.status == 'stopped':
            client.remove_torrent(torrent.id)
            print('{} removed'.format(torrent.id))

if __name__ == '__main__':
    main()