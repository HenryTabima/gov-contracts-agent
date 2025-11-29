import requests
import json

def search_contracts(query: str, min_budget: int = 0, max_budget: int = 10000000000, department: str = None):
    """
    Searches for government contracts in Colombia (SECOP II) based on a query and optional filters.
    
    Args:
        query (str): Keywords to search for in the contract description.
        min_budget (int): Minimum budget for the contract.
        max_budget (int): Maximum budget for the contract.
        department (str): Department to filter by (e.g., "Valle del Cauca", "Bogotá D.C.").
    
    Returns:
        str: A JSON string containing the list of found contracts.
    """
    print(f"\n[Tool Call] Searching contracts: query='{query}', budget={min_budget}-{max_budget}, department='{department}'")
    
    contract_url = "https://www.datos.gov.co/resource/p6dx-8zbt.json"
    
    # Construct the SQL-like query for the Socrata API
    where_clause = f"estado_de_apertura_del_proceso = 'Abierto' AND precio_base >= {min_budget} AND precio_base <= {max_budget}"
    
    if department:
        where_clause += f" AND departamento_entidad = '{department}'"
    
    # Add keyword search
    if query:
        keywords = query.split()
        keyword_clauses = []
        for keyword in keywords:
            keyword_clauses.append(f"descripci_n_del_procedimiento LIKE '%{keyword}%'")
        
        if keyword_clauses:
            where_clause += f" AND ({' OR '.join(keyword_clauses)})"

    params = {
        "$where": where_clause,
        "$select": "codigo_entidad, id_del_proceso, nombre_del_procedimiento, descripci_n_del_procedimiento, fase, precio_base, modalidad_de_contratacion, estado_del_procedimiento, urlproceso, departamento_entidad, ciudad_entidad",
        "$limit": 5
    }
    
    try:
        response = requests.get(contract_url, params=params)
        response.raise_for_status()
        contracts = response.json()
        
        if not contracts:
            return "No contracts found matching the criteria."
            
        # Simplify the output for the LLM
        simplified_contracts = []
        for c in contracts:
            simplified_contracts.append({
                "id": c.get("id_del_proceso"),
                "description": c.get("descripci_n_del_procedimiento"),
                "price": c.get("precio_base"),
                "department": c.get("departamento_entidad"),
                "city": c.get("ciudad_entidad"),
                "url": c.get("urlproceso", {}).get("url")
            })
            
        return json.dumps(simplified_contracts, ensure_ascii=False)
        
    except Exception as e:
        return f"Error searching contracts: {str(e)}"
