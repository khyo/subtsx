import type { Child, Classes, EventListener, Fragment, FunctionMaybe, ObservableMaybe, Ref, TemplateActionProxy } from '../types';
declare const setAttributeStatic: (element: HTMLElement, key: string, value: null | undefined | boolean | number | string) => void;
declare const setAttribute: (element: HTMLElement, key: string, value: FunctionMaybe<null | undefined | boolean | number | string>) => void;
declare const setChildReplacementFunction: (parent: HTMLElement, fragment: Fragment, child: (() => Child)) => void;
declare const setChildReplacementText: (child: string, childPrev: Node) => Node;
declare const setChildReplacement: (child: Child, childPrev: Node) => void;
declare const setChildStatic: (parent: HTMLElement, fragment: Fragment, fragmentOnly: boolean, child: Child, dynamic: boolean) => void;
declare const setChild: (parent: HTMLElement, child: Child, fragment?: Fragment) => void;
declare const setClassStatic: (element: HTMLElement, classes: string, force: boolean | null | undefined) => void;
declare const setClass: (element: HTMLElement, key: string, value: FunctionMaybe<null | undefined | boolean>) => void;
declare const setClassBooleanStatic: (element: HTMLElement, value: boolean, key: null | undefined | boolean | string, keyPrev?: null | undefined | boolean | string) => void;
declare const setClassesStatic: (element: HTMLElement, object: null | undefined | string | FunctionMaybe<null | undefined | boolean | string>[] | Record<string, FunctionMaybe<null | undefined | boolean>>, objectPrev?: null | undefined | string | FunctionMaybe<null | undefined | boolean | string>[] | Record<string, FunctionMaybe<null | undefined | boolean>>) => void;
declare const setClasses: (element: HTMLElement, object: Classes) => void;
declare const setEventStatic: (element: HTMLElement, event: string, value: null | undefined | EventListener) => void;
declare const setEvent: (element: HTMLElement, event: string, value: ObservableMaybe<null | undefined | EventListener>) => void;
declare const setHTMLStatic: (element: HTMLElement, value: null | undefined | number | string) => void;
declare const setHTML: (element: HTMLElement, value: FunctionMaybe<{
    __html: FunctionMaybe<null | undefined | number | string>;
}>) => void;
declare const setPropertyStatic: (element: HTMLElement, key: string, value: null | undefined | boolean | number | string) => void;
declare const setProperty: (element: HTMLElement, key: string, value: FunctionMaybe<null | undefined | boolean | number | string>) => void;
declare const setRef: <T>(element: T, value: Ref<T> | (Ref<T> | null | undefined)[] | null | undefined) => void;
declare const setStyleStatic: (element: HTMLElement, key: string, value: null | undefined | number | string) => void;
declare const setStyle: (element: HTMLElement, key: string, value: FunctionMaybe<null | undefined | number | string>) => void;
declare const setStylesStatic: (element: HTMLElement, object: null | undefined | string | Record<string, FunctionMaybe<null | undefined | number | string>>, objectPrev?: null | undefined | string | Record<string, FunctionMaybe<null | undefined | number | string>>) => void;
declare const setStyles: (element: HTMLElement, object: FunctionMaybe<null | undefined | string | Record<string, FunctionMaybe<null | undefined | number | string>>>) => void;
declare const setTemplateAccessor: (element: HTMLElement, key: string, value: TemplateActionProxy) => void;
declare const setProp: (element: HTMLElement, key: string, value: any) => void;
declare const setProps: (element: HTMLElement, object: Record<string, unknown>) => void;
export { setAttributeStatic, setAttribute, setChildReplacementFunction, setChildReplacementText, setChildReplacement, setChildStatic, setChild, setClassStatic, setClass, setClassBooleanStatic, setClassesStatic, setClasses, setEventStatic, setEvent, setHTMLStatic, setHTML, setPropertyStatic, setProperty, setRef, setStyleStatic, setStyle, setStylesStatic, setStyles, setTemplateAccessor, setProp, setProps };