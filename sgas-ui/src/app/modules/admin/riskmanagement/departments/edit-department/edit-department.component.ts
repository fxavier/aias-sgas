import { Component, OnInit } from '@angular/core';
import { FormBuilder, FormGroup, Validators, ReactiveFormsModule } from '@angular/forms';
import { CommonModule } from '@angular/common';
import { MatButtonModule } from '@angular/material/button';
import { MatFormFieldModule } from '@angular/material/form-field';
import { MatInputModule } from '@angular/material/input';
import { MatIconModule } from '@angular/material/icon';
import { MatCardModule } from '@angular/material/card';
import { ActivatedRoute, RouterModule, Router } from '@angular/router';
import { Department } from '../../types/types';
import { RiskManagementAdminService } from '../../risk-management-admin.service';


@Component({
  selector: 'app-edit-department',
  standalone: true,
  templateUrl: './edit-department.component.html',
  styleUrl: './edit-department.component.scss',
  imports: [
    CommonModule,
    ReactiveFormsModule,
    MatButtonModule,
    MatFormFieldModule,
    MatInputModule,
    MatIconModule,
    MatCardModule,
    RouterModule
  ]
})
export class EditDepartmentComponent {

  departmentForm!: FormGroup;
  departmentId!: number;

  constructor(
    private fb: FormBuilder,
    private route: ActivatedRoute,
    private router: Router,
    private riskManagementAdminService: RiskManagementAdminService
  ) {}

  ngOnInit(): void {
    this.departmentForm = this.fb.group({
      name: ['', Validators.required],
      description: ['', Validators.required]
    });

    this.route.paramMap.subscribe(params => {
      this.departmentId = Number(params.get('id'));
      this.loadDepartment(this.departmentId);
    });
  }

  loadDepartment(id: number): void {
    this.riskManagementAdminService.getDepartment(id).subscribe({
      next: (department) => {
        this.departmentForm.patchValue(department);
      },
      error: (error) => {
        console.error('Error loading department', error);
      }
    });
  }

  onSubmit(): void {
    if (this.departmentForm.valid) {
      const updatedDepartment: Department = {
        id: this.departmentId,
        ...this.departmentForm.value
      };
      this.riskManagementAdminService.editDepartment(updatedDepartment).subscribe({
        next: (response) => {
          console.log('Department updated successfully', response);
          this.router.navigate(['/departments']); // Adjust the route as needed
        },
        error: (error) => {
          console.error('Error updating department', error);
        }
      });
    }
  }

}
