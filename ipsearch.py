import ipinfo
access_token = 'e29e6f2c126204'
handler = ipinfo.getHandler(access_token)
ip_address = '1.1.1.1'
def do_req(ip_address):
     details = handler.getDetails(ip_address)

     return details.ip, details.city, details.org, details.timezone, details.hostname