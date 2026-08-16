-- =====================================================
-- Exercício 01 - Contagem de Clientes e Produtos
-- =====================================================

-- 1.a) Verificar se existem 2.517 produtos cadastrados
-- Resultado: 2.517 linhas

SELECT *
FROM DimProduct;

-- 1.b) Verificar se o número de clientes aumentou ou reduziu
-- Resultado: 18.869 clientes
-- Comparação: 19.500 clientes no mês passado
-- Diferença: redução de 631 clientes

SELECT *
FROM DimCustomer;
