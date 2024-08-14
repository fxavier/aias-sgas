import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-list-env-social-risk-impact',
  standalone: true,
  imports: [],
  templateUrl: './list-env-social-risk-impact.component.html',
  styleUrl: './list-env-social-risk-impact.component.scss'
})
export class ListEnvSocialRiskImpactComponent implements OnInit {

  displayedColumns: string[] = [
    'activity',
    'life_cycle',
    'department',
    'extension',
    'env_factor',
    'legal_req_control',
    'duration',
    'life_cycle',
    'intensity',
    'probability',
    'significance',
    'actions'
  ]
  
  ngOnInit(): void {
    throw new Error('Method not implemented.');
  }

}
