import * as React from "react";

import { cn } from "@/lib/utils";
import { CopyRegular, DismissFilled } from "@fluentui/react-icons";
import { useToast } from "@/hooks/use-toast";

const CopyAction = ({
  inputRef,
}: {
  inputRef: React.Ref<HTMLInputElement>;
}) => {
  const { toast } = useToast();

  return (
    <CopyRegular
      onClick={async () => {
        console.log(inputRef);
        if (inputRef) {
          if (typeof inputRef !== "function" && inputRef.current) {
            try {
              await navigator.clipboard.writeText(inputRef.current.value);
              toast({
                description: "The endpoint was copied to your clipboard",
              });
            } catch (err) {
              toast({
                description: "Copy to clipboard failed",
              });
            }
          }
        }
      }}
      className="cursor-pointer"
    />
  );
};

const ClearAction = ({ cb }: { cb: () => void }) => {
  return <DismissFilled onClick={cb} className="cursor-pointer" />;
};

interface Props extends React.InputHTMLAttributes<HTMLInputElement> {
  children?: React.ReactNode;
  copyable?: boolean;
  clearCallBack?: () => void;
}
const Input = React.forwardRef(
  (
    { className, type, children, copyable, clearCallBack, ...props }: Props,
    ref: React.Ref<HTMLInputElement>
  ) => {
    return (
      <div
        className={cn(
          "flex h-10 w-full items-center overflow-hidden rounded-md border border-input ring-offset-background focus-within:ring-2 focus-within:ring-ring focus-within:ring-offset-2",
          className
        )}
      >
        {children ? (
          <div className="flex h-full items-center bg-secondary px-2">
            {children}
          </div>
        ) : null}
        <input
          type={type}
          className="flex basis-full truncate bg-transparent px-2 text-sm placeholder:text-muted-foreground focus-visible:outline-none disabled:cursor-not-allowed disabled:opacity-50"
          ref={ref}
          {...props}
        />
        <div className="flex space-x-2 pr-2">
          {copyable ? <CopyAction inputRef={ref} /> : null}
          {clearCallBack ? <ClearAction cb={clearCallBack} /> : null}
        </div>
      </div>
    );
  }
);

Input.displayName = "Input";

export { Input };
