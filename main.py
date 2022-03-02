from User2 import User
from CuentaBancaria import CuentaBancaria


Violeta= User("Violeta Rojas")
Nancy= User("Nancy Rojas")

# Violeta.cuenta.nueva_tasa(10)
# Nancy.cuenta.nueva_tasa(6)

Violeta.cuenta.hacer_deposito(1000).hacer_deposito(1000).hacer_deposito(1000).hacer_retiro(500).nueva_tasa(5).generar_interes().mostrar_balance_usuario()
Nancy.cuenta.hacer_deposito(1500).hacer_deposito(1500).hacer_retiro(500).hacer_retiro(500).hacer_retiro(500).hacer_retiro(500).generar_interes().mostrar_balance_usuario()


CuentaBancaria.imprimir_cuentas()



# Fabian.cuenta.hacer_deposito(5000).hacer_deposito(1000).hacer_deposito(1000).hacer_retiro(500).mostrar_balance_usuario()
# # Fabian.cuenta.hacer_deposito(1000)
# # Fabian.cuenta.hacer_retiro(500)
# # Fabian.cuenta.mostrar_balance_usuario()


# Roberto.cuenta.hacer_deposito(500).hacer_deposito(1000).hacer_retiro(200).hacer_retiro(200).mostrar_balance_usuario()
# # # Roberto.cuenta.hacer_deposito(500)
# # # Roberto.cuenta.hacer_deposito(1000)
# # # Roberto.cuenta.hacer_retiro(200)
# # # Roberto.cuenta.hacer_retiro(400)
# # # Roberto.cuenta.mostrar_balance_usuario()

# Cristian.cuenta.hacer_deposito(2000).hacer_retiro(100).hacer_retiro(100).hacer_retiro(100).mostrar_balance_usuario()
# # Cristian.cuenta.hacer_deposito(2000)
# # Cristian.cuenta.hacer_retiro (100)
# # Cristian.cuenta.hacer_retiro (100)
# # Cristian.cuenta.hacer_retiro (100)
# # Cristian.cuenta.mostrar_balance_usuario()

# Fabian.cuenta.transfer_dinero(Cristian, 2000).mostrar_balance_usuario()
# # print("Saldo Cristian pre transaccion: ", Cristian.cuenta.balance)
# # Fabian.cuenta.transfer_dinero(Cristian, 2000)
# # Fabian.cuenta.mostrar_balance_usuario()
# # # Cristian.cuenta.mostrar_balance_usuario()

# # print("Saldo Cristian post transaccion: ", Cristian.cuenta.balance)


# Fabian.cuenta.generar_interes()


# john.cuenta.hacer_deposito(1500)
# print(john.cuenta.balance)
# # john.hacer_retiro(100)

# mary.hacer_deposito(100).hacer_deposito(200)

# john.transfer_dinero(mary, 100)

# john.mostrar_balance_usuario()

# print(john.pesos)
# print(mary.pesos)

# cuenta = CuentaBancaria(8, 100)
# cuenta_2 = CuentaBancaria(10, 1000)

# cynthia = User("Cynthia")

# CuentaBancaria.imprimir_cuentas()
