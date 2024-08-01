import { Component, OnInit, ViewChild, ViewEncapsulation } from '@angular/core';
import { FormBuilder, FormGroup, FormsModule, NgForm, ReactiveFormsModule, Validators } from '@angular/forms';
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
import { FuseAlertType } from '@fuse/components/alert';
import { HttpClient } from '@angular/common/http';

@Component({
  selector: 'app-add-department',
  standalone: true,
  encapsulation: ViewEncapsulation.None,
  imports: [
        MatIconModule,
        FormsModule,
        ReactiveFormsModule,
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
 departmentForm!: FormGroup;
 @ViewChild('departmentNgForm') departmentNgForm: NgForm;
 departments: Department[] = [];

 alert: { type: FuseAlertType; message: string } = {
    type: 'success',
    message: '',
 };

 showAlert: boolean = false;

// departments: any = [];

  constructor(private service: RiskManagementAdminService,
              private formBuilder: FormBuilder) { }

  ngOnInit(): void {
  //  this.getDepartments();
    this.departmentForm = this.formBuilder.group({
      name: ['', Validators.required],
      description: ['', Validators.required],
    });
  }

  getDepartments(): void{
    this.service.getDepartments().subscribe({
      next: (res: Department[]) => {
      //  console.log('res', res);
        this.departments = res;
        console.log('Departments', this.departments);
      },
      error: (error) => {
        console.error(error);
      }
    });
  }

  onSubmit(): void {
    if (this.departmentForm.valid) {
      if (this.departmentForm.valid) {
        const department: Omit<Department, 'id'> = this.departmentForm.value;
        this.service.addDepartment(department)
        .subscribe({
          next: (res: Department) => {
            this.departments.push(res);
            this.departmentForm.reset();
            this.showAlert = true;
            this.alert.message = 'Department added successfully';
          },
          error: (error) => {
            console.error(error);
            this.showAlert = true;
            this.alert.type = 'error';
            this.alert.message = 'An error occurred while adding department';
          }
        })
      }
    }
  }

}
