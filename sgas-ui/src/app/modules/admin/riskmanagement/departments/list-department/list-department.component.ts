import { Component } from '@angular/core';
import { Observable } from 'rxjs';
import { Department } from '../../types/types';
import { RiskManagementAdminService } from '../../risk-management-admin.service';
import { CommonModule } from '@angular/common';
import { MatButtonModule } from '@angular/material/button';
import { MatIconModule } from '@angular/material/icon';
import { MatTableModule } from '@angular/material/table';

@Component({
  selector: 'app-list-department',
  standalone: true,
  imports: [
    CommonModule,
    MatButtonModule,
    MatIconModule,
    MatTableModule
  ],
  templateUrl: './list-department.component.html',
  styleUrl: './list-department.component.scss'
})
export class ListDepartmentComponent {
  displayedColumns: string[] = ['name', 'description', 'actions'];
  departments$: Observable<Department[]>;

  constructor(private riskManagementAdminService: RiskManagementAdminService) {}

  ngOnInit(): void {
    this.departments$ = this.riskManagementAdminService.getDepartments();
  }

  editDepartment(department: Department): void {
    // Implement the logic for editing a department.
    // This could involve navigating to a different component with a form to edit the department.
    console.log('Edit department', department);
  }

  deleteDepartment(id: number): void {
    this.riskManagementAdminService.deleteDepartment(id).subscribe({
      next: () => {
        console.log('Department deleted successfully');
        this.departments$ = this.riskManagementAdminService.getDepartments(); // Refresh the list
      },
      error: (error) => {
        console.error('Error deleting department', error);
      }
    });
  }

}
