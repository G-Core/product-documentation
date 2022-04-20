import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';

import { DocumentationComponent } from './documentation.component';

const routes: Routes = [
  {
    path: 'Cloud',
    component: DocumentationComponent,
  },
  {
    path: 'CDN',
    component: DocumentationComponent,
  },
  {
    path: 'Protection',
    component: DocumentationComponent,
  },
  {
    path: 'Cloud/:title',
    component: DocumentationComponent,
  },
  {
    path: 'CDN/:title',
    component: DocumentationComponent,
  },
  {
    path: 'Protection/:title',
    component: DocumentationComponent,
  },
  {
    path: '',
    redirectTo: 'CDN',
    pathMatch: 'full',
  },
];

@NgModule({
  imports: [RouterModule.forChild(routes)],
  exports: [RouterModule],
})
export class DocumentationRoutingModule {}
