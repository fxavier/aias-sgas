import { AfterViewInit, ChangeDetectorRef, Component, OnInit, ViewChild } from '@angular/core';
import { EnvironAndSocialRiskAndImpactAssessment } from '../types/types';
import { RiskManagementService } from '../risk-management.service';
import { MatTableDataSource, MatTableModule } from '@angular/material/table';
import { MatPaginator, MatPaginatorModule } from '@angular/material/paginator';
import { MatSortModule } from '@angular/material/sort';
import { MatIconModule } from '@angular/material/icon';
import { MatButtonModule } from '@angular/material/button';
import { AsyncPipe } from '@angular/common';
import { CommonModule } from '@angular/common';
import { MatDialog } from '@angular/material/dialog';
import { AddEnvSocialRiskImpactAssementComponent } from '../add-env-social-risk-impact-assement/add-env-social-risk-impact-assement.component';


@Component({
  selector: 'app-list-env-social-risk-impact',
  standalone: true,
  templateUrl: './list-env-social-risk-impact.component.html',
  styleUrl: './list-env-social-risk-impact.component.scss',
  imports: [
    MatTableModule,
    MatPaginatorModule,
    MatSortModule,
    MatIconModule,
    MatButtonModule,
    AsyncPipe,
    CommonModule
  ]
    
})
export class ListEnvSocialRiskImpactComponent implements OnInit, AfterViewInit {
  
  displayedColumns: string[] = [
    'activity',
    'life_cycle',
    'department_name',
    'extension',
    'statute',
    'intensity',
    // 'env_factor',
    // 'legal_req_control',
    'duration',
    // 'life_cycle',
    // 'intensity',
    // 'probability',
    'significance',
    'actions'
  ];
  dataSource = new MatTableDataSource<EnvironAndSocialRiskAndImpactAssessment>();
  @ViewChild(MatPaginator) paginator: MatPaginator;


  constructor(
    private service: RiskManagementService, 
    private cdr: ChangeDetectorRef,
    private dialog: MatDialog
  ) { }

  ngOnInit(): void {
    this.loadEnvSocialList();
  }

  ngAfterViewInit(): void {
    this.dataSource.paginator = this.paginator;
  }

  loadEnvSocialList(): void {
    this.service.getEnvSocialRiskImpact().subscribe(data => {
      this.dataSource.data = data;
      this.cdr.detectChanges(); // Trigger change detection if needed
    });
  }

  editItem(item: EnvironAndSocialRiskAndImpactAssessment): void {
    const dialogRef = this.dialog.open(AddEnvSocialRiskImpactAssementComponent, {
      width: '600px',
      data: item // Pass the selected item to the dialog
    });

    dialogRef.afterClosed().subscribe(result => {
      if (result) {
        this.service.updateEnvSocialImpact(result).subscribe(() => {
          this.loadEnvSocialList(); // Reload the list after editing
        });
      }
    });
  }

  deleteItem(id: number): void {
    if (confirm('Are you sure you want to delete this item?')) {
      this.service.deleteEnvSocialImpact(id).subscribe(() => {
        this.loadEnvSocialList(); // Reload the list after deletion
      });
    }
  }



}
