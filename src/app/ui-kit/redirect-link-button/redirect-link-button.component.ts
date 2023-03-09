import { ChangeDetectionStrategy, Component, Input } from '@angular/core';

@Component({
  selector: 'gc-redirect-link-button',
  templateUrl: './redirect-link-button.component.html',
  styleUrls: ['./redirect-link-button.component.scss'],
  changeDetection: ChangeDetectionStrategy.OnPush,
})
export class RedirectLinkButtonComponent {
  @Input() href: string;
  @Input() label: string;
  @Input() variant: string;
}
