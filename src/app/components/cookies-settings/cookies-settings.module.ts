import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';

import { UiKitModule } from '../../ui-kit/ui-kit.module';
import { CookiesSettingsComponent } from './cookies-settings.component';

@NgModule({
    declarations: [CookiesSettingsComponent],
    imports: [CommonModule, UiKitModule],
    exports: [CookiesSettingsComponent],
})
export class CookiesSettingsModule {}
