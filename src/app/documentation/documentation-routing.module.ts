import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';

import { DocumentationComponent } from './documentation.component';

const routes: Routes = [
  {
    path: ':title',
    component: DocumentationComponent,
  },
  {
    path: '',
    component: DocumentationComponent,
  },
];

@NgModule({
  imports: [RouterModule.forChild(routes)],
  exports: [RouterModule],
})
export class DocumentationRoutingModule {}
