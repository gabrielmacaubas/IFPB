SELECT * FROM Funcionario
WHERE Genero IN ('F')

SELECT * FROM CasaDeShow
WHERE Capacidade BETWEEN 3000 AND 4000

SELECT * FROM Funcionario
WHERE Cpf_Chefe IS NULL

SELECT * FROM CasaDeShow
WHERE nome LIKE 'P%'

SELECT * FROM Apresenta_Show
ORDER BY Data_Apresentacao

SELECT COUNT(Nome) as Anonimos
FROM Convidado
WHERE Nome='ANONIMO'

SELECT MAX(Capacidade) as Capacidade
FROM CasaDeShow

SELECT CasaShow_Cnpj AS [CNPJ CASA SHOW], 
Funcionario_Cpf AS [CPF FUNCIONARIO]
FROM EmpregadoPor
GROUP BY CasaShow_Cnpj, Funcionario_Cpf
HAVING Funcionario_Cpf IS NOT NULL

SELECT Banda.Nome, Telefone_Banda.Numero_Telefone
FROM Telefone_Banda
INNER JOIN Banda
ON Banda.Cnpj = Telefone_Banda.Banda_CNPJ	
ORDER BY Banda.Nome