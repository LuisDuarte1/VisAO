// @generated by protobuf-ts 2.9.3
// @generated from protobuf file "main.proto" (package "visao", syntax proto3)
// tslint:disable
import type { RpcTransport } from "@protobuf-ts/runtime-rpc";
import type { ServiceInfo } from "@protobuf-ts/runtime-rpc";
import { VisAO } from "./main";
import { stackIntercept } from "@protobuf-ts/runtime-rpc";
import type { File } from "./main";
import type { FileUpload } from "./main";
import type { UnaryCall } from "@protobuf-ts/runtime-rpc";
import type { RpcOptions } from "@protobuf-ts/runtime-rpc";
/**
 * Interface exported by the server.
 *
 * @generated from protobuf service visao.VisAO
 */
export interface IVisAOClient {
    /**
     * @generated from protobuf rpc: UploadFile(visao.FileUpload) returns (visao.File);
     */
    uploadFile(input: FileUpload, options?: RpcOptions): UnaryCall<FileUpload, File>;
}
/**
 * Interface exported by the server.
 *
 * @generated from protobuf service visao.VisAO
 */
export class VisAOClient implements IVisAOClient, ServiceInfo {
    typeName = VisAO.typeName;
    methods = VisAO.methods;
    options = VisAO.options;
    constructor(private readonly _transport: RpcTransport) {
    }
    /**
     * @generated from protobuf rpc: UploadFile(visao.FileUpload) returns (visao.File);
     */
    uploadFile(input: FileUpload, options?: RpcOptions): UnaryCall<FileUpload, File> {
        const method = this.methods[0], opt = this._transport.mergeOptions(options);
        return stackIntercept<FileUpload, File>("unary", this._transport, method, opt, input);
    }
}
