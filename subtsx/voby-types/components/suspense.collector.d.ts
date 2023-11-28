import type { SuspenseCollectorData } from '../types';
declare const SuspenseCollector: {
    create: () => SuspenseCollectorData;
    get: () => SuspenseCollectorData | undefined;
    wrap: <T>(fn: (data: SuspenseCollectorData) => T) => (() => T) extends infer T_1 ? T_1 extends () => T ? T_1 extends import("oby/dist/types").Resolvable ? T_1 : never : never : never;
};
export default SuspenseCollector;
