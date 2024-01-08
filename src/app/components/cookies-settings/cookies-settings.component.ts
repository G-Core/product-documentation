import { ChangeDetectionStrategy, Component, EventEmitter, Output } from '@angular/core';
import { AnalyticsService, CookiesConsent } from '../../services/analitycs.service';

@Component({
    selector: 'gc-cookies-settings',
    templateUrl: './cookies-settings.component.html',
    styleUrls: ['./cookies-settings.component.scss'],
    changeDetection: ChangeDetectionStrategy.OnPush,
})
export class CookiesSettingsComponent {
    public isSettings: boolean = false;
    public marketing: string = 'decline';
    public statistic: string = 'decline';

    @Output() public closeModal: EventEmitter<void> = new EventEmitter();
    @Output() public openPolicy: EventEmitter<void> = new EventEmitter();

    constructor(private analitycsService: AnalyticsService) {}

    public showSetting(): void {
        this.isSettings = true;
    }

    public backFromSettings(): void {
        this.isSettings = false;
    }

    public acceptAll(): void {
        this.analitycsService.setCookiesConsent(CookiesConsent.All);
        this.closeModal.emit();
    }

    public rejectAll(): void {
        this.analitycsService.setCookiesConsent(CookiesConsent.DeclineAll);
        this.closeModal.emit();
    }

    public acceptSelected(): void {
        let cookieConsent;

        if (this.marketing === 'decline' && this.statistic === 'decline') {
            cookieConsent = CookiesConsent.DeclineAll;
        } else if (this.marketing === 'accept' && this.statistic === 'accept') {
            cookieConsent = CookiesConsent.All;
        } else if (this.marketing === 'accept') {
            cookieConsent = CookiesConsent.Marketing;
        } else if (this.statistic === 'accept') {
            cookieConsent = CookiesConsent.Statistic;
        }
        this.analitycsService.setCookiesConsent(cookieConsent);
        this.closeModal.emit();

        console.log('reer');
    }
}
