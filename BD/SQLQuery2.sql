SELECT * FROM Cliente

SELECT * FROM Produto
WHERE descricao IS not NULL

SELECT idcliente, nome, fone FROM Cliente

SELECT idpedido, datapedid AS "data do pedido", frete FROM Pedido

SELECT DISTINCT idcliente, datapedid FROM Pedido

SELECT DISTINCT bairro, idreside
FROM Funcionario

SELECT idproduto, quantest, venda,
quantest*venda AS valor
FROM Produto

SELECT nome, idcidade
from Cliente

FROM Cliente
ORDER BY cargo

SELECT idproduto, nome, custo, venda,
venda-custo AS diferença
FROM Produto
WHERE venda-custo > 10
ORDER BY diferença DESC

SELECT idproduto, nome, idtipo
FROM Produto
ORDER BY idtipo ASC, nome DESC

SELECT nome, bairro FROM Funcionario
WHERE bairro IN ('MANAÍRA','BESSA')

SELECT nome, bairro FROM Funcionario
WHERE bairro != 'MANAÍRA' AND bairro != 'BESSA'

SELECT nome, venda
from Produto
WHERE venda >= 30 AND venda <= 50

SELECT nome 
FROM Cliente
WHERE nome LIKE 'A_A%'

SELECT TOP 10 percent NOME, year(datanasc) as ano
FROM Funcionario
order by year(datanasc)