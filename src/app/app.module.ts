import { NgModule, Injector } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { createCustomElement } from '@angular/elements';
import { ScullyLibModule } from '@scullyio/ng-lib';
import { BrowserAnimationsModule } from '@angular/platform-browser/animations';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { DocumentationComponent } from './components/documentation/documentation.component';
import { LeftBarMenuComponent } from './components/left-bar-menu/left-bar-menu.component';
import { BreadCrumbsComponent } from './components/bread-crumbs/bread-crumbs.component';
import { HomeComponent } from './components/home/home.component';
import { HeaderComponent } from './components/header/header.component';
import { UiKitModule } from './ui-kit/ui-kit.module';
import { DropdownMenuItemComponent } from './components/left-bar-menu/dropdown-menu-item/dropdown-menu-item.component';
import { ExandableElementComponent } from './web-components/exandable-element/exandable-element.component';
import { CodeBlockComponent } from './web-components/code-block/code-block.component';
import { TextColumnsComponent } from './web-components/text-columns/text-columns.component';
import { GalleryComponent } from './web-components/gallery/gallery.component';
import { MenuService } from './services/menu.service';

@NgModule({
    declarations: [
        AppComponent,
        DocumentationComponent,
        LeftBarMenuComponent,
        BreadCrumbsComponent,
        HomeComponent,
        HeaderComponent,
        DropdownMenuItemComponent,
        ExandableElementComponent,
        CodeBlockComponent,
        TextColumnsComponent,
        GalleryComponent,
    ],
    imports: [BrowserModule, AppRoutingModule, ScullyLibModule, BrowserAnimationsModule, UiKitModule],
    providers: [MenuService],
    bootstrap: [AppComponent],
})
export class AppModule {
    constructor(private injector: Injector) {
        const expandableElement = createCustomElement(ExandableElementComponent, {
            injector,
        });
        const codeBlock = createCustomElement(CodeBlockComponent, {
            injector,
        });
        const columnsLayout = createCustomElement(TextColumnsComponent, {
            injector,
        });
        const gallery = createCustomElement(GalleryComponent, {
            injector,
        });
        customElements.define('expandable-element', expandableElement);
        customElements.define('code-block', codeBlock);
        customElements.define('columns-layout', columnsLayout);
        customElements.define('media-gallery', gallery);
    }
}
