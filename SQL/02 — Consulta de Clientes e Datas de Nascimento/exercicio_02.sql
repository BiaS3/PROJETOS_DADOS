-- =====================================================
-- Exercício 02 - Consulta de Clientes e Datas de Nascimento
-- =====================================================

-- 2.a) Selecionar CustomerKey, FirstName, EmailAddress e BirthDate

SELECT CustomerKey, FirstName, EmailAddress, BirthDate
FROM DimCustomer;


-- 2.b) Renomear as colunas utilizando ALIAS com AS

SELECT CustomerKey AS Código,
       FirstName AS Nome,
       EmailAddress AS E_mail,
       BirthDate AS Aniversário
FROM DimCustomer;
