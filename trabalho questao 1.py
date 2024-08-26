print ('Bem vindo à loja do Leon Santiago Gomes!')
valueOrder = float(input('Insira o valor do pedido:')) #valorDoPedido
installmentNo = int(input('Insira a quantidade de parcelas:')) #quantidadeParcelas

#juros
if installmentNo < 4:
    taxes = 0 #juros
    installmentValue = (valueOrder * (1 + taxes)) / installmentNo #valorDaParcela = valorDoPedido * (1+ juros) / quantidadeParcelas

elif installmentNo >= 4 and installmentNo < 6:
    taxes = (4 / 100)
    installmentValue = (valueOrder * (1 + taxes)) / installmentNo

elif installmentNo >= 6 and installmentNo < 9:
    taxes = (8 / 100)
    installmentValue = (valueOrder * (1 + taxes)) / installmentNo

elif installmentNo >= 9 and installmentNo < 13:
    taxes = (16 / 100)
    installmentValue = (valueOrder * (1 + taxes)) / installmentNo

else: #installmentNo >=13
    taxes = (32 / 100) 
    installmentValue = (valueOrder * (1 + taxes)) / installmentNo

receipt = (installmentValue * installmentNo) #valorTotalParcelado = valorDaParcela * quantidadeParcelas
print (f'O valor das parcelas é de: R${installmentValue}')
print (f'O valor total parcelado é de: R${receipt}')