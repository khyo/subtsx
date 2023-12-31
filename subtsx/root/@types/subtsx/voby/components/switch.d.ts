import type { Child, ChildWithMetadata, FunctionMaybe, ObservableReadonly } from '../types';
declare const Switch: {
    <T>({ when, fallback, children }: {
        when: FunctionMaybe<T>;
        fallback?: Child;
        children: Child;
    }): ObservableReadonly<Child>;
    Case<T_1>({ when, children }: {
        when: T_1;
        children: Child;
    }): ChildWithMetadata<[T_1, Child]>;
    Default({ children }: {
        children: Child;
    }): ChildWithMetadata<[Child]>;
};
export default Switch;
