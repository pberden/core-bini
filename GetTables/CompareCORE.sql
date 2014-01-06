SELECT TableName, ColumnName
FROM dbc.ColumnsV 
WHERE DataBaseName = 'TAS21B03_CORE'
AND TableName LIKE 'CORE%'
AND ColumnName NOT IN ('TAS_EXTRACTION_DATE', 'TAS_SOURCE_ID') --TAS_EXTRACTION_DATE makes no sense in comparing, TAS_SOURCE_ID is added in python script
ORDER BY TableName
;

SELECT SUBSTRING(TableName from 6 )
FROM dbc.TablesV
WHERE DataBaseName = 'TAS21B03_CORE'
AND TableName LIKE 'CORE%'
ORDER BY TableName
;
