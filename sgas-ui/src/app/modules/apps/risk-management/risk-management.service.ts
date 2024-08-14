import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';
import { Department, EnvironAndSocialRiskAndImpactAssessment, EnvironmentalFactor, LegalRequirementControl, RisksAndImpact } from './types/types';
import { environment } from 'environments/environment.development';

const apiUrl = environment.apiUrl;

@Injectable({
  providedIn: 'root'
})
export class RiskManagementService {

  constructor(private http: HttpClient) { }

  getEnvSocialRiskImpact(): Observable<EnvironAndSocialRiskAndImpactAssessment[]>{
    return this.http.get<EnvironAndSocialRiskAndImpactAssessment[]>(`${apiUrl}/riskmanagement/environ-and-social-risk-and-impact-assessments/`);
  }

  getDepartments(): Observable<Department[]> {
    return this.http.get<Department[]>(`${apiUrl}/riskmanagement/departments/`);
  }

  getEnvFactors(): Observable<EnvironmentalFactor[]> {
    return this.http.get<EnvironmentalFactor[]>(`${apiUrl}/riskmanagement/environmental-factors/`)
  }

  getRisksImpact(): Observable<RisksAndImpact[]> {
    return this.http.get<RisksAndImpact[]>(`${apiUrl}/riskmanagement/risks-and-impacts/`)
  }

  getLegalRequirements(): Observable<LegalRequirementControl[]> {
    return this.http.get<LegalRequirementControl[]>(`${apiUrl}/riskmanagement/legal-requirement-controls/`)
  }

  addEnvSocialImpact(envSocialImpact: Omit<EnvironAndSocialRiskAndImpactAssessment, 'id'>):
    Observable<EnvironAndSocialRiskAndImpactAssessment> {
    return this.http.post<EnvironAndSocialRiskAndImpactAssessment>(
      `${apiUrl}/riskmanagement/environ-and-social-risk-and-impact-assessments/`, envSocialImpact);
  }



  // getDepartment(id: number): Observable<Department> {
  //   return this.http.get<Department>(`${apiUrl}/riskmanagement/departments/${id}`);
  // }

  // addDepartment(department: Omit<Department, 'id'>): Observable<Department> {
  //   return this.http.post<Department>(`${apiUrl}/riskmanagement/departments/`, department);
  // }
}
