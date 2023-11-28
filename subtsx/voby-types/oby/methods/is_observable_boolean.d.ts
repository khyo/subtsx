import type { ObservableReadonly } from '../types';
declare const isObservableBoolean: (value: unknown) => value is ObservableReadonly<boolean>;
export default isObservableBoolean;
