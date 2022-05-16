import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { ScullyLibModule } from '@scullyio/ng-lib';
import { BrowserAnimationsModule } from '@angular/platform-browser/animations';
import { DocumentationComponent } from './components/documentation/documentation.component';
import { LeftBarMenuComponent } from './components/left-bar-menu/left-bar-menu.component';
import { BreadCrumbsComponent } from './components/bread-crumbs/bread-crumbs.component';
import { HomeComponent } from './components/home/home.component';
import { HeaderComponent } from './components/header/header.component';
import { UiKitModule } from './ui-kit/ui-kit.module';

@NgModule({
  declarations: [
    AppComponent,
    DocumentationComponent,
    LeftBarMenuComponent,
    BreadCrumbsComponent,
    HomeComponent,
    HeaderComponent,
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    ScullyLibModule,
    BrowserAnimationsModule,
    UiKitModule,
  ],
  providers: [],
  bootstrap: [AppComponent],
})
export class AppModule {}
