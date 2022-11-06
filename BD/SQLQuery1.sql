SELECT * FROM Produto

SELECT SUM(quantest) AS Soma
FROM Produto

SELECT COUNT(quantest) AS Quantidade
FROM Produto

SELECT SUM(quantest)/COUNT(quantest) AS Média
FROM Produto

SELECT COUNT(quantest) AS Quantidade,
	   SUM(quantest) AS Soma,
	   AVG(quantest) AS Média
FROM Produto

SELECT COUNT(idcliente) as Clientes
FROM Cliente

SELECT COUNT(idpedido) as Pedidos
FROM Pedido
WHERE via = 'A'

SELECT COUNT(email) as Funcionarios
FROM Funcionario

SELECT IDCIDADE FROM Cliente
ORDER BY idcidade

SELECT COUNT(DISTINCT idcidade) FROM Cliente

SELECT COUNT(DISTINCT idvendedor) AS Vendedores
FROM Pedido

SELECT SUM(salario) AS [Total]
FROM funcionario

SELECT * 
FROM Produto

SELECT (venda * quantest)
FROM Produto

SELECT AVG(venda) AS [Preço Médio]
FROM Produto
WHERE idtipo not in (1, 3, 4)

SELECT venda FROM Produto
ORDER BY venda DESC

SELECT MAX(venda) 'Valor máximo'
FROM Produto

SELECT TOP 1 nome, venda 
FROM Produto
ORDER BY venda DESC

SELECT MIN(datafatura) AS [Data]
FROM pedido

SELECT MIN(datanasc)
FROM Funcionario
WHERE sexo = 'M'

SELECT AVG(salario) AS 'Salário médio'
FROM Funcionario
WHERE sexo = 'F'

SELECT sexo, AVG(salario) AS 'Salário médio'
FROM Funcionario
GROUP BY sexo

SELECT idsetor, 
	   COUNT(idfuncionario) AS Funcionarios,
       SUM(salario) AS salario
FROM Funcionario
GROUP BY idsetor

SELECT YEAR(datapedid) AS Ano,
	   MONTH(datapedid) AS Mês,
	   COUNT(*) AS Quant
FROM Pedido
GROUP BY MONTH(datapedid), YEAR(datapedid)

SELECT idpedido, COUNT(*) as Quantidade
FROM Itens
GROUP BY idpedido
HAVING COUNT(*) >= 3

SELECT YEAR(datapedid) AS Ano,
       COUNT(*) as Pedidos
FROM Pedido
GROUP BY YEAR(datapedid)
HAVING COUNT(*) > 100