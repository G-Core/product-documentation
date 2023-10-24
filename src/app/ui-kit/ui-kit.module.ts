import { CommonModule } from '@angular/common';
import { NgModule } from '@angular/core';
import { FormsModule } from '@angular/forms';
import { RedirectLinkButtonComponent } from './redirect-link-button/redirect-link-button.component';
import { SearchBoxComponent } from './search-box/search-box.component';
import { CallToActionBoxComponent } from './call-to-action-box/call-to-action-box.component';
import { PaginationComponent } from './pagination';
import { ModalComponent } from './modal';
import { LoaderComponent, LoaderModule } from './loader';

@NgModule({
    declarations: [
        RedirectLinkButtonComponent,
        SearchBoxComponent,
        CallToActionBoxComponent,
        PaginationComponent,
        ModalComponent,
    ],
    imports: [FormsModule, CommonModule, LoaderModule],
    exports: [
        RedirectLinkButtonComponent,
        SearchBoxComponent,
        CallToActionBoxComponent,
        FormsModule,
        PaginationComponent,
        ModalComponent,
        LoaderComponent,
    ],
    providers: [],
})
export class UiKitModule {}
