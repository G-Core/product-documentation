import { NgModule } from '@angular/core';
import { RedirectLinkButtonComponent } from './redirect-link-button/redirect-link-button.component';
import { SearchBoxComponent } from './search-box/search-box.component';
import { CallToActionBoxComponent } from './call-to-action-box/call-to-action-box.component';

@NgModule({
    declarations: [RedirectLinkButtonComponent, SearchBoxComponent, CallToActionBoxComponent],
    imports: [],
    exports: [RedirectLinkButtonComponent, SearchBoxComponent, CallToActionBoxComponent],
    providers: [],
})
export class UiKitModule {}
