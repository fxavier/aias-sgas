import { TestBed } from '@angular/core/testing';

import { RiskManagementAdminService } from './risk-management-admin.service';

describe('RiskManagementAdminService', () => {
  let service: RiskManagementAdminService;

  beforeEach(() => {
    TestBed.configureTestingModule({});
    service = TestBed.inject(RiskManagementAdminService);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });
});
