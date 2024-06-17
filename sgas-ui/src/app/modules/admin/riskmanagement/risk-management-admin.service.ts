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
    console.log('apiUrl', `${apiUrl}/riskmanagement/departments/`);
    const result = this.http.get<Department[]>(`${apiUrl}/riskmanagement/departments/`);
    console.log('result', result);
    return result;
  }

//   getDepartments() {
//     console.log('apiUrl', `${apiUrl}/riskmanagement/departments/`);
//     const result = this.http.get(`${apiUrl}/riskmanagement/departments/`);
//     console.log('result', result);
//     return result;
//   }
}
