import { Component, ChangeDetectionStrategy } from '@angular/core';
import { Observable } from 'rxjs';
import { DeviceService } from '../../services/device';

@Component({
    selector: 'gcore-modal-login',
    templateUrl: './modal-login.component.html',
    styleUrls: ['./modal-login.component.scss'],
    changeDetection: ChangeDetectionStrategy.OnPush,
})
export class ModalLoginComponent {
    public isMobile$: Observable<boolean> = this.deviceService.isMobile$;
    public showAllProducts = false;
    public gcoreEdgeSolutionsProducts: Array<string> = [
        'Edge Delivery (CDN)',
        'DNS with failover',
        'Virtual Machines',
        'Bare Metal',
        'Cloud Load Balancers',
        'Managed Kubernetes',
        'AI Infrastructure',
        'Edge Security (DDOS+WAF)',
        'FaaS',
        'Streaming',
        'Object Storage',
        'ImageStack (Optimize and Resize)',
        'Edge Compute (Coming soon)',
    ];
    public gcoreHostingProducts: Array<string> = ['VPS Hosting', 'Dedicated Servers', 'SSL Certificates'];

    constructor(private deviceService: DeviceService) {}

    public showAll(): void {
        this.showAllProducts = true;
    }
}
