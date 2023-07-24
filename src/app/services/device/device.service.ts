import { Injectable } from '@angular/core';
import { debounceTime, fromEvent, map, Observable, share, startWith } from 'rxjs';
import { Device, DeviceTypeEnum, WindowResizeEvent } from './device.interface';

export const DEVICES: Array<Device> = [
    {
        type: DeviceTypeEnum.Mobile,
        breakpoint: 576,
    },
    {
        type: DeviceTypeEnum.Tablet,
        breakpoint: 1128,
    },
    {
        type: DeviceTypeEnum.Desktop,
        breakpoint: Infinity,
    },
];

@Injectable({
    providedIn: 'root',
})
export class DeviceService {
    public deviceType$: Observable<DeviceTypeEnum>;
    public isMobile$: Observable<boolean>;
    private resize$: Observable<number>;

    constructor() {
        this.resize$ = this.windowResize$().pipe(
            map((event) => event.target.innerWidth),
            startWith(window.innerWidth),
            debounceTime(300),
        );

        this.deviceType$ = this.resize$.pipe(
            map((width) => {
                return this.getDeviceType(width);
            }),
        );

        this.isMobile$ = this.deviceType$.pipe(map((type) => type === DeviceTypeEnum.Mobile));
    }

    private windowResize$(): Observable<WindowResizeEvent> {
        return fromEvent(window, 'resize', {
            passive: true,
        }) as Observable<WindowResizeEvent>;
    }

    private getDeviceType(width: number): DeviceTypeEnum {
        return DEVICES.find((device) => width < device.breakpoint).type;
    }
}
