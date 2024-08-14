import { TextFieldModule } from '@angular/cdk/text-field';
import { NgClass } from '@angular/common';
import { Component, OnInit, ViewChild, ViewEncapsulation } from '@angular/core';
import {
    FormBuilder,
    FormControl,
    FormGroup,
    FormsModule,
    NgForm,
    ReactiveFormsModule,
    ValidationErrors,
    Validators,
} from '@angular/forms';
import { MatButtonModule } from '@angular/material/button';
import { MatButtonToggleModule } from '@angular/material/button-toggle';
import { MatChipsModule } from '@angular/material/chips';
import { MatOptionModule } from '@angular/material/core';
import { MatDatepickerModule } from '@angular/material/datepicker';
import { MatFormFieldModule } from '@angular/material/form-field';
import { MatIconModule } from '@angular/material/icon';
import { MatInputModule } from '@angular/material/input';
import { MatSelectModule } from '@angular/material/select';
import { Duration, Extension, Intensity, LifeCycle, Probability, Statute, } from 'app/modules/admin/riskmanagement/types/types';
import { enumToArray } from 'app/modules/admin/riskmanagement/utils/enum-utils';
import { RiskManagementService } from '../risk-management.service';
import { Department, EnvironAndSocialRiskAndImpactAssessment, EnvironmentalFactor, LegalRequirementControl, RisksAndImpact } from '../types/types';



@Component({
  selector: 'forms-fields',
  templateUrl: './add-env-social-risk-impact-assement.component.html',
  encapsulation: ViewEncapsulation.None,
  standalone: true,
  imports: [
      MatIconModule,
      FormsModule,
      MatFormFieldModule,
      NgClass,
      MatInputModule,
      TextFieldModule,
      ReactiveFormsModule,
      MatButtonToggleModule,
      MatButtonModule,
      MatSelectModule,
      MatOptionModule,
      MatChipsModule,
      MatDatepickerModule,
  ],
})
export class AddEnvSocialRiskImpactAssementComponent implements OnInit {
  envForm: FormGroup;
  formFieldHelpers: string[] = [''];
  durations: { key: string; value: string }[] = [];
  lifeCycles: { key: string; value: string}[] = [];
  statutes: { key: string; value: string}[] = [];
  extensions: { key: string; value: string}[] = [];
  intensities: { key: string; value: string}[] = [];
  departments: Department[] = [];
  risks_impacts: RisksAndImpact[] = [];
  env_factors: EnvironmentalFactor[] = [];
  legalRequirements: LegalRequirementControl[] = [];
  probabilities: { key: string; value: string}[] = [];
  user_id: number = 1;
  responsible: number = 1;
  @ViewChild('riskImpactNgForm') riskImpactNgForm: NgForm;
  envRiskImpact: EnvironAndSocialRiskAndImpactAssessment;
  

  
  /**
   * Constructor
   */
  constructor(private formBuilder: FormBuilder, private service: RiskManagementService) {}

  // -----------------------------------------------------------------------------------------------------
  // @ Public methods
  // -----------------------------------------------------------------------------------------------------


  ngOnInit(): void {
    this.getDepartments();
    this.getRisksImpact();
    this.getEnvFactors();
    this.getLegalRequirements();
    this.durations = enumToArray(Duration);
    this.lifeCycles = enumToArray(LifeCycle);
    this.extensions = enumToArray(Extension);
    this.statutes = enumToArray(Statute);
    this.intensities = enumToArray(Intensity);
    this.probabilities = enumToArray(Probability);
    this.envForm = this.formBuilder.group({
        activity: ['', Validators.required],
        life_cycle: ['', Validators.required],
        statute: ['', Validators.required],
        extension: ['', Validators.required],
        intensity: ['', Validators.required],
        duration: ['', Validators.required],
        description_of_measures: ['', Validators.required],
        deadline: ['', Validators.required],
        effectiveness_assessment: ['', Validators.required],
        compliance_requirements: ['', Validators.required],
        observations: ['', Validators.required],
        departament: ['', Validators.required],
        risks_and_impact: ['', Validators.required],
        environmental_factor: ['', Validators.required],
        responsible: this.responsible,
        legal_requirements: [[], Validators.required],
        probability:'',
        created_by: this.user_id

    });
    }

    getDepartments(): void {
        this.service.getDepartments().subscribe({
          next: (res: Department[]) => {
            this.departments = res;
          },
          error: (error) => {
            console.error(error);
          }
        });
      }

    getRisksImpact(): void {
        this.service.getRisksImpact().subscribe({
          next: (res: RisksAndImpact[]) => {
            this.risks_impacts = res;
          },
          error: (error) => {
            console.error(error);
          }
        });
      }

    getEnvFactors(): void {
        this.service.getEnvFactors().subscribe({
          next: (res: EnvironmentalFactor[]) => {
            this.env_factors = res;
          },
          error: (error) => {
            console.error(error);
          }
        });
      }

    getLegalRequirements(): void {
        this.service.getLegalRequirements().subscribe({
          next: (res: LegalRequirementControl[]) => {
            this.legalRequirements = res;
          },
          error: (error) => {
            console.error(error);
          }
        });
      }

      onSubmit(form: FormControl) {
          if (this.envForm.valid) {
            console.log(this.envForm.value);
            this.service.addEnvSocialImpact(this.envForm.value).subscribe({
                next: (res) => {
                console.log(res);
               // form.reset();
                },
                error: (error) => {
                console.error(error);
                }
            });
        }
          
      }

    
}
    


