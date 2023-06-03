import { createRef, useEffect } from "react";
import {
  AddSquareFilled,
  ArrowSortFilled,
  FilterFilled,
  LightbulbFilled,
  LockOpenFilled,
  PersonFilled,
  WeatherMoonFilled,
} from "@fluentui/react-icons";
import { Input } from "@/components/Input";
import { Button } from "@/components/Button";
import { Toaster } from "@/components/Toaster";
import { ComboboxDemo } from "@/components/Combobox";
import GithubLogoLight from "@/assets/github-mark.svg";
import GithubLogoDark from "@/assets/github-mark-white.svg";
import { atom, useAtom } from "jotai";

const colorSchemeAtom = atom<"light" | "dark">("light");

let initTheme = true;
const ThemeSelector = () => {
  const [colorScheme, setColorScheme] = useAtom(colorSchemeAtom);

  useEffect(() => {
    if (initTheme) {
      if (window.matchMedia("(prefers-color-scheme: dark)").matches)
        setColorScheme("dark");
      else if (window.matchMedia("(prefers-color-scheme: light)").matches)
        setColorScheme("light");
      initTheme = false;
    }
  }, [setColorScheme]);

  useEffect(() => {
    const lightMatchMedia = window.matchMedia("(prefers-color-scheme: light)");
    const darkMatchMedia = window.matchMedia("(prefers-color-scheme: dark)");

    const lightCb = (e: MediaQueryListEvent) =>
      e.matches && !localStorage.theme && setColorScheme("light");
    const darkCb = (e: MediaQueryListEvent) =>
      e.matches && !localStorage.theme && setColorScheme("dark");

    lightMatchMedia.addEventListener("change", lightCb);
    darkMatchMedia.addEventListener("change", darkCb);

    return () => {
      lightMatchMedia.removeEventListener("change", lightCb);
      darkMatchMedia.removeEventListener("change", darkCb);
    };
  }, [setColorScheme]);

  useEffect(() => {
    if (colorScheme === "dark") {
      document.documentElement.classList.add("dark");
    } else {
      document.documentElement.classList.remove("dark");
    }
  }, [colorScheme]);

  return (
    <Button
      onClick={() => setColorScheme(colorScheme === "dark" ? "light" : "dark")}
      variant={"outline"}
    >
      {colorScheme == "dark" ? (
        <LightbulbFilled className="h-5 w-5" />
      ) : (
        <WeatherMoonFilled className="h-5 w-5" />
      )}
    </Button>
  );
};

export const App = () => {
  const [colorScheme] = useAtom(colorSchemeAtom);

  const searchInput = createRef<HTMLInputElement>();
  const endpointInput = createRef<HTMLInputElement>();

  return (
    <div className="flex h-screen w-screen">
      <div className="flex h-full basis-2/5 flex-col space-y-4 border-r p-2">
        <div className="flex h-14 items-center justify-between rounded-lg border p-2">
          <h1 className="font-serif text-xl font-bold">HTTP Inspect</h1>
          <div className="flex items-center space-x-2">
            <Button variant={"outline"}>
              <a
                target="_blank"
                rel="noreferrer"
                href="https://github.com/sebastienwae/httpinspect"
              >
                {colorScheme === "dark" ? (
                  <img src={GithubLogoDark} alt="" className="h-5 w-5" />
                ) : (
                  <img src={GithubLogoLight} alt="" className="h-5 w-5" />
                )}
              </a>
            </Button>
            <ThemeSelector />
            <Button variant={"outline"}>
              <PersonFilled className="h-5 w-5" />
            </Button>
          </div>
        </div>
        <div className="flex items-center space-x-2">
          <Input
            clearCallBack={() => {
              if (searchInput.current) searchInput.current.value = "";
            }}
            placeholder="search..."
            ref={searchInput}
          />
          <FilterFilled className="h-5 w-5" />
          <ArrowSortFilled className="h-5 w-5" />
        </div>
      </div>
      <div className="flex h-full basis-full flex-col space-y-4 p-2">
        <div className="flex w-full basis-14 items-center rounded-lg border p-2">
          <div className="flex w-full items-center justify-between space-x-2">
            <div className="flex items-center space-x-2">
              <Button variant={"secondary"}>
                <AddSquareFilled className="h-5 w-5" />
                <span className="ml-1">New</span>
              </Button>
              <ComboboxDemo />
            </div>
            <div className="flex items-center space-x-2">
              <Input
                copyable={true}
                defaultValue={"https://test.com/endpoint/123"}
                ref={endpointInput}
                readOnly={true}
                className="w-96"
              >
                <span className="text-sm">Endpoint</span>
              </Input>
              <Button variant={"outline"}>
                <LockOpenFilled className="h-5 w-5 text-red-500" />
                <span className="ml-1">Public</span>
              </Button>
            </div>
          </div>
        </div>
      </div>
      <Toaster />
    </div>
  );
};
