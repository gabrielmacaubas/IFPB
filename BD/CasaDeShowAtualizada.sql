
Use [CasaDeShow]
SET DATEFORMAT dmy

CREATE TABLE [Funcionario]
(
    Cpf VARCHAR(14) NOT NULL PRIMARY KEY,
    Cpf_Chefe VARCHAR(14),
    Nome VARCHAR(80) NOT NULL,
    Genero CHAR(1) CHECK(Genero IN ('M','F')),
    Endereco VARCHAR(60)
    
    CONSTRAINT FK_Funcionario_Cpf_chefe FOREIGN KEY (Cpf_Chefe) REFERENCES [Funcionario](Cpf)
)

INSERT INTO [Funcionario]
VALUES(
    '12345678911',
    NULL,
    'Kamila',
    'F',	
    'Av Rua dos Anões'
)

INSERT INTO [Funcionario]
VALUES(
    '543216789',
    NULL,
    'Guilherme Miranda',
    'M',
    'Av Rua Santos'
)

INSERT INTO [Funcionario]
VALUES(
    '54326788',
    NULL,
    'Caio',
    'M',
    'Av Rua Drauzio Varella'
)

INSERT INTO [Funcionario]
VALUES(
    '5432678812',
    NULL,
    'Paulo',
    'M',
    'Av Rua dos Emos'
)

INSERT INTO [Funcionario]
VALUES(
    '08188517402',
    NULL,
    'Leticia',
    'F',
    'Av Rua Bandeirantes'
)

INSERT INTO [Funcionario]
VALUES(
    '987654321',
    '12345678911',
    'Leticia',
    'F',
    'Av Rua Charlie Brown'
)


CREATE TABLE [TelefoneFuncionario]
(
    Numero_telefone VARCHAR(16) NOT NULL PRIMARY KEY,
    Funcionario_Cpf VARCHAR(14) NOT NULL,

    CONSTRAINT FK_Funcionario_Cpf FOREIGN KEY (Funcionario_Cpf) REFERENCES [Funcionario] (Cpf)
)

INSERT INTO [TelefoneFuncionario]
VALUES(
    '(83)98877-6655',
    '54326788'
)

INSERT INTO [TelefoneFuncionario]
VALUES(
    '(83)91235-6789',
    '5432678812'
)

INSERT INTO [TelefoneFuncionario]
VALUES(
    '(83)94356-6535',
    '987654321'
)

INSERT INTO [TelefoneFuncionario]
VALUES(
    '(83)90099-8877',
    '12345678911'
)

INSERT INTO [TelefoneFuncionario]
VALUES(
    '(83)99823-8565',
    '08188517402'
)

CREATE TABLE [EmpregadoPor]
(
    CasaShow_Cnpj VARCHAR(14) NOT NULL,
    Funcionario_Cpf VARCHAR(14) NOT NULL,
    
    CONSTRAINT FK_Funcionario_Cpf_Empregado FOREIGN KEY (Funcionario_Cpf) REFERENCES [Funcionario] (Cpf),

    PRIMARY KEY ([CasaShow_Cnpj], [Funcionario_Cpf]),
)


INSERT INTO [EmpregadoPor]
VALUES(
    '1234567891011',
    '5432678812'
)

INSERT INTO [EmpregadoPor]
VALUES(
    '1234567891011',
    '54326788'
)

INSERT INTO [EmpregadoPor]
VALUES(
    '8987654637281',
    '08188517402'
)

INSERT INTO [EmpregadoPor]
VALUES(
    '1234567891011',
    '12345678911'
)

INSERT INTO [EmpregadoPor]
VALUES(
    '1234567891011',
    '543216789'
)

INSERT INTO [EmpregadoPor]
VALUES(
    '1234567891011',
    '987654321'
)

CREATE TABLE [CasaDeShow]
(
    Cnpj VARCHAR(14) NOT NULL PRIMARY KEY,
    Nome VARCHAR(80) NOT NULL,
    Capacidade INT NOT NULL CHECK(Capacidade > 0 OR Capacidade <= 4000),
    Endereco VARCHAR(60) NOT NULL,
    Telefone VARCHAR(16) NOT NULL,
)

INSERT INTO [CasaDeShow]
VALUES(
    '1234567891011',
    'PH',
    4000,
    'Av Mandacaru',
    '8332357667'
)

INSERT INTO [CasaDeShow]
VALUES(
    '8987654637281',
    'Ponte Preta',
    3500,
    'Av Ponte',
    '8378787878'
)

INSERT INTO [CasaDeShow]
VALUES(
    '988764536253',
    'Miss Mangabeira',
    3000,
    'Av Mangabeira',
    '83988764736'
)

INSERT INTO [CasaDeShow]
VALUES(
    '98765362781',
    'Emos Balada',
    2500,
    'Av dos Emos',
    '83565453627'
)

INSERT INTO [CasaDeShow]
VALUES(
    '123985567878',
    'Balada tal',
    2000,
    'Av Tal',
    '83987656784'
)

CREATE TABLE [Banda]
(
    Cnpj VARCHAR(14) NOT NULL PRIMARY KEY,
    Nome VARCHAR(80) NOT NULL,
    Assessor VARCHAR(80) NOT NULL,
)

INSERT INTO [Banda]
VALUES(
    '1234678911',
    'Gil Bala',
    'Allan Jesus'
)

INSERT INTO [Banda]
VALUES(
    '11987654321',
    'Luva de Pedreiro',
    'Falcão'
)

INSERT INTO [Banda]
VALUES(
    '5647893212',
    'Banda Djavu',
    'João Mourinho'
)

INSERT INTO [Banda]
VALUES(
    '98765432156',
    'Nirvana',
    'Ajs Consultoria'
)

INSERT INTO [Banda]
VALUES(
    '7867656565',
    'Zé Vaqueiro',
    'Whindersson Nunes'
)

CREATE TABLE [Apresenta_Show]
(
    Id int NOT NULL PRIMARY KEY IDENTITY(1,1),
    Data_Apresentacao DATETIME NOT NULL UNIQUE CHECK(Data_Apresentacao > '1900-01-01'),
    Banda_Cnpj VARCHAR(14) NOT NULL,
    Casa_Show_Cnpj VARCHAR(14) NOT NULL, 

    CONSTRAINT FK_Banda_Cnpj FOREIGN KEY (Banda_Cnpj) REFERENCES [Banda](Cnpj),

    CONSTRAINT FK_Casa_Show_Cnpj FOREIGN KEY (Casa_Show_Cnpj) REFERENCES [CasaDeShow](Cnpj)
)


INSERT INTO[Apresenta_Show]
VALUES(
    '04-07-2022',
    '11987654321',
    '8987654637281'
)

INSERT INTO[Apresenta_Show]
VALUES(
    '20-09-2022',
    '98765432156',
    '1234567891011'
)

INSERT INTO[Apresenta_Show]
VALUES(
    '26-06-2022',
    '7867656565',
    '8987654637281'
)

INSERT INTO[Apresenta_Show]
VALUES(
    '22-02-2022',
    '1234678911',
    '8987654637281'
)

INSERT INTO[Apresenta_Show]
VALUES(
    '06-10-2022',
    '5647893212',
    '8987654637281'
)

CREATE TABLE [Telefone_Banda]
(
    Numero_Telefone VARCHAR(16) NOT NULL,
    Banda_Cnpj VARCHAR(14) NOT NULL,

    PRIMARY KEY ([Numero_Telefone], [Banda_Cnpj]),

    CONSTRAINT FK_Contato_Banda_Cnpj FOREIGN KEY (Banda_Cnpj) REFERENCES [Banda] ([Cnpj])
)

SELECT * FROM Telefone_Banda
INSERT INTO[Telefone_Banda]
VALUES(
    '12345678911',
    '1234678911'
)

INSERT INTO[Telefone_Banda]
VALUES(
    '18283923404',
    '98765432156'
)

INSERT INTO[Telefone_Banda]
VALUES(
    '1717171717',
    '5647893212'
)

INSERT INTO[Telefone_Banda]
VALUES(
    '1313131313',
    '7867656565'
)

INSERT INTO[Telefone_Banda]
VALUES(
	'0093213998',
	'11987654321'
)

CREATE TABLE [Patrocinador]
(
    Cnpj VARCHAR(14) NOT NULL PRIMARY KEY,
    Nome VARCHAR(80) NOT NULL,
    Cod_Lista int NOT NULL UNIQUE, 
    Telefone VARCHAR(16)
)

INSERT INTO[Patrocinador]
VALUES(
	'01234567891011',
	'Sportsbet.io',
	'123',
	'(83)91234-5678'
)

INSERT INTO[Patrocinador]
VALUES(
	'12131415161718',
	'Mc Donalds',
	'456',
	'(83)99101-1121'
)

INSERT INTO[Patrocinador]
VALUES(
	'19202122232425',
	'Avon',
	'789',
	'(83)91314-1516'
)

INSERT INTO[Patrocinador]
VALUES(
	'26272829303132',
	'Brahma',
	'101',
	'(83)91718-1920'
)

INSERT INTO[Patrocinador]
VALUES(
	'33343536373839',
	'Adidas',
	'111',
	'(83)92122-2324'
)

CREATE TABLE [Patrocinado_Por]
(
    Patrocinador_Cnpj VARCHAR(14) NOT NULL,
    Apresenta_Show_Id int NOT NULL,

    PRIMARY KEY ([Patrocinador_Cnpj], [Apresenta_Show_Id]),


    CONSTRAINT FK_Apresenta_Show_Id FOREIGN KEY (Apresenta_Show_Id) REFERENCES [Apresenta_Show] ([Id]), 

    CONSTRAINT FK_Patrocinado_Por_Cnpj FOREIGN KEY (Patrocinador_Cnpj) REFERENCES [Patrocinador]([Cnpj])
)

INSERT INTO[Patrocinado_Por]
VALUES(
	'26272829303132',
	'1'
)

INSERT INTO[Patrocinado_Por]
VALUES(
	'26272829303132',
	'2'
)

INSERT INTO[Patrocinado_Por]
VALUES(
	'33343536373839',
	'3'
)

INSERT INTO[Patrocinado_Por]
VALUES(
	'33343536373839',
	'4'
)

INSERT INTO[Patrocinado_Por]
VALUES(
	'12131415161718',
	'5'
)

create table [Convidado]
(
	Codigo int not null,
	Nome varchar(80) DEFAULT('ANONIMO'),
	Patrocinador_Convidado_CNPJ VARCHAR(14) not null,
	Telefone varchar(16) not null

	CONSTRAINT FK_Patrocinado_Convidado_CNPJ FOREIGN KEY (Patrocinador_Convidado_CNPJ) REFERENCES [Patrocinador]([Cnpj])
)

INSERT INTO[Convidado]
VALUES(
	'123',
	'Virginia Fonseca',
	'01234567891011',
	'(83)98371-2833'
)

INSERT INTO[Convidado]
VALUES(
	'123',
	DEFAULT,
	'12131415161718',
	'(83)91233-7832'
)

INSERT INTO[Convidado]
VALUES(
	'456',
	DEFAULT,
	'19202122232425',
	'(83)99234-7987'
)

INSERT INTO[Convidado]
VALUES(
	'456',
	'Léo Dias',
	'19202122232425',
	'(83)99234-7987'
)

INSERT INTO[Convidado]
VALUES(
	'456',
	'Carlinhos Maia',
	'26272829303132',
	'(83)98239-0871'
)


create table [Radio]
(
	Cnpj VARCHAR(14) not null,
	Razao_Social varchar(80) not null,
	Telefone varchar(16) not null,
	Nome_Responsavel varchar(45) not null,
	Frequencia int not null,

	PRIMARY KEY ([Cnpj])
	
)

INSERT INTO[Radio]
VALUES(
	'82391238812132',
	'Jovem Pan Esportes',
	'(18)3702-2353',
	'Thiago Asmar',
	91
)

INSERT INTO[Radio]
VALUES(
	'92812038183973',
	'Cruzeiro Sportes',
	'(31)9048-3889',
	'Diogo Medeiros',
	92
)

INSERT INTO[Radio]
VALUES(
	'94847828103114',
	'Arapuan',
	'(83)3241-9000',
	'Carlos Melo',
	93
)

INSERT INTO[Radio]
VALUES(
	'09219382848193',
	'Mix',
	'(83)9480-1832',
	'Letícia Benício ',
	94
)

INSERT INTO[Radio]
VALUES(
	'49284921921944',
	'Correio',
	'(83)0932-3219',
	'Roberto Júnior ',
	95
)


create table[Tv]
(
	Cnpj VARCHAR(14) not null,
	Razao_Social varchar(80) not null,
	Telefone varchar(16) not null,
	Nome_Responsavel varchar(45) not null,
	numero int not null,

	PRIMARY KEY ([Cnpj])
)

INSERT INTO[Tv]
VALUES(
	'17238038485477',
	'Globo',
	'(22)2771-1854',
	'Roberto Marinho',
	7
)

INSERT INTO[Tv]
VALUES(
	'83912399213893',
	'Sbt',
	'(21)4002-8922',
	'Silvio Santos',
	6
)

INSERT INTO[Tv]
VALUES(
	'09381847182394',
	'Band',
	'(83)98132-9321',
	'João Jorge',
	10
)

INSERT INTO[Tv]
VALUES(
	'84747183122411',
	'Record',
	'(83)6732-8478',
	'Paulo Machado',
	12
)

INSERT INTO[Tv]
VALUES(
	'01829384891784',
	'Mtv',
	'(11)3003-2819',
	'Paulo Machado',
	85
)

create table [PossuiCobertura]
(
	Apresenta_Show_Id int not null,
	Radio_CNPJ VARCHAR(14) null,
	Tv_CNPJ VARCHAR(14) null,

	primary key ([Apresenta_Show_Id]),

	CONSTRAINT FK_Apresenta_Show_Id_Cobertura FOREIGN KEY (Apresenta_Show_Id) REFERENCES [Apresenta_Show]([Id]),
	CONSTRAINT FK_Radio_CNPJ FOREIGN KEY (Radio_CNPJ) REFERENCES [Radio]([Cnpj]),
	CONSTRAINT FK_Tv_CNPJ FOREIGN KEY (Tv_CNPJ) REFERENCES [Tv]([Cnpj])
)

INSERT INTO[PossuiCobertura]
VALUES(
	'5',
	'82391238812132',
	NULL
)

INSERT INTO[PossuiCobertura]
VALUES(
	'4',
	'92812038183973',
	NULL
)

INSERT INTO[PossuiCobertura]
VALUES(
	'3',
	NULL,
	'17238038485477'
)

INSERT INTO[PossuiCobertura]
VALUES(
	'2',
	NULL,
	'83912399213893'
)

INSERT INTO[PossuiCobertura]
VALUES(
	'1',
	NULL,
	'01829384891784'
)

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