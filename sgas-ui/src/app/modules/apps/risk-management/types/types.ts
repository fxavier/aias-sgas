export interface Department {
    id: number;
    name: string;
    description: string;
  }

  export interface EnvironmentalFactor {
    id: number;
    description: string;
  }
  
  export interface RisksAndImpact {
    id: number;
    description: string;
  }

  export interface EnvironAndSocialRiskAndImpactAssessment {
    id: number;
    departament: number;
    department_name: string;
    activity: string;
    risks_and_impact: RisksAndImpact;
    environmental_factor: EnvironmentalFactor;
    life_cycle: string;
    statute: string;
    extension: string;
    duration: string;
    intensity: string;
    probability: string;
    significance: string | null;
    description_of_measures: string;
    deadline: string;
    responsible: number;
    effectiveness_assessment: string;
    legal_requirements: number[];
    compliance_requirements: string;
    observations: string;
    created_by: number;
    created_at: string;
    updated_at: string;
  }
  
  export interface LegalRequirementControl {
    id: number;
    number: string;
    document_title: string;
    effective_date: string;
    description: string;
    status: string;
    amended_description: string | null;
    observation: string | null;
    law_file: string | null;
    created_by: number;
    created_at: string;
    updated_at: string;
  }
  
  export interface ContactPerson {
    id: number;
    name: string;
    role: string;
    contact: string;
    date: string;
    signature: string | null;
  }
  
  export interface ResponsibleForFillingForm extends ContactPerson {}
  
  export interface ResponsibleForVerification extends ContactPerson {}
  
  export interface BiodiversityAndNaturalResources {
    id: number;
    reference: string | null;
    description: string;
  }
  
  export interface Subproject {
    id: number;
    name: string;
    contract_reference: string | null;
    contractor_name: string | null;
    estimated_cost: number | null;
    location: string;
    geographic_coordinates: string | null;
    type: string;
    approximate_area: string;
  }
  
  export interface EnvironmentalSocialScreening {
    id: number;
    responsible_for_filling_form: ResponsibleForFillingForm;
    responsible_for_verification: ResponsibleForVerification;
    subproject: Subproject;
    biodiversidade_recursos_naturais: BiodiversityAndNaturalResources;
    response: string;
    comment: string | null;
    relevant_standard: string | null;
    consultation_and_engagement: string | null;
    recommended_actions: string | null;
    screening_results: number;
    created_by: number;
    created_at: string;
    updated_at: string;
  }
  
  export interface ConsultationAndEngagement {
    id: number;
    subproject: Subproject;
    details: string;
  }
  
  export interface ScreeningResult {
    id: number;
    subproject: Subproject;
    risk_category: string;
    description: string;
    instruments_to_be_developed: string;
  }
  
  export interface PreliminaryEnvironmentalInformation {
    id: number;
    activity_name: string;
    activity_type: string;
    other_activity_type: string | null;
    development_stage: string;
    other_development_stage: string | null;
    proponents: string | null;
    address: string;
    telephone: string | null;
    fax: string | null;
    mobile_phone: string | null;
    email: string;
    activity_location: string;
    activity_city: string;
    activity_locality: string | null;
    activity_district: string | null;
    activity_province: string;
    geographic_coordinates: string | null;
    insertion_point: string;
    territorial_planning_framework: string;
    activity_infrastructure: string | null;
    associated_activities: string | null;
    construction_operation_technology_description: string | null;
    main_complementary_activities: string | null;
    labor_type_quantity_origin: string | null;
    raw_materials_type_quantity_origin_and_provenance: string | null;
    chemicals_used: string | null;
    type_origin_water_energy_consumption: string | null;
    fuels_lubricants_origin: string | null;
    other_resources_needed: string | null;
    land_ownership: string | null;
    activity_location_alternatives: string | null;
    brief_description_on_local_regional_ref_env_situation: string | null;
    physical_characteristics_of_activity_site: string | null;
    predominant_ecosystems: string | null;
    location_zone: string | null;
    type_predominant_vegetation: string | null;
    land_use: string | null;
    existing_infrastructure_around_activity_area: string | null;
    total_investment_value: number | null;
    created_by: number;
    created_at: string;
    updated_at: string;
  }