import { AfterViewInit, Component, ElementRef, Renderer2, ViewChild } from '@angular/core';
import { v4 as uuidv4 } from 'uuid';

@Component({
    selector: 'gc-tabset',
    templateUrl: './tabset.component.html',
    styleUrls: ['./tabset.component.scss'],
})
export class TabsetComponent implements AfterViewInit {
    @ViewChild('tabset') public tabset: ElementRef;

    public buttons: Array<{ id: string; title: string }> = [];

    constructor(private renderer: Renderer2) {}

    public activeTab = 0;

    public ngAfterViewInit(): void {
        const tabset = this.tabset.nativeElement;
        const elements = [...tabset.childNodes] as Array<HTMLElement>;

        const content = elements.reduce((acc, el) => {
            if (!el.tagName) {
                return acc;
            }
            if (el.tagName === 'H6') {
                this.buttons = [...this.buttons, { id: uuidv4(), title: el.textContent }];
                return acc;
            }
            const n = this.buttons.length - 1;
            acc[n] = [...(acc[n] || []), el];
            return acc;
        }, []);

        const tabsetName = uuidv4();

        this.buttons.forEach((button, i) => {
            const tab = this.renderer.createElement('div');
            this.renderer.addClass(tab, 'tab');

            const input = this.renderer.createElement('input');
            input.type = 'radio';
            input.id = button.id;
            input.name = tabsetName;
            input.checked = !i;

            tab.append(...content[i]);
            tabset.append(input, tab);
        });
    }

    public activeTabChange(index: number): void {
        this.activeTab = index;
    }
}
