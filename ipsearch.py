import ipinfo
access_token = 'e29e6f2c126204'
handler = ipinfo.getHandler(access_token)
ip_address = '1.1.1.1'
def do_req(ip_address):
     details = handler.getDetails(ip_address)
     res="IP地址" + details.ip + "\n城市" + details.city + "\nASN Org:" + details.org + "\n时区" + details.timezone + "\nHostname" + details.hostname

     return res