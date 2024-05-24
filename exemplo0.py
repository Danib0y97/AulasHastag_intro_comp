vendas_pessoa = 900

vendas_empresa = 100000

meta_pessoa = 1000

meta_empresa = 12000 

bonus = 0 

if vendas_pessoa > meta_pessoa and vendas_empresa > meta_empresa:
 bonus = 250 

else: 

 bonus = 50

if vendas_empresa < meta_empresa: 
  bonus = 0 
 
print(bonus) 