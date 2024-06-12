import { Routes } from '@angular/router';
import { DashboardComponent } from './dashboard/dashboard.component';
import { RiskImpactComponent } from './risk-impact/risk-impact.component';

export const routes: Routes = [
    {path: '', redirectTo: 'dashboard', pathMatch: 'full'},
    {path: 'dashboard', component: DashboardComponent},
    {path: 'risk-impact',component: RiskImpactComponent},
    // {path: 'products', component: ProductsComponent},
    // {path: 'statistics', component: StatisticsComponent},
    // {path: 'coupens', component: CoupensComponent},
    // {path: 'pages', component: PagesComponent},
    // {path: 'media', component: MediaComponent},
    // {path: 'settings', component: SettingsComponent}
];
