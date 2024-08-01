import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { environment } from 'environments/environment.development';
import { Observable } from 'rxjs';
import { Department } from './types/types';

const apiUrl = environment.apiUrl;

@Injectable({
  providedIn: 'root'
})
export class RiskManagementAdminService {

  constructor(private http: HttpClient) { }

  getDepartments(): Observable<Department[]>{
    return this.http.get<Department[]>(`${apiUrl}/riskmanagement/departments/`);
  }

  getDepartment(id: number): Observable<Department> {
    return this.http.get<Department>(`${apiUrl}/riskmanagement/departments/${id}`);
  }

  addDepartment(department: Omit<Department, 'id'>): Observable<Department> {
    return this.http.post<Department>(`${apiUrl}/riskmanagement/departments/`, department);
  }

  editDepartment(department: Department): Observable<Department> {
    return this.http.put<Department>(`${apiUrl}/riskmanagement/departments/${department.id}`, department);
  }

  deleteDepartment(id: number): Observable<void> {
    return this.http.delete<void>(`${apiUrl}/riskmanagement/departments/${id}`);
  }

}
