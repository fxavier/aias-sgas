import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';
import { EnvironAndSocialRiskAndImpactAssessment } from './types/types';
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

  // getDepartment(id: number): Observable<Department> {
  //   return this.http.get<Department>(`${apiUrl}/riskmanagement/departments/${id}`);
  // }

  // addDepartment(department: Omit<Department, 'id'>): Observable<Department> {
  //   return this.http.post<Department>(`${apiUrl}/riskmanagement/departments/`, department);
  // }
}
