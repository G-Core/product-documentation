export interface WindowResizeEvent extends UIEvent {
    target: Window;
}

export enum DeviceTypeEnum {
    Mobile = 'Mobile',
    Tablet = 'Tablet',
    Desktop = 'Desktop',
}

export interface Device {
    type: DeviceTypeEnum;
    breakpoint: number;
}
