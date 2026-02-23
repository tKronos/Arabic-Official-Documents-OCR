# schemas.py

DOCUMENT_SCHEMAS = {
    "Passport": {
        "passport_number": "",
        "full_name": "",
        "first_name": "",
        "father_name": "",
        "nationality": "",
        "date_of_birth": "",
        "place_of_birth": "",
        "sex": "",
        "issuance_date": "",
        "expiry_date": "",
        "authority": "",
        "mother_name": "",
        "registry_place": ""
    },
    "National ID": {
        "id_number": "",
        "full_name": "",
        "date_of_birth": "",
        "nationality": "",
        "address": "",
        "issue_date": "",
        "expiry_date": ""
    },
    "Company Registration": {
        "company_name": "",
        "registration_number": "",
        "tax_id": "",
        "registration_date": "",
        "address": "",
        "legal_form": ""
    },
    "Establishment Registration": {
        "establishment_name": "",       
        "trade_name": "",              
        "registration_number": "",      
        "personal_registration_number": "", 
        "owner_name": "",              
        "registration_date": "",
        "address": "",
        "legal_form": "Establishment"   
    },
    "Driver's License": {
        "license_number": "",
        "full_name": "",
        "date_of_birth": "",
        "issue_date": "",
        "expiry_date": "",
        "license_class": "",
        "address": ""
    },
    "Residence Permit": {
        "permit_number": "",
        "full_name": "",
        "nationality": "",
        "issue_date": "",
        "expiry_date": "",
        "sponsor": ""
    },
    "Hand Writing": {
        "Written Sentence": ""
    }
}