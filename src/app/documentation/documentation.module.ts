import { CommonModule } from '@angular/common';
import { NgModule } from '@angular/core';
import { ScullyLibModule } from '@scullyio/ng-lib';

import { DocumentationRoutingModule } from './documentation-routing.module';
import { DocumentationComponent } from './documentation.component';

@NgModule({
  declarations: [DocumentationComponent],
  imports: [CommonModule, DocumentationRoutingModule, ScullyLibModule],
})
export class DocumentationModule {}
