fechas_pago = ("ene/25","may/25","dic/25","feb/26","abr/26","may/26","nov/26","dic/26","may/27")

# meses_pago = []
# for mes in fechas_pago:
#     for c in mes:
#         if c.isalpha():
#             ''.join(c)

            

# print(meses_pago)            
            

meses_pago = [ ''.join(c for c in mes if c.isalpha()) for mes in fechas_pago ]

print(meses_pago)