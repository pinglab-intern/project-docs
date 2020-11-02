"""
Link to reference card for cypher:
https://neo4j.com/docs/cypher-refcard/current/
Cypher style guide:
https://neo4j.com/developer/cypher/style-guide/
"""

"""
#10.20.20 
"""
"""Tables:"""
MATCH path=(g:Gene)--(d:Disease) RETURN g.name,count(d.name) LIMIT 100
#lists 100 genes and number of relationships with diseases in table form
MATCH path=(g:Gene)--(d:Disease) RETURN DISTINCT g.name,count(DISTINCT d.name),collect(DISTINCT d.name) LIMIT 100
#lists 100 genes, number of relationships with diseases, and disease names in table form, similar to above
MATCH (d:Disease)--(g:Gene) RETURN DISTINCT d.name,count(DISTINCT g.name),collect(DISTINCT g.name) LIMIT 100
#lists 100 diseases, number of related genes, and lists disease names in table form, opposite relationship b/w gene and disease compared to above
MATCH path=(p:Pathway)--(g:Gene)--(d:Disease) RETURN p.name, count(g.name), count(d.name) LIMIT 100
#lists 100 pathways and number of related genes and diseases in table form; number of genes=number of diseases
"""Graphs:"""
CALL db.schema()
#Shows the data model metagraph for Hetionet
MATCH path=(g:Gene)--(d:Disease) RETURN path LIMIT 100
#Shows the relationships b/w 100 genes and 2 diseases in a graph
