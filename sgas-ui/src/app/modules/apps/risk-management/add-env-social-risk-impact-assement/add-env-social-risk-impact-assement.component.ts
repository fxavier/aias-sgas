import { CommonModule } from '@angular/common';
import { Component, OnInit, ViewChild } from '@angular/core';
import { FormBuilder, FormGroup, FormsModule, NgForm, ReactiveFormsModule, Validators } from '@angular/forms';
import { MatButtonModule } from '@angular/material/button';
import { MatOptionModule } from '@angular/material/core';
import { MatFormFieldModule } from '@angular/material/form-field';
import { MatIcon } from '@angular/material/icon';
import { MatSelectModule } from '@angular/material/select';
import { RiskManagementAdminService } from 'app/modules/admin/riskmanagement/risk-management-admin.service';
import { Department } from '../types/types';

@Component({
  selector: 'app-add-env-social-risk-impact-assement',
  standalone: true,
  templateUrl: './add-env-social-risk-impact-assement.component.html',
  styleUrl: './add-env-social-risk-impact-assement.component.scss',
  imports: [
    CommonModule,
    FormsModule,
    ReactiveFormsModule,
    MatFormFieldModule,
    MatIcon,
    MatButtonModule,
    MatOptionModule,
    MatSelectModule

  ]
})
export class AddEnvSocialRiskImpactAssementComponent implements OnInit{
 
  envForm!: FormGroup;
  @ViewChild('envNgForm') envNgForm: NgForm;
  departments: Department [] = [];

  constructor( private departmentService: RiskManagementAdminService,
               private formBuilder: FormBuilder){}

  ngOnInit(): void {
    this.getDepartments();
      this.envForm = this.formBuilder.group({
      department: ['', Validators.required],
      activity: ['', Validators.required],
      risks_and_impact: ['', Validators.required]

    })
  }


  getDepartments() {
    return this.departmentService.getDepartments().subscribe(
      (data: Department[]) => {
        this.departments = data;
      },
      (error) => {
        console.error('Error fetching departments', error);
      }
    );
  }
  
  onSubmit() { 
    console.log('Do something');
  }



}
