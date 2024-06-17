import { Component, OnInit, ViewEncapsulation } from '@angular/core';
import { FormsModule } from '@angular/forms';
import { MatButtonModule } from '@angular/material/button';
import { MatCheckboxModule } from '@angular/material/checkbox';
import { MatOptionModule } from '@angular/material/core';
import { MatDividerModule } from '@angular/material/divider';
import { MatFormFieldModule } from '@angular/material/form-field';
import { MatIconModule } from '@angular/material/icon';
import { MatInputModule } from '@angular/material/input';
import { MatRadioModule } from '@angular/material/radio';
import { MatSelectModule } from '@angular/material/select';
import { Department } from '../../types/types';
import { RiskManagementAdminService } from '../../risk-management-admin.service';

@Component({
  selector: 'app-add-department',
  standalone: true,
  encapsulation: ViewEncapsulation.None,
  imports: [
        MatIconModule,
        FormsModule,
        MatFormFieldModule,
        MatInputModule,
        MatSelectModule,
        MatOptionModule,
        MatDividerModule,
        MatCheckboxModule,
        MatRadioModule,
        MatButtonModule,
  ],
  templateUrl: './add-department.component.html',
  styleUrl: './add-department.component.scss'
})
export class AddDepartmentComponent implements OnInit{
 departments: Department[] = [];
// departments: any = [];

  constructor(private service: RiskManagementAdminService) { }

  ngOnInit(): void {
    this.getDepartments();
  }

  getDepartments(): void{
    this.service.getDepartments().subscribe({
      next: (res: Department[]) => {
        console.log('res', res);
        this.departments = res;
        console.log('Departments', this.departments);
      },
      error: (error) => {
        console.error(error);
      }
    });
  }

  // getDepartments(){
  //   this.service.getDepartments().subscribe({
  //     next: (res: any) => {
  //       this.departments = res.data;
  //       console.log('Departments', this.departments);
  //     },
  //     error: (error) => {
  //       console.error(error);
  //     }
  //   });
  // }

}
