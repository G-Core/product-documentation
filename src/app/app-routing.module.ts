import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { DocumentationComponent } from './components/documentation/documentation.component';
import { HomeComponent } from './components/home/home.component';
import { HEADER_HEIGHT } from './constants';

const routes: Routes = [
    { path: '', component: HomeComponent },
    {
        path: `:title`,
        children: [
            {
                path: '**',
                component: DocumentationComponent,
            },
        ],
        component: DocumentationComponent,
    },
];

@NgModule({
    imports: [
        RouterModule.forRoot(routes, {
            useHash: false,
            anchorScrolling: 'enabled',
            scrollOffset: [0, HEADER_HEIGHT + 16],
        }),
    ],
    exports: [RouterModule],
})
export class AppRoutingModule {}
