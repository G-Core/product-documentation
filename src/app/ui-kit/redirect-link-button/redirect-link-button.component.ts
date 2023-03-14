import { ChangeDetectionStrategy, Component, Input } from '@angular/core';

@Component({
    selector: 'gc-redirect-link-button',
    templateUrl: './redirect-link-button.component.html',
    styleUrls: ['./redirect-link-button.component.scss'],
    changeDetection: ChangeDetectionStrategy.OnPush,
})
export class RedirectLinkButtonComponent {
    @Input() public href: string;
    @Input() public label: string;
    @Input() public variant: string;
}
