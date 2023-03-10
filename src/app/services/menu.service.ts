import {Injectable} from "@angular/core";
import {Subject} from "rxjs";

@Injectable()
export class MenuService {
  constructor() { }

  private emitToggleMenu = new Subject<any>();

  toggleMenuEmitted$ = this.emitToggleMenu.asObservable();

  toggleMenu(event: any) {
    this.emitToggleMenu.next(event);
  }
}
