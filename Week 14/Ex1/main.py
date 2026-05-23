import counter, auth, shop

auth.login('Alisher')
auth.login('Sevara')
shop.buy('Alisher', 'book')
shop.buy('Sevara', 'phone')
shop.buy('Alisher', 'pen')

print(f'Total visits: counter.get_count()')