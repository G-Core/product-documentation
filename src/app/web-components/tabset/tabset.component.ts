import {
    AfterViewInit,
    ChangeDetectionStrategy,
    ChangeDetectorRef,
    Component,
    ElementRef,
    OnDestroy,
    Renderer2,
    ViewChild,
} from '@angular/core';
import { ActivatedRoute } from '@angular/router';
import { Subscription } from 'rxjs';
import { v4 as uuidv4 } from 'uuid';
import { HEADER_HEIGHT, headerTagNameList } from '../../constants';

@Component({
    selector: 'gc-tabset',
    templateUrl: './tabset.component.html',
    styleUrls: ['./tabset.component.scss'],
    changeDetection: ChangeDetectionStrategy.OnPush,
})
export class TabsetComponent implements OnDestroy, AfterViewInit {
    @ViewChild('tabset') public tabset: ElementRef;

    public buttons: Array<{ id: string; title: string }> = [];

    public tabs: Array<HTMLInputElement> = [];

    private tagType = '';

    private subscription: Subscription;

    constructor(private renderer: Renderer2, private route: ActivatedRoute, private cdr: ChangeDetectorRef) {}

    public activeTab = 0;

    public ngAfterViewInit(): void {
        const tabset = this.tabset.nativeElement;
        const elements = [...tabset.childNodes] as Array<HTMLElement>;

        const content = elements.reduce(this.sortTags, []);

        const tabsetName = uuidv4();

        this.buttons.forEach((button, i) => {
            const tab = this.renderer.createElement('div');
            this.renderer.addClass(tab, 'tab');

            const input = this.renderer.createElement('input');
            input.type = 'radio';
            input.id = button.id;
            input.name = tabsetName;
            input.checked = !i;
            this.tabs = [...this.tabs, input];

            tab.append(...content[i]);
            tabset.append(input, tab);
        });

        if (this.subscription) {
            this.subscription.unsubscribe();
        }

        this.subscription = this.route.fragment.subscribe((fragment) => {
            let idx = 0;
            const tab = this.tabs.find((tab, i) => {
                if (tab.id === fragment) {
                    idx = i;
                    return true;
                }
                return false;
            });
            if (tab) {
                this.activeTabChange(idx);
                tab.checked = true;

                window.scrollTo({ top: tabset.offsetTop - HEADER_HEIGHT });
            }
        });

        this.cdr.detectChanges();
    }

    public ngOnDestroy(): void {
        this.subscription?.unsubscribe();
    }

    public activeTabChange(index: number): void {
        this.activeTab = index;
        this.cdr.detectChanges();
    }

    private sortTags = (acc: Array<Array<HTMLElement>>, el: HTMLElement): Array<Array<HTMLElement>> => {
        if (!el.tagName) {
            return acc;
        }

        if (headerTagNameList.includes(el.tagName) && (!this.tagType || this.tagType === el.tagName)) {
            if (!this.tagType) {
                this.tagType = el.tagName;
            }

            this.buttons = [...this.buttons, { id: el.id, title: el.textContent }];
            el.remove();
            return acc;
        }

        const n = this.buttons.length - 1;
        acc[n] = [...(acc[n] || []), el];
        return acc;
    };
}
