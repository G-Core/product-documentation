import { ChangeDetectionStrategy, ChangeDetectorRef, Component, OnDestroy, OnInit } from '@angular/core';
import { NavigationEnd, Router } from '@angular/router';
import { Subscription, filter } from 'rxjs';

@Component({
    selector: 'gc-disclaimer',
    templateUrl: './disclaimer.component.html',
    styleUrls: ['./disclaimer.component.scss'],
    changeDetection: ChangeDetectionStrategy.OnPush,
})
export class DisclaimerComponent implements OnInit {
    public isResellerSupportPage = false;
    public isWaapPage = false;

    constructor(private router: Router, private cd: ChangeDetectorRef) {}

    public ngOnInit(): void {
        this.router.events.pipe(filter((event) => event instanceof NavigationEnd)).subscribe(() => {
            this.isResellerSupportPage = this.router.url.includes('/reseller-support');
            this.isWaapPage = this.router.url.includes('/waap');
            this.cd.detectChanges();
        });
    }
}
