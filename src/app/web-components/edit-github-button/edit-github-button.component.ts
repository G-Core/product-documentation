import { ChangeDetectionStrategy, Component, OnInit } from '@angular/core';
import { DOCS_GITHUB_REPO } from '../../constants';

@Component({
    selector: 'gc-code-block',
    templateUrl: './edit-github-button.component.html',
    styleUrls: ['./edit-github-button.component.scss'],
    changeDetection: ChangeDetectionStrategy.OnPush,
})
export class EditGithubButtonComponent implements OnInit {
    public articleUrl: string = '';

    public ngOnInit(): void {
        const prevPage = document.referrer.split('/docs/')[1];
        this.articleUrl = `${DOCS_GITHUB_REPO}${prevPage}.md`;
    }
}
