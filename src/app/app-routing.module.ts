import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { DocumentationComponent } from './components/documentation/documentation.component';
import { HomeComponent } from './components/home/home.component';

const routes: Routes = [
  { path: '', component: HomeComponent },
  {
    path: `documentation/cdn-dns`,
    component: DocumentationComponent,
  },
  {
    path: `documentation/video-streaming`,
    component: DocumentationComponent,
  },
  {
    path: `documentation/cloud-computing`,
    component: DocumentationComponent,
  },
  {
    path: `documentation/containers`,
    component: DocumentationComponent,
  },
  {
    path: `documentation/servers`,
    component: DocumentationComponent,
  },
  {
    path: `documentation/security`,
    component: DocumentationComponent,
  },
  {
    path: `documentation/cloud-storage`,
    component: DocumentationComponent,
  },
  {
    path: `documentation/infrastructure`,
    component: DocumentationComponent,
  },
  {
    path: `documentation/hybrid-cloud`,
    component: DocumentationComponent,
  },
  {
    path: `documentation/monitoring`,
    component: DocumentationComponent,
  },
  {
    path: `documentation/custom-services`,
    component: DocumentationComponent,
  },
  {
    path: `documentation/cdn-dns/:title`,
    component: DocumentationComponent,
  },
  {
    path: `documentation/video-streaming/:title`,
    component: DocumentationComponent,
  },
  {
    path: `documentation/cloud-computing/:title`,
    component: DocumentationComponent,
  },
  {
    path: `documentation/containers/:title`,
    component: DocumentationComponent,
  },
  {
    path: `documentation/servers/:title`,
    component: DocumentationComponent,
  },
  {
    path: `documentation/security/:title`,
    component: DocumentationComponent,
  },
  {
    path: `documentation/cloud-storage/:title`,
    component: DocumentationComponent,
  },
  {
    path: `documentation/infrastructure/:title`,
    component: DocumentationComponent,
  },
  {
    path: `documentation/hybrid-cloud/:title`,
    component: DocumentationComponent,
  },
  {
    path: `documentation/monitoring/:title`,
    component: DocumentationComponent,
  },
  {
    path: `documentation/custom-services/:title`,
    component: DocumentationComponent,
  },
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule],
})
export class AppRoutingModule {}
